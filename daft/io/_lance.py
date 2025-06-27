from math import isinf
from pip._vendor.requests import options
# ruff: noqa: I002
# isort: dont-add-import: from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

from daft import context
from daft.api_annotations import PublicAPI
from daft.daft import IOConfig, ScanOperatorHandle
from daft.dataframe import DataFrame
from daft.io.object_store_options import io_config_to_storage_options
from daft.io.scan import ScanOperator
from daft.logical.builder import LogicalPlanBuilder
from tests.integration.sql.test_sql import pdf

from daft.lance.lance_scan import LanceScanOperator
from collections.abc import Iterator


if TYPE_CHECKING:
    import lance
    from datetime import datetime
    from pathlib import Path


@PublicAPI
def read_lance(
    table: Union[str, Path, "lance.LanceDataset"],
    version: Optional[Union[int | str]] = None,
    asof: Optional[Union[datetime, str]] = None,
    io_config: Optional[IOConfig] = None,
) -> DataFrame:
    """Create a DataFrame from a Lance dataset.

    Args:
        url (str): URL to the Lance dataset (supports remote URLs to object stores such as `s3://` or `gs://`)
        version (optional, int | str): load a specific version of the Lance dataset. Else, loads the latest version. A version number (`int`) or a tag (`str`) can be provided.
        asof (optional, datetime or str): find the latest version created on or earlier than the given argument value. If a version is already specified, this arg is ignored.
        io_config (optional: IOConfig): A custom IOConfig to use when accessing Lance data. Defaults to None.

    Returns:
        DataFrame: a DataFrame with the schema converted from the specified Lance dataset

    Note:
        This function requires the use of [Lance](https://github.com/lancedb/lance), which provides
        the underlying dataset format. To ensure that this is installed with Daft, you may install:
        `pip install daft[lance]`

    Examples:
        Read a local Lance dataset:
        >>> df = daft.read_lance("/path/to/dataset")
        >>> df.show()

        Read a specific version (time travel):
        >>> df = daft.read_lance("/path/to/dataset", version=5)
        >>> df.show()

        Read a Lance dataset from a public S3 bucket with optimized caching:
        >>> from daft.io import S3Config
        >>> s3_config = S3Config(region="us-west-2", anonymous=True)
        >>> df = daft.read_lance(
        ...     "s3://daft-public-data/lance/words-test-dataset",
        ...     io_config=s3_config,
        ...     index_cache_size=256 * 1024 * 1024,  # 256MB index cache
        ...     metadata_cache_size=128 * 1024 * 1024,  # 128MB metadata cache
        ... )
        >>> df.show()
    """
    try:
        import lance
    except ImportError as e:
        raise ImportError(
            "Unable to import the `lance` package, please ensure that Daft is installed with the lance extra dependency: `pip install daft[lance]`"
        ) from e

    if (isinstance(table, str) | isinstance(table, Path)):
        uri = table
    else:
        uri = table.uri

    io_config = context.get_context().daft_planning_config.default_io_config if io_config is None else io_config
    storage_options = io_config_to_storage_options(io_config, uri)

    # Read dataset
    ds = lance.dataset(
        uri=uri,
        version=version,
        asof=asof,
        storage_options=storage_options,
    )
    lance_operator = LanceScanOperator(ds)

    handle = ScanOperatorHandle.from_python_scan_operator(lance_operator)
    builder = LogicalPlanBuilder.from_tabular_scan(scan_operator=handle)
    return DataFrame(builder)
