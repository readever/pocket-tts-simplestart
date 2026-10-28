# 🎙️ pocket-tts-simplestart

Text-to-speech **and 5-second voice cloning** — 95 lines of pure Python. Runs entirely on CPU, no GPU, no API keys, no JavaScript.

Built with [SimpleStart](https://pypi.org/project/simplestart/) (UI + interaction) and [Kyutai Pocket TTS](https://github.com/kyutai-labs/pocket-tts) (voice synthesis, MIT license).

> ⚠️ Not affiliated with Kyutai Labs. Pocket TTS is their project. Please only clone voices you have permission to use.

<!-- TODO: 填入在线演示 URL -->
> 在线演示：[ModelScope 空间]()

## ✨ Features

- **5-second zero-shot cloning** — drop any audio clip, no transcript needed, any language
- **9 built-in voices** with instant preview
- **CPU-only inference** — ~2-3x real-time on a laptop, shows per-generation speed badge
- **Background generation** — page stays responsive while synthesizing
- **95 lines** — the whole app is [app.py](app.py), zero front-end code

## 🚀 Quickstart

```bash
pip install -r requirements.txt
ss app.py
```

首次启动会自动下载约 200MB 模型权重（默认走 ModelScope 国内直连，无需登录；不可达时回退 Hugging Face）。打开终端打印的 `http://localhost:8000` 即可使用。

## 🧬 How voice cloning works

Pocket TTS is zero-shot: it captures timbre, accent, cadence and microphone character from a 5-second reference clip — no fine-tuning, no transcript. The app only passes a `voice` parameter (either a built-in voice name, or a wav file path); everything else goes through the same API.

## 📦 What's included

```
app.py                  # the whole app (95 lines)
modelscope_patch.py     # redirects weight downloads to ModelScope (no token)
assets/voice_samples/   # 9 built-in voice previews
requirements.txt
LICENSE
```

## 🙏 Credits

- TTS engine: [Kyutai Pocket TTS](https://github.com/kyutai-labs/pocket-tts) (MIT)
- Voice samples: [kyutai/tts-voices](https://huggingface.co/kyutai/tts-voices) — LibriVox/voice-zero (CC0), VCTK (CC BY 4.0), Alba MacKenna (CC BY 4.0)

## 📄 License

MIT — see [LICENSE](LICENSE).

---

## 中文

**95 行纯 Python 文字转语音 + 声音克隆**：上传 5 秒参考音频即可克隆音色（无需文稿、不限语言），或使用 9 个内置音色。全程 CPU 运行，无需 GPU 和 API Key。

```bash
pip install -r requirements.txt
ss app.py
```

首次启动自动下载约 200MB 模型权重（默认 ModelScope 国内直连，无需登录）。克隆声音请确保已获得授权。
