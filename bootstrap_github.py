#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skapar ett komplett Raspberry Pi 5-projekt:
- RAG (webb + dokument) med llama.cpp-embeddings + hnswlib
- LLM-chatt (svenska) via llama.cpp (GGUF)
- Whisper ASR via mikrofon (faster-whisper)
- TTS (pyttsx3/espeak-ng)
- GitHub-redo struktur (.gitignore, LICENSE, README, körskript)
"""
import os, pathlib, textwrap

root = pathlib.Path(".")
proj = root

# ---------- .gitignore ----------
(proj / ".gitignore").write_text(textwrap.dedent("""
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.egg-info/
.eggs/
.env
.venv
venv/
build/
dist/

# Data & modeller
index/
data/
models/
logs/
*.wav
*.mp3

# OS
.DS_Store
Thumbs.db
""").strip()+"\n", encoding="utf-8")

# ---------- LICENSE ----------
(proj / "LICENSE").write_text(textwrap.dedent("""
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
""").strip()+"\n", encoding="utf-8")

# ---------- requirements.txt ----------
(proj / "requirements.txt").write_text(textwrap.dedent("""
# LLM + RAG
llama-cpp-python>=0.3.5
hnswlib>=0.8.0
numpy>=1.26.0
requests>=2.32.0
beautifulsoup4>=4.12.0
pypdf>=4.2.0
python-docx>=1.1.0
tqdm>=4.66.0

# ASR (Whisper)
faster-whisper>=1.0.3

# Audio I/O
sounddevice>=0.4.7
soundfile>=0.12.1

# VAD (valfritt men bra)
webrtcvad>=2.0.10; platform_system != "Windows"

# TTS (pyttsx3 använder espeak-ng på Linux)
pyttsx3>=2.90
""").strip()+"\n", encoding="utf-8")

# ---------- README.md ----------
(proj / "README.md").write_text(textwrap.dedent("""
# RAG + Voice (Whisper) + TTS för Raspberry Pi 5 (Svenska)

- **RAG:** indexera webbsidor & dokument (PDF/DOCX/TXT/MD)
- **Chat:** liten GGUF-modell via `llama.cpp` (svenska)
- **ASR:** mikrofon → `faster-whisper`
- **TTS:** läs upp svar (`pyttsx3`/`espeak-ng`)

## Systempaket
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev build-essential \\
                    portaudio19-dev espeak-ng git cmake
