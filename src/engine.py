"""
Motor de análise da Mission Control AI
"""

import os
from pathlib import Path

from ollama import Client
from dotenv import load_dotenv

from src.telemetria import coletar
from src.alertas import avaliar

load_dotenv()

TRILHA = "envirosat"

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")
    }
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):

    messages = []

    if system:
        messages.append(
            {
                "role": "system",
                "content": system
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    try:

        resposta = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={
                "num_predict": max_tokens,
                "temperature": temperature
            },
            stream=False
        )

        return resposta["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"


def load_system_prompt():

    path = Path("prompts/system_prompt.md")

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "Você é um assistente espacial."


class MissionEngine:

    def __init__(self):

        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):

        return True

    def status_snapshot(self):

        dados = coletar()

        texto = f"""
🛰️ STATUS ATUAL DA MISSÃO

🔋 Energia: {dados['energia']}%
🌡️ Temperatura: {dados['temperatura']}°C
🖼️ Buffer de imagens: {dados['buffer_imagens']}%
📍 Precisão GPS: {dados['precisao_gps']} m
🔥 Sensor térmico: {dados['sensor_termico']}%
"""

        return texto

    def analyze(self, pergunta_usuario):

        dados = coletar()

        alertas = avaliar(dados)

        prompt = f"""
PERGUNTA DO OPERADOR:
{pergunta_usuario}

TELEMETRIA ATUAL:

Energia: {dados['energia']}%
Temperatura: {dados['temperatura']}°C
Buffer de imagens: {dados['buffer_imagens']}%
Precisão GPS: {dados['precisao_gps']} m
Sensor térmico: {dados['sensor_termico']}%

ALERTAS DETECTADOS:

{chr(10).join(alertas)}

Analise a situação da missão e explique:

1. Estado atual do satélite
2. Gravidade da situação
3. Impacto terrestre
4. Recomendação operacional
"""

        resposta = llm(
            prompt=prompt,
            system=self.system_prompt
        )

        return resposta
