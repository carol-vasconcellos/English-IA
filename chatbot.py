from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import random

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

prompts = [
    "Let's talk about movies.",
    "What do you think about traveling?",
    "Tell me about your favorite food.",
    "Do you like music? What kind?",
    "Have you read any good books lately?",
    "What's your hobby?",
    "Tell me about your day.",
    "Do you enjoy sports?",
]

chat_history_ids = None
max_turns = 6
turns = 0

def responder_mensagem(user_input):
    global chat_history_ids, turns

    if chat_history_ids is None or turns >= max_turns:
        prompt = random.choice(prompts)
        print(f"💡 AI inicia o tópico: {prompt}")
        new_input = prompt + " " + user_input
        chat_history_ids = None
        turns = 0
    else:
        new_input = user_input

    new_input_ids = tokenizer.encode(new_input + tokenizer.eos_token, return_tensors='pt')

    # Criar attention_mask para os tokens
    attention_mask = torch.ones(new_input_ids.shape, dtype=torch.long)

    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
    else:
        bot_input_ids = new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        attention_mask=attention_mask,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_p=0.9,
        temperature=0.8,
        no_repeat_ngram_size=3
    )

    resposta = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    turns += 1

    return resposta
