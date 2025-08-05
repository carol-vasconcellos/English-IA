import pyttsx3

def falar_texto(texto):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # ajuste se quiser outra voz
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print(f"🔇 Erro ao falar o texto: {e}")
        print("⚠️ Continuando sem áudio...")
