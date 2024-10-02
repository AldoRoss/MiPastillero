"""
Archivo para declarar todas las funciones que se van a ocupar para el desarrollo
de este proyecto, aqui van a ir las funciones que se ocupen para desarrollar otras funciones
"""
import pyaudio
import wave
import keyboard 
import speech_recognition as sr

# Configuración para grabar audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "audio_recorded.wav"

def record_audio():
    """Función para grabar audio desde el micrófono hasta que se presione una tecla"""
    audio = pyaudio.PyAudio()

    # Iniciar la grabación
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Grabando audio... Presiona 'Espacio' para detener la grabación.")

    frames = []

    # Grabar hasta que se presione la tecla "Espacio"
    while True:
        if keyboard.is_pressed('space'):  # Detener si se presiona 'Espacio'
            print("Grabación terminada.")
            break
        data = stream.read(CHUNK)
        frames.append(data)

    # Detener la grabación
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Guardar el audio en un archivo WAV
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def audio_to_text():
    """Función para convertir el audio grabado a texto"""
    recognizer = sr.Recognizer()

    # Leer el archivo de audio
    with sr.AudioFile(OUTPUT_FILENAME) as source:
        audio = recognizer.record(source)

    try:
        # Usar el reconocimiento de voz de Google para convertir a texto
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Texto reconocido: " + text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error al solicitar el servicio de reconocimiento: {e}")

def addAlarmVoice():
    print('add Alarm with voice')
    return None

if __name__ == "__main__":
    # Grabar el audio sin duración predefinida, usando la tecla 'Espacio' para detener
    record_audio()

    # Convertir el audio a texto
    audio_to_text()
 

