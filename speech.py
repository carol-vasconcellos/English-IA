import speech_recognition as sr

def ouvir_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="en-US")
        return texto
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("❌ Erro ao conectar ao serviço de reconhecimento.")
        return None
