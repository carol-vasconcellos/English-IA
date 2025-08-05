from deep_translator import GoogleTranslator

def traduzir(texto):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(texto)
    except Exception:
        return "(Erro na tradução)"
