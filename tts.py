import pyttsx3

def falar_texto(texto):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        
        voices = engine.getProperty('voices')
        # Vamos listar as vozes disponíveis para garantir que alguma seja usada
        for i, voice in enumerate(voices):
            print(f"Voice {i}: {voice.id} - {voice.name}")

        # Escolha uma voz que realmente exista no seu sistema (exemplo: primeira)
        if voices:
            engine.setProperty('voice', voices[0].id)
        
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print(f"🔇 Erro ao falar o texto: {e}")
        print("⚠️ Continuando sem áudio...")
