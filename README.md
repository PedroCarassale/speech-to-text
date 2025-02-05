# Audio Transcriber

Este proyecto permite convertir archivos de audio en texto utilizando `pydub` y `speech_recognition` en Python. Actualmente, soporta la transcripción de archivos WAV dividiéndolos en fragmentos de 30 segundos para mejorar la precisión.

## 📌 Características

- Transcripción de audio a texto utilizando Google Speech Recognition.
- Procesamiento de archivos WAV con `pydub`.
- División automática del audio en fragmentos de 30 segundos.
- Exportación del texto transcrito a un archivo `.txt`.
- Permite pasar la ruta del archivo WAV como parámetro.

## 🚀 Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/audio-transcriber.git
cd audio-transcriber
```

### 2️⃣ Instalar dependencias

Asegúrate de tener Python instalado y luego ejecuta:

```bash
pip install -r requirements.txt
```

Si `ffmpeg` no está instalado, instálalo con:

- **Windows (usando Chocolatey)**:
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

## 📖 Uso

### 1️⃣ Convertir un archivo de audio en texto

Para transcribir un archivo WAV, pásalo como parámetro al ejecutar el script:

```bash
python app.py ruta/del/archivo.wav
```

El texto transcrito se guardará en `transcripcion.txt` en la misma carpeta del script.

## 📌 Tecnologías utilizadas

- Python
- pydub
- speech_recognition
- ffmpeg

## 📄 Licencia

Este proyecto está bajo la licencia MIT. ¡Úsalo como quieras! 🚀
