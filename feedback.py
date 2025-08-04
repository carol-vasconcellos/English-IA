import language_tool_python
from tts import falar_texto

tool = language_tool_python.LanguageTool('en-US')

def analisar_texto(texto):
    matches = tool.check(texto)
    if not matches:
        print("✅ Sem erros encontrados! Parabéns!")
        falar_texto("Great job! No mistakes found.")
        return

    print("❌ Foram encontrados os seguintes problemas:\n")
    for m in matches:
        print(f"👉 Erro: {m.message}")
        print(f"🔁 Sugestão: {m.replacements}")
        print(f"📍 Contexto: {m.context}")
        print("---")
    
    falar_texto("There are some mistakes. Let me show you.")
