"""Redirect pocket-tts downloads from Hugging Face to ModelScope (anonymous, no token).
Usage: import modelscope_patch  BEFORE  TTSModel.load_model().
Falls back to the original Hugging Face download if ModelScope is unreachable.
"""
import os
from pathlib import Path

import requests

_CACHE = Path(os.environ.get("POCKET_TTS_MS_CACHE",
                             Path.home() / ".cache" / "pocket-tts-modelscope"))
_BASE_URL = "https://modelscope.cn/models/{repo_id}/resolve/master/{filename}"

def _download_from_modelscope(repo_id, filename):
    dest = _CACHE / repo_id / filename
    if dest.is_file():
        return str(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = str(dest) + ".part"
    with requests.get(_BASE_URL.format(repo_id=repo_id, filename=filename),
                      stream=True, timeout=600) as r:
        r.raise_for_status()
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
    os.replace(tmp, dest)
    return str(dest)

def _patched_hf_hub_download(repo_id, filename, revision=None, **kwargs):
    try:
        return _download_from_modelscope(repo_id, filename)
    except Exception:
        from huggingface_hub import hf_hub_download
        return hf_hub_download(repo_id=repo_id, filename=filename,
                               revision=revision, **kwargs)

def use_modelscope():
    import pocket_tts.utils.utils as _utils
    _utils.hf_hub_download = _patched_hf_hub_download

use_modelscope()
