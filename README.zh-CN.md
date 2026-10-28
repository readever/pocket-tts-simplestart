# 🎙️ pocket-tts-simplestart

[English](README.md) | [中文](README.zh-CN.md)

**96 行纯 Python 文字转语音 + 声音克隆**。全程 CPU 运行，无需 GPU、API Key、JavaScript。

使用 [SimpleStart](https://pypi.org/project/simplestart/)（界面与交互）和 [Kyutai Pocket TTS](https://github.com/kyutai-labs/pocket-tts)（语音合成，MIT 协议）构建。

> ⚠️ 本项目与 Kyutai Labs 无关，Pocket TTS 是他们的项目。克隆他人声音前请确认已获得授权。

> 在线演示：[ModelScope 创空间](https://modelscope.cn/studios/simplestart/PocketTTS_SimpleStart_Demo)

## ✨ 特性

- **5 秒零样本克隆** — 任意语言、任意音频片段，无需文稿
- **9 个内置音色**，支持即时试听
- **纯 CPU 推理** — 笔记本上约 2~3 倍实时速度，每次生成显示速度徽章
- **后台生成** — 合成期间页面保持响应
- **96 行** — 整个应用就是 [app.py](app.py)，零前端代码

## 🚀 快速开始

```bash
pip install -r requirements.txt
ss app.py            # 也可用 simplestart app.py，两个别名等价
```

首次启动自动下载约 200MB 模型权重（默认走 ModelScope 国内直连，无需登录；不可达时回退 Hugging Face）。浏览器打开 `http://localhost:8000` 即可使用。

## 🧬 克隆原理

Pocket TTS 是零样本方案：一段 5 秒参考音频即可捕捉音色、口音、节奏甚至麦克风特征，无需微调、无需文稿。应用只传一个 `voice` 参数（内置音色名或 wav 文件路径），底层走同一条 API。

## 📦 项目结构

```
app.py                  # 整个应用（96 行）
modelscope_patch.py     # 把权重下载重定向到 ModelScope（无需 token）
assets/voice_samples/   # 9 个内置音色预览
requirements.txt
LICENSE
```

## 🙏 致谢

- TTS 引擎：[Kyutai Pocket TTS](https://github.com/kyutai-labs/pocket-tts)（MIT）
- 音色样本：[kyutai/tts-voices](https://huggingface.co/kyutai/tts-voices) — LibriVox/voice-zero（CC0）、VCTK（CC BY 4.0）、Alba MacKenna（CC BY 4.0）

## 🔗 相关资源

- [SimpleStart 框架](https://github.com/readever/simplestart) — 本应用使用的框架
- [SimpleStart 中文文档](https://www.simplestart.cc/zh)

## 📄 协议

MIT — 见 [LICENSE](LICENSE)。
