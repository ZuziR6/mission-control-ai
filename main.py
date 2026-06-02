from src.telemetria import coletar
from src.alertas import avaliar

def main():

    dados = coletar()

    print("\n===== ENVIROSAT GUARDIAN =====\n")

    print("Telemetria Atual:")
    print(dados)

    print("\nAlertas:")

    for alerta in avaliar(dados):
        print("-", alerta)

if __name__ == "__main__":
    main()
