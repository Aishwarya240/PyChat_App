# PyChat_App

**PyChat_App** — a desktop GUI app built with **Tkinter** that integrates chat and image-generation features (uses `diffusers` / Stable Diffusion pipeline).
This repository contains the GUI (`main.py`), a small `logo.py` helper and build artifacts. The app is intended as a local, self-contained chat / image-generation desktop prototype.

> ⚠️ The README below is written from the repository structure and the visible code imports (Tkinter, Pillow, diffusers, torch, threading). If you want me to tailor this README to exact command-line options, screenshots, or to include step-by-step code snippets from your `main.py`, paste the `main.py` source here or let me open the raw files and I’ll embed exact usage.

---

# Table of contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Install & run](#install--run)
* [Usage](#usage)
* [Build a standalone executable (optional)](#build-a-standalone-executable-optional)
* [Configuration & troubleshooting](#configuration--troubleshooting)
* [Files in this repo](#files-in-this-repo)
* [Contributing](#contributing)
* [License](#license)

---

# Features

* Simple desktop GUI built with **Tkinter** (chat window, input area, basic controls).
* Local image generation support using **Hugging Face Diffusers** (`StableDiffusionPipeline`) — can generate or edit images from text prompts (if pipeline is correctly configured and model weights are available).
* Basic file dialogs and save/load flows (typical for GUI apps).
* Threaded model calls so the UI doesn't freeze while generating images.

---

# Prerequisites

* **Python 3.10+** (recommended; 3.8+ likely works but newer is preferred)
* ~8+ GB RAM; for image generation with Stable Diffusion you will usually need a GPU with sufficient VRAM (or run small/low-VRAM models on CPU but expect it to be slow).
* (Optional) CUDA-enabled GPU and the matching **PyTorch** build to accelerate diffusers.

---

# Install & run

1. Clone the repository:

```bash
git clone https://github.com/Aishwarya240/PyChat_App.git
cd PyChat_App
```

2. (Recommended) Create a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install required packages.

Create a `requirements.txt` file (example included below). Then:

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`**

```
tk            # built-in with CPython on many platforms; if not, install your system's Tk dev package
pillow
torch         # select CPU or GPU wheel directly from pytorch.org for best compatibility
diffusers
transformers
accelerate
safetensors   # optional, recommended for some model weights
```

> **PyTorch note:** For GPU support, install the correct `torch` wheel from the official PyTorch instructions for your CUDA version. Example (Linux, CUDA 11.8):
>
> ```bash
> pip install torch --index-url https://download.pytorch.org/whl/cu118
> ```

4. Run the app:

```bash
python main.py
```

---

# Usage

* Launch the app (`python main.py`) — the GUI opens.
* Use the text input to type prompts or chat messages.
* If image-generation features are available in your build:

  * Enter a prompt and click **Generate Image** (or the button named in the UI) to request a new image.
  * Generated images can typically be previewed in the GUI and saved via a Save dialog.
* Use the **File** menu (if present) to load/save session logs, images, or to change settings.

---

# Build a standalone executable (optional)

You can package the app into a standalone executable using **PyInstaller**.

Example command (Windows):

```bash
pyinstaller --onefile --windowed main.py
```

Common PyInstaller notes:

* If your GUI loads external assets (icons, model files, templates), include them with `--add-data` or place them in a known relative path handled by your code.
* Some heavy ML dependencies (torch, diffusers) will make the generated .exe large; for distribution consider instructing users to install requirements instead of bundling ML models.

---

# Configuration & troubleshooting

**1. Slow / Out of memory while generating images**

* If you get GPU OOM errors, try smaller models or reduce image resolution.
* On CPU, image generation will be *very* slow — expect minutes per image.

**2. Torch / CUDA mismatch**

* If `torch` imports but CUDA isn't available, verify you installed the wheel matching your CUDA runtime. Use `torch.cuda.is_available()` to check.

**3. `diffusers` permissions**

* If loading models from Hugging Face hub, you might need to set the `HF_HOME` or use an authentication token for private/consented models.

**4. UI freezes while generating**

* The app uses threads to avoid blocking the GUI. If you still see freezes, ensure model calls run in a separate thread and heavy CPU/GPU usage is isolated.

**5. Missing Tkinter / Display issues**

* On Linux, you might need system packages like `tk-dev` or `python3-tk`:

  * Debian/Ubuntu: `sudo apt install python3-tk`
  * Fedora: `sudo dnf install python3-tkinter`

---

# Files in this repo (observed)

* `main.py` — main application entry (Tkinter GUI, model integration).
* `logo.py` — small helper for branding/logo text or ASCII art.
* `dist/`, `build/` — build artifacts (probably from PyInstaller).
* `.idea/`, `__pycache__/` — IDE and cache files.

If you'd like, I can:

* generate a polished `requirements.txt` pinned to versions,
* create a more detailed README with exact CLI flags and screenshots if you paste `main.py`,
* or produce a `setup.py` / `pyproject.toml` for packaging.

---

# Contributing

Contributions welcome! Suggested workflow:

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit & push; create a PR describing your changes

Please include tests (or manual test steps) for new features — especially where model loading or long-running tasks are involved.

---

# License

Add your preferred license file (e.g., `MIT`, `Apache-2.0`). If you want, I can suggest a LICENSE text and add it to the repo.

---
