# RAG + Voice (Whisper) + TTS för Raspberry Pi 5 (Svenska)

- **RAG:** indexera webbsidor & dokument (PDF/DOCX/TXT/MD)
- **Chat:** liten GGUF-modell via `llama.cpp` (svenska)
- **ASR:** mikrofon → `faster-whisper`
- **TTS:** läs upp svar (`pyttsx3`/`espeak-ng`)

## Hämta projektet
Ladda ner källkoden genom att klona repositoriet från GitHub:
```bash
git clone https://github.com/<ditt-användarnamn>/aiv1.git
cd aiv1
```

## Systempaket
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev build-essential \
                    portaudio19-dev espeak-ng git cmake
```

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Körning
Skapa din applikation i `main.py` och kör:
```bash
python main.py
```

