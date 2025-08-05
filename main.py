from chatbot import responder_mensagem
from feedback import analisar_texto
from speech import ouvir_audio
from tts import falar_texto
from tradutor import traduzir
from dotenv import load_dotenv
import os

def modo_texto():
    while True:
        entrada = input("\n🧑‍💻 Você (ou 'sair'): ").strip()
        if entrada.lower() in ['exit', 'sair']:
            print("👋 Encerrando o modo texto...")
            break

        if not entrada:
            print("🤖 AI: You seem quiet. Want me to start a topic?")
            falar_texto("You seem quiet. Want me to start a topic?")
            continue

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

if __name__ == "__main__":
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
