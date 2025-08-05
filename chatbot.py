import random
import requests

prompts = [
    "Let's talk about movies!",
    "What's your favorite dish to cook?",
    "If you could travel anywhere, where would you go?",
    "What kind of music do you like?",
    "Tell me something interesting that happened this week.",
]

history = []
max_history = 5  # reduzido por limitação do modelo gratuito

def responder_mensagem(user_input):
    global history

    if not user_input.strip():
        user_input = random.choice(prompts)
        print(f"💡 AI inicia o tópico: {user_input}")

    history.append({"role": "user", "content": user_input})

    # Monta o histórico em formato de string (modelo mistral não aceita JSON)
    conversation = ""
    for h in history[-max_history:]:
        role = "You" if h["role"] == "user" else "AI"
        conversation += f"{role}: {h['content']}\n"
    conversation += "AI:"

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
        headers={"Accept": "application/json"},
        json={"inputs": conversation},
    )

    if response.status_code != 200:
        return "⚠️ Erro ao se comunicar com o modelo gratuito da Hugging Face."

    data = response.json()
    resposta = data[0]["generated_text"].split("AI:")[-1].strip()

    history.append({"role": "assistant", "content": resposta})
    return resposta
