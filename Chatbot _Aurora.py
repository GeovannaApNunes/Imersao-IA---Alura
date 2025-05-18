# 🔐 Chave da API via Colab
import os
from google.colab import userdata
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

# 📦 Importando Gemini
from google import genai
from google.genai import types

# 🚀 Iniciando cliente Gemini
client = genai.Client()

# 🤖 Modelo e configuração da IA Aurora
modelo = "models/gemini-1.5-flash"

chat_config = types.GenerateContentConfig(
    system_instruction = """
    Você é Aurora, uma assistente virtual dedicada a ajudar causas sociais.
    Sua missão é fornecer informações acessíveis, claras e empáticas sobre temas como educação, sustentabilidade, direitos humanos e inclusão.
    Suas respostas devem ser breves, respeitosas e sempre incentivar o bem comum.
    Evite termos técnicos complexos e sempre seja acolhedora.
    """
)

chat = client.chats.create(model=modelo, config=chat_config)

# 🌟 Mensagem de boas-vindas
print("🌍 Iniciando a conversa com Aurora - Assistente para Causas Sociais")
print("Digite 'fim' para encerrar.\n")

# 🔁 Loop de interação
while True:
    prompt = input("Você: ")
    if prompt.lower().strip() == "fim":
        print("\nAurora: Obrigada por conversar comigo! Continue espalhando o bem. 💚")
        break
    elif prompt.lower().strip() == "histórico":
        print("\n🕘 Histórico da conversa:")
        for i, (pergunta, resposta) in enumerate(historico, start=1):
            print(f"{i}. Você: {pergunta}")
            print(f"   Aurora: {resposta}\n")
        continue

    resposta = chat.send_message(prompt)
    print(f"Aurora: {resposta.text}\n")
