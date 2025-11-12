import csv


class Analizador:

    def __init__(self, archivo_csv):

        self.archivo_csv = archivo_csv

        self.datos = []

        self._leer_archivo()

    def _leer_archivo(self):
        """


        Lee el archivo CSV separado por '|' y guarda su contenido en una lista de diccionarios.


        """

        try:

            # Abrimos con encoding latin1 (para AÑOS, Ñ, etc.) y newline='' (para saltos de línea raros)

            with open(
                self.archivo_csv, mode="r", encoding="latin1", newline=""
            ) as file:

                lector = csv.DictReader(file, delimiter="|")

                for fila in lector:

                    # Aseguramos que las claves estén en mayúsculas y sin espacios

                    fila = {k.strip().upper(): v.strip() for k, v in fila.items() if k}

                    # Si la fila no tiene TOTAL_VENTAS o PROVINCIA, la saltamos

                    if "PROVINCIA" not in fila or "TOTAL_VENTAS" not in fila:

                        continue

                    try:

                        fila["TOTAL_VENTAS"] = float(fila["TOTAL_VENTAS"])

                        self.datos.append(fila)

                    except ValueError:

                        continue  # si hay un valor no numérico, lo ignoramos

            print(f"✅ Archivo cargado correctamente ({len(self.datos)} filas).")

        except FileNotFoundError:

            print(f"❌ Error: No se encontró el archivo '{self.archivo_csv}'.")

        except Exception as e:

            print("❌ Error inesperado:", e)

    def ventas_totales_por_provincia(self):
        """


        Retorna un diccionario con el total de ventas agrupado por provincia.


        """

        ventas_por_prov = {}

        for fila in self.datos:

            provincia = fila["PROVINCIA"].strip().upper()

            total = fila["TOTAL_VENTAS"]

            ventas_por_prov[provincia] = ventas_por_prov.get(provincia, 0) + total

        # print("🔍 Provincias encontradas:")

        # for prov, total in ventas_por_prov.items():

        # print(f"{prov}: {total}")

        return ventas_por_prov

    def ventas_por_provincia(self, nombre):
        """


        Retorna el total de ventas de una provincia específica.


        """

        nombre = nombre.strip().upper()

        total = sum(
            f["TOTAL_VENTAS"]
            for f in self.datos
            if f["PROVINCIA"].strip().upper() == nombre
        )

        return total
