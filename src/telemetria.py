"""
Geração de telemetria simulada - Trilha EnviroSat
"""

import random


def coletar():
    """
    Retorna um snapshot da telemetria atual.
    """

    return {
        "sensor_termico": round(random.uniform(20, 120), 2),
        "sensor_optico": round(random.uniform(70, 100), 2),
        "buffer_imagens": random.randint(0, 100),
        "precisao_geolocalizacao": round(random.uniform(0.5, 10.0), 2),
        "energia_disponivel": round(random.uniform(10, 100), 2)
    }
