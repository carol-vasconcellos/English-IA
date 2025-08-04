from chatbot import responder_mensagem
from speech import ouvir_audio
from feedback import analisar_texto
from tts import falar_texto
from googletrans import Translator

translator = Translator()

def traduzir(texto):
    traducao = translator.translate(texto, dest='pt')
    return traducao.text

def modo_texto():
    while True:
        entrada = input("\n🧑‍💻 Você (ou 'sair'): ").strip()
        if entrada.lower() in ['exit', 'sair']:
            print("👋 Encerrando o modo texto...")
            break

        analisar_texto(entrada)
        resposta = responder_mensagem(entrada)
        print(f"\n🤖 AI: {resposta}")
        print(f"📘 Tradução: {traduzir(resposta)}")
        falar_texto(resposta)

def modo_voz():
    while True:
        print("\n🎤 Fale algo em inglês ou diga 'sair' para encerrar...")
        entrada = ouvir_audio()
        if entrada:
            if entrada.lower() in ['exit', 'sair']:
                print("👋 Encerrando o modo voz...")
                break

            print(f"\n📝 Você disse: {entrada}")
            analisar_texto(entrada)
            resposta = responder_mensagem(entrada)
            print(f"\n🤖 AI: {resposta}")
            print(f"📘 Tradução: {traduzir(resposta)}")
            falar_texto(resposta)
        else:
            print("❌ Não entendi. Tente novamente.")

def menu():
    print("\n🎓 EnglishCoach AI - Menu")
    print("1. Praticar com texto")
    print("2. Praticar com voz")
    print("3. Sair")

while True:
    menu()
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        modo_texto()
    elif opcao == "2":
        modo_voz()
    elif opcao == "3":
        print("👋 Até a próxima!")
        break
    else:
        print("❌ Opção inválida.")
