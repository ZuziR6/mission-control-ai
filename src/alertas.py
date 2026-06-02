"""
Regras de alerta da missão EnviroSat.
"""


def avaliar(dados):
    """
    Avalia a telemetria e retorna os alertas encontrados.
    """

    alertas = []

    # Energia crítica
    if dados["energia"] < 20:
        alertas.append("🔴 CRÍTICO: Energia abaixo de 20%")
        alertas.append("⚙️ AÇÃO AUTOMÁTICA: Modo economia de energia ativado")

    # Temperatura crítica
    if dados["temperatura"] > 75:
        alertas.append("🔴 CRÍTICO: Temperatura acima de 75°C")
        alertas.append("⚙️ AÇÃO AUTOMÁTICA: Sensor secundário desligado")

    # Buffer elevado
    if dados["buffer_imagens"] > 85:
        alertas.append("🟠 ALERTA: Buffer de imagens acima de 85%")

    # Problema de geolocalização
    if dados["precisao_gps"] > 5:
        alertas.append("🟠 ALERTA: Precisão GPS acima de 5 metros")

    # Sensor térmico degradado
    if dados["sensor_termico"] < 60:
        alertas.append("🟡 ATENÇÃO: Eficiência do sensor térmico abaixo de 60%")

    if not alertas:
        alertas.append("🟢 Nenhum alerta detectado")

    return alertas
