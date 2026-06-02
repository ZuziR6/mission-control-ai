# Mission Control AI — EnviroSat Guardian

## Integrantes

* Gabriel Guimarães de Oliveira — RM: SEU_RM
* Pedro Paulo Ferreira Agnelo D'angelo — RM: RM_DO_PEDRO
* Nicolas Henriques Fernandes — RM: RM_DO_NICOLAS

Modalidade: Trio

---

# O que o projeto faz

O EnviroSat Guardian é um sistema inteligente de monitoramento de satélites ambientais inspirado em missões como Amazônia-1 e Landsat. O sistema coleta dados simulados de telemetria, identifica anomalias operacionais através de regras implementadas em Python e utiliza IA generativa via Ollama Cloud para produzir análises em linguagem natural.

Além da análise técnica, a IA traduz o impacto terrestre de cada ocorrência, permitindo que operadores entendam rapidamente como problemas em órbita podem afetar o combate a incêndios, o monitoramento ambiental e a preservação de áreas protegidas.

---

# Persona atendida

O sistema foi projetado para atender operadores de centros de monitoramento ambiental, analistas de compliance ambiental e coordenadores de brigadas de combate a incêndios.

Esses profissionais precisam interpretar rapidamente grandes volumes de dados operacionais para tomar decisões críticas relacionadas à proteção ambiental.

---

# Trilha escolhida

EnviroSat — Observação Ambiental

---

# Tecnologias utilizadas

* Python 3.10+
* Ollama Cloud API
* Modelo gpt-oss:120b
* Ollama
* Python Dotenv
* Rich
* Prompt Toolkit
* PyFiglet
* GitHub

---

# Como executar

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar arquivo .env

```env
OLLAMA_API_KEY=SUA_CHAVE
```

### 4. Executar

```bash
python main.py
```

---

# Funcionalidades

* Monitoramento de telemetria em tempo real
* Avaliação automática de parâmetros críticos
* Sistema de alertas operacionais
* Respostas automáticas para situações críticas
* Integração com IA generativa
* Tradução do impacto terrestre das anomalias
* Interface CLI inspirada no Claude Code

---

# Cenários de teste demonstrados

### Cenário 1 — Operação normal

Todos os parâmetros dentro dos limites aceitáveis.

### Cenário 2 — Energia crítica

Ativação automática do modo economia de energia.

### Cenário 3 — Temperatura crítica

Desligamento automático de sensores secundários.

### Cenário 4 — Buffer elevado

Alerta preventivo de armazenamento.

### Cenário 5 — Falha de geolocalização

Detecção de degradação na precisão da missão.

---

# Demonstração

![Banner do sistema](assets/screenshot_banner.png)

![Análise da IA](assets/screenshot_analise.png)

---

# System Prompt

O system prompt completo está disponível em:

```text
prompts/system_prompt.md
```

---

# Proposta de valor / Modelo de negócio

## 1. Qual problema terrestre esta missão resolve?

O sistema auxilia no monitoramento ambiental através da identificação rápida de incêndios florestais, desmatamento e degradação de áreas protegidas, reduzindo o tempo necessário para resposta operacional.

## 2. Quem paga pela solução?

Modelo híbrido.

Clientes incluem órgãos governamentais de monitoramento ambiental, institutos de pesquisa, empresas de geotecnologia e organizações privadas que dependem de dados ambientais.

## 3. Métrica de impacto

Mantendo o satélite operando com alta disponibilidade durante um ano, estima-se o monitoramento contínuo de milhões de hectares de áreas protegidas, contribuindo para a redução de danos ambientais e melhoria da resposta a incêndios.

## 4. Modelo de negócio

Data as a Service (DaaS).

Os clientes contratam acesso às análises, relatórios operacionais e dados processados gerados pela plataforma.

---

# Limitações conhecidas

* Utiliza dados simulados.
* Não se conecta a satélites reais.
* Não realiza previsão de eventos futuros.
* Não substitui sistemas operacionais de monitoramento governamentais.

---

# Vídeo de demonstração

LINK_DO_VIDEO_YOUTUBE

Configuração do vídeo: Não listado.

---

# Estrutura do projeto

mission-control-ai/

* main.py
* banner_ascii.py
* requirements.txt
* README.md

src/

* ui.py
* engine.py
* telemetria.py
* alertas.py

prompts/

* system_prompt.md

assets/

* screenshot_banner.png
* screenshot_analise.png

data/

* cenarios.json

---

# Conclusão

O EnviroSat Guardian demonstra a aplicação prática de IA generativa integrada à análise operacional de missões espaciais, conectando dados orbitais a impactos reais na sociedade através de uma solução simples, funcional e alinhada aos objetivos da Global Solution 2026.1.
