"""
Archivo para declarar todas las funciones que se van a ocupar para el desarrollo
de este proyecto, aqui van a ir las funciones que se ocupen para desarrollar otras funciones
"""
import pyaudio
import wave
import tkinter as tk
from threading import Thread
import speech_recognition as sr

# Configuración para grabar audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "audio_recorded.wav"
frames = []  # Para almacenar los fragmentos de audio
stream = None
audio = None

def start_recording():
    """Función para comenzar a grabar el audio"""
    global stream, audio, frames
    audio = pyaudio.PyAudio()

    # Iniciar la grabación
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Grabando audio...")
    frames = []  # Limpiar frames anteriores

    def record_loop():
        while recording_active:  # Mientras no se detenga la grabación
            data = stream.read(CHUNK)
            frames.append(data)

    # Ejecutar la grabación en un hilo separado
    global recording_thread
    recording_thread = Thread(target=record_loop)
    recording_thread.start()

def stop_recording():
    """Función para detener la grabación"""
    global stream, audio

    print("Grabación detenida.")
    
    global recording_active
    recording_active = False  # Cambiar estado de la grabación

    # Esperar a que el hilo termine
    recording_thread.join()

    # Detener y cerrar el flujo de grabación
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Guardar el audio en un archivo WAV
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    # Convertir el audio a texto
    audio_to_text()

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

def on_start_button_click():
    """Función que se ejecuta al hacer clic en el botón de iniciar grabación"""
    global recording_active
    recording_active = True
    start_recording()

def on_stop_button_click():
    """Función que se ejecuta al hacer clic en el botón de detener grabación"""
    stop_recording()