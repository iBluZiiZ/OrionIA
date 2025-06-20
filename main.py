import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Inicializar motor de voz
voz = pyttsx3.init()

def hablar(texto):
    print("ORION:", texto)
    voz.say(texto)
    voz.runAndWait()

def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-CL")
        print("Tú dijiste:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        hablar("No entendí, repite por favor.")
        return ""
    except sr.RequestError:
        hablar("Error de conexión con el reconocimiento de voz.")
        return ""

def ejecutar_comando(comando):
    if "hola orion" in comando:
        hablar("Hola Oscar, ¿en qué te puedo ayudar?")
    elif "abre google" in comando:
        webbrowser.open("https://www.google.com")
        hablar("Abriendo Google")
    elif "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora}")
    elif "salir" in comando:
        hablar("Hasta luego.")
        exit()

# Bucle principal
while True:
    comando = escuchar()
    if comando:
        ejecutar_comando(comando)
