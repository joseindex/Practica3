from src.procesador import (
    Analizador,
)  # Importa la clase Analizador desde el archivo procesador.py


def main():

    # Ruta del archivo CSV con los datos del SRI

    archivo = "datos/sri_ventas_2024.csv"

    # Crea un objeto Analizador para trabajar con ese archivo

    analizador = Analizador(archivo)

    # Muestra las ventas totales por provincia

    print("Ventas totales por provincia:")

    resumen = analizador.ventas_totales_por_provincia()

    # Recorre el diccionario y muestra cada provincia con su total

    for prov, total in resumen.items():

        print(f"\t{prov}: ${total:.2f}")

    # Pide al usuario el nombre de una provincia

    print("\nCompras para una provincia")

    provincia = input("\tIngrese el nombre de una provincia: ")

    # Calcula las ventas de esa provincia y las muestra

    ventas = analizador.ventas_por_provincia(provincia)

    print(f"\tVentas de {provincia}: ${ventas:,.2f}")


# Esto se ejecuta solo si corres este archivo directamente (python main.py)


if __name__ == "__main__":

    main()
