"""WARNING! These APIs are internal; please use Catalog.from_lance() and Table.from_lance()."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Any

from daft.catalog import Catalog, Identifier, NotFoundError, Properties, Schema, Table
from daft.io._lance import read_lance

if TYPE_CHECKING:
    from daft.dataframe import DataFrame
    import lance


class LanceTable(Table):
    """A Daft Table implementation that wraps a LanceDB Table.

    This class bridges LanceDB's high-level table API with Daft's catalog system.
    Reading is done by converting the LanceDB table to a Lance dataset and using
    Daft's existing read_lance functionality. Writing uses LanceDB's native add() API.
    """
    _inner: lance.dataset.LanceDataset

    _read_options = {"version", "asof"}  # LanceDB-specific read options
    _write_options: set[str] = set()

    def __init__(self, inner: lance.LanceDataset):
        """Please use `Table.from_lance` instead."""
        self._inner = inner

    @property
    def name(self) -> str:
        """Return the table name from the LanceDB table."""
        return self._inner.name

    @property
    def uri(self) -> str:
        """Return the table URI from the LanceDB table."""
        return self._inner.uri

    def schema(self) -> Schema:
        """Get schema directly from LanceDB table to avoid circular dependency."""
        return Schema.from_pyarrow_schema(self._inner.schema)

    @staticmethod
    def _from_obj(obj: object) -> LanceTable:
        """Returns a LanceTable if the given object can be adapted so."""
        # Import here to avoid circular imports and allow optional dependency
        try:
            import lance
            from lancedb import  LanceTable as LanceDBTable, AsyncTable as LanceDBAsyncTable

        except ImportError as e:
            raise ImportError(
                "Unable to import the `lancedb` package, please ensure that LanceDB is installed: `pip install lancedb`"
            ) from e

        if isinstance(obj, LanceDBTable):
            t = LanceTable()
            t._inner = obj.to_lance()
            return t
        if isinstance(obj, LanceDBAsyncTable):
            t = LanceTable()
            t._inner = obj._inner.to_lance()
            return t
        if isinstance(obj, lance.LanceDataset):
            t = LanceTable()
            t._inner = obj
            return t
        raise ValueError(f"Unsupported lance table type: {type(obj)}")

    def read(self, **options: Any) -> DataFrame:
        """Read from LanceDB table by converting to Lance dataset and using read_lance.

        This implements the bridge pattern: LanceDB Table → Lance Dataset → Daft DataFrame
        """
        Table._validate_options("Lance read", options, LanceTable._read_options)

        return self._read_lance_from_dataset(self._inner, **options)

    def _read_lance_from_dataset(self, lance_dataset: "lance.LanceDataset", **options: Any) -> DataFrame:
        """Helper method to read from a Lance dataset directly.

        This reuses the logic from read_lance() but works with an existing dataset
        instead of creating one from a URL.
        """
        from daft.lance.lance_scan import LanceScanOperator
        from daft.daft import ScanOperatorHandle
        from daft.logical.builder import LogicalPlanBuilder
        from daft.dataframe import DataFrame

        # Reuse the existing LanceScanOperator logic
        scan_operator = LanceScanOperator(lance_dataset)
        handle = ScanOperatorHandle.from_python_scan_operator(scan_operator)
        builder = LogicalPlanBuilder.from_tabular_scan(scan_operator=handle)
        return DataFrame(builder)

    def append(self, df: DataFrame, **options: Any) -> None:
        """Append data to LanceDB table using its native add() API."""
        self._validate_options("Lance write", options, LanceTable._write_options)

        # Bridge: Convert Daft DataFrame to Arrow Table and use LanceDB API
        arrow_table = df.to_arrow()
        self._inner.add(arrow_table, mode="append")

    def overwrite(self, df: DataFrame, **options: Any) -> None:
        """Overwrite LanceDB table using its native add() API."""
        self._validate_options("Lance write", options, LanceTable._write_options)

        # Bridge: Convert Daft DataFrame to Arrow Table and use LanceDB API
        arrow_table = df.to_arrow()
        self._inner.add(arrow_table, mode="overwrite")


def _to_lance_ident(ident: Identifier | str) -> tuple[str, ...] | str:
    """Convert Daft identifier to Lance identifier format."""
    return tuple(ident) if isinstance(ident, Identifier) else ident
