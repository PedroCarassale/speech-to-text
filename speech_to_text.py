import os
import shutil
import sys
from pydub import AudioSegment
import speech_recognition as sr

# Obtener el archivo de audio desde los parámetros
if len(sys.argv) < 2:
    print("Por favor, proporciona la ruta del archivo de audio.")
    sys.exit(1)

archivo = sys.argv[1]
temp_folder = "temp"

# Crear la carpeta temporal
os.makedirs(temp_folder, exist_ok=True)

# Cargar el archivo
audio = AudioSegment.from_wav(archivo)

# Dividir en fragmentos de 30 segundos
fragmentos = [audio[i:i+30000] for i in range(0, len(audio), 30000)]

recognizer = sr.Recognizer()
transcripcion_completa = ""

for i, fragmento in enumerate(fragmentos):
    fragmento_path = os.path.join(temp_folder, f"fragmento_{i}.wav")
    fragmento.export(fragmento_path, format="wav")
    with sr.AudioFile(fragmento_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="es-ES")
            transcripcion_completa += f"{text} "  # Agregar el texto con un espacio entre fragmentos
        except sr.UnknownValueError:
            transcripcion_completa += "[No se pudo entender el audio] "
        except sr.RequestError as e:
            transcripcion_completa += f"[Error con el servicio de reconocimiento: {e}] "

# Guardar la transcripción en un archivo de texto
ruta_salida = "./transcripcion.txt"
with open(ruta_salida, "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(transcripcion_completa)

# Eliminar la carpeta temporal y su contenido
shutil.rmtree(temp_folder)