# Speech To Text

This project allows converting audio files into text using `pydub` and `speech_recognition` in Python. Currently, it supports the transcription of WAV files by splitting them into 30-second fragments to improve accuracy.

## 📌 Features

- Audio-to-text transcription using Google Speech Recognition.
- WAV file processing with `pydub`.
- Automatic division of audio into 30-second fragments.
- Exporting transcribed text to a `.txt` file.
- Allows passing the WAV file path as a parameter.

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PedroCarassale/speech-to-text.git
cd speech-to-text
```

### 2️⃣ Install dependencies

Make sure you have Python installed and then run:

```bash
pip install -r requirements.txt
```

If `ffmpeg` is not installed, install it using:

- **Windows (using Chocolatey)**:
  ```powershell
  choco install ffmpeg
  ```
- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install ffmpeg
  ```
- **MacOS (Homebrew)**:
  ```bash
  brew install ffmpeg
  ```

## 📖 Usage

### 1️⃣ Convert an audio file to text

To transcribe a WAV file, pass it as a parameter when running the script:

```bash
python speech_to_text.py path/to/audio.wav
```

The transcribed text will be saved as `transcription.txt` in the same folder as the script.

## 📌 Technologies Used

- Python
- pydub
- speech_recognition
- ffmpeg

## 📄 License

This project is licensed under the MIT License. Use it as you like! 🚀
