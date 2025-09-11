# Examples

<div class="examples-grid">
  <a href="./mm_structured_outputs" class="card feature" aria-label="Multimodal Structured Outputs with Gemma 3 and vLLM">
    <div class="card-bg" style="background-image: url('../img/structured-outputs-cover.png');"></div>
    <div class="card-content">
      <span class="card-label">STRUCTURED OUTPUTS</span>
      <h2 class="card-title feature-title">Multimodal Structured Outputs with Gemma 3 and vLLM</h2>
      <p class="card-desc">Evaluate image understanding with guided choice on HuggingFace's TheCauldron Dataset</p>
    </div>
  </a>

  <a href="./minhash-dedupe" class="card minhash" aria-label="MinHash Deduplication on Common Crawl">
    <div class="card-bg" style="background-image: url('../img/minhash-dedupe-cover2.png');"></div>
    <div class="card-content">
      <span class="card-label">HTML</span>
      <h3 class="card-title">MinHash Deduplication on Common Crawl</h3>
      <p class="card-desc">Clean web text at scale with MinHash, LSH Banding, and Connected Components.</p>
    </div>
  </a>

  <a href="./document-processing" class="card docproc" aria-label="Document Processing and OCR">
    <div class="card-bg" style="background-image: url('../img/document-processing-cover2.png');"></div>
    <div class="card-content">
      <span class="card-label">DOCUMENTS</span>
      <h3 class="card-title">Large Scale Document Processing and OCR</h3>
      <p class="card-desc">Load PDFs from S3, extract text, run layout analysis, and compute embeddings</p>
    </div>
  </a>

  <a href="./audio-transcription" class="card audio" aria-label="Audio Transcription with Whisper">
    <div class="card-bg" style="background-image: url('../img/audio-transcription-cover.jpg');"></div>
    <div class="card-content">
      <span class="card-label">MULTIMODAL</span>
      <h3 class="card-title">Audio Transcription with Whisper</h3>
      <p class="card-desc">Effortlessly transcribe audio to text at scale</p>
    </div>
  </a>

  <a href="./text-embeddings" class="card embeddings wide" aria-label="Text Embeddings with spaCy and Turbopuffer">
    <div class="card-bg" style="background-image: url('../img/text-embeddings-cover.jpg');"></div>
    <div class="card-content">
      <span class="card-label">EMBEDDINGS</span>
      <h3 class="card-title">Build a 100% GPU Utilization Text Embedding Pipeline featuring spaCy and Turbopuffer</h3>
      <p class="card-desc">Generate and store millions of text embeddings in vector databases using distributed GPU processing and state-of-the-art models.</p>
    </div>
  </a>

  <a href="./image-generation" class="card imagegen" aria-label="Generate Images with Stable Diffusion">
    <div class="card-bg" style="background-image: url('../img/image-generation-cover.jpg');"></div>
    <div class="card-content">
      <span class="card-label tight">INFERENCE</span>
      <h3 class="card-title">Generate Images with Stable Diffusion</h3>
      <p class="card-desc">Open Source image generation model on your own GPUs using Daft UDFs</p>
    </div>
  </a>

  <a href="./window-functions" class="card windows" aria-label="Window Functions: The Great Chocolate Race">
    <div class="card-bg" style="background-image: url('../img/window-functions-cover.jpg');"></div>
    <div class="card-content">
      <span class="card-label tight">ANALYTICS</span>
      <h3 class="card-title">Window Functions: The Great Chocolate Race</h3>
      <p class="card-desc">Transforming complex analytical challenges into elegant solutions</p>
    </div>
  </a>

  <a href="./llms-red-pajamas" class="card redpajamas" aria-label="Running LLMs on the Red Pajamas Dataset">
    <div class="card-bg" style="background-image: url('../img/llms-red-pajamas-cover.jpg');"></div>
    <div class="card-content">
      <span class="card-label tight">DATASETS</span>
      <h3 class="card-title">Running LLMs on the Red Pajamas Dataset</h3>
      <p class="card-desc">Perform similarity search on Stack Exchange questions using language models and embeddings.</p>
    </div>
  </a>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap');

.examples-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: auto;
  gap: 12px;
  margin: 8px 0;
}

.card {
  position: relative;
  display: block;
  background: #141519;
  border: 2px solid magenta;
  text-decoration: none;
  color: inherit;
  overflow: hidden;
}

.card-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: saturate(0.9) brightness(0.7);
}

.card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8) 12%, rgba(0,0,0,0.4) 35%, rgba(0,0,0,0) 65%);
  pointer-events: none;
}

.card-content {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  padding: 10px 16px 12px;
  color: #fff;
}

.card-label {
  position: absolute;
  top: 0px;
  left: 0px;
  display: inline-block;
  background: magenta;
  color: #fff;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.5px;
  padding: 4px 10px;
}

.card-label.tight { padding-left: 6px; padding-right: 6px; }

.card-title {
  margin: 0 0 6px 0;
  font-size: 16px;
  line-height: 1.2;
}

.feature-title {
  font-size: 64px;
}

.card-title,
.feature-title {
  font-family: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

.card-desc {
  margin: 0;
  font-size: 14px;
  color: #bababa;
}

/* Grid placement */
.feature { grid-column: 1 / span 2; grid-row: 1 / span 2; }
.minhash { grid-column: 3; grid-row: 1; }
.docproc { grid-column: 3; grid-row: 2; }
.audio { grid-column: 1; grid-row: 3; }
.wide { grid-column: 2 / span 2; grid-row: 3; }
.imagegen { grid-column: 1; grid-row: 4; }
.windows { grid-column: 2; grid-row: 4; }
.redpajamas { grid-column: 3; grid-row: 4; }

@media (max-width: 1024px) {
  .examples-grid {
    grid-template-columns: auto;
    grid-auto-rows: auto;
  }
  .feature { grid-column: 1 / span 2; grid-row: 1; min-height: 360px; }
  .minhash { grid-column: 1; grid-row: 2 / span 2; min-height: auto; }
  .docproc { grid-column: 2; grid-row: auto; }
  .audio { grid-column: 2; grid-row: auto; }
  .wide { grid-column: 1 / span 2; grid-row: auto; }
  .imagegen { grid-column: 1; grid-row: auto; }
  .windows { grid-column: 2; grid-row: auto; }
  .redpajamas { grid-column: 1 / span 2; grid-row: auto; }
  .feature-title { font-size: 28px; }
}

@media (max-width: 820px) {
  .examples-grid {
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
    gap: 16px;
  }
  .feature, .minhash, .docproc, .audio, .wide, .imagegen, .windows, .redpajamas {
    grid-column: auto;
    grid-row: auto;

  }
  .feature-title { font-size: 18px; }
  .card-title { font-size: 18px; }
  .card-desc { font-size: 13px; }
}
</style>
