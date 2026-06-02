"""
Geração de telemetria simulada - Trilha EnviroSat
"""

import random


def coletar():
    """
    Retorna um snapshot da telemetria atual.
    """

    return {
        "energia": round(random.uniform(10, 100), 2),
        "temperatura": round(random.uniform(20, 100), 2),
        "buffer_imagens": random.randint(0, 100),
        "precisao_gps": round(random.uniform(0.5, 10.0), 2),
        "sensor_termico": round(random.uniform(40, 100), 2)
    }
