"""
Geração de telemetria simulada da missão EnviroSat.
"""

import random


def coletar():
    """
    Retorna um conjunto de dados simulados da missão.
    """

    return {
        "energia": random.randint(10, 100),                 # %
        "temperatura": random.randint(20, 90),             # °C
        "sensor_termico": random.randint(50, 100),         # %
        "buffer_imagens": random.randint(0, 100),          # %
        "precisao_gps": round(random.uniform(0.5, 8.0), 2) # metros
    }
