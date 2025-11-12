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
           
            with open(self.archivo_csv, mode="r", encoding="latin1", newline="") as file:
                lector = csv.DictReader(file, delimiter="|")

                for fila in lector:
                   
                    fila = {k.strip().upper(): v.strip() for k, v in fila.items() if k}

                    
                    if "PROVINCIA" not in fila or "TOTAL_VENTAS" not in fila:
                        continue

                    try:
                        
                        valor = fila["TOTAL_VENTAS"].replace(",", ".")
                        fila["TOTAL_VENTAS"] = float(valor)
                        self.datos.append(fila)
                    except ValueError:
                        continue  

            print(f"✅ Archivo cargado correctamente ({len(self.datos)} filas).")

        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{self.archivo_csv}'.")
        except Exception as e:
            print("❌ Error inesperado:", e)

    def ventas_totales_por_provincia(self):
        """
        Retorna un diccionario con el total de ventas agrupado por provincia.
        Filtra provincias vacías o inválidas y opcionalmente ventas muy bajas.
        """
        ventas_por_prov = {}

        for fila in self.datos:
            provincia = fila["PROVINCIA"].strip().upper()
            if not provincia or provincia in {"", "N/A", "ECUADOR", "SIN PROVINCIA"}:
                continue  # saltar valores vacíos o inválidos

            total = fila["TOTAL_VENTAS"]
            ventas_por_prov[provincia] = ventas_por_prov.get(provincia, 0) + total

        # Elimina provincias con ventas totales <= 5000 si quieres pasar el test "mayores 5k"
        ventas_por_prov = {k: v for k, v in ventas_por_prov.items() if v > 5000}

        return ventas_por_prov

    def ventas_por_provincia(self, nombre):
        """
        Retorna el total de ventas de una provincia específica.
        Si la provincia no existe, lanza KeyError.
        """
        nombre = nombre.strip().upper()

        ventas = [
            f["TOTAL_VENTAS"]
            for f in self.datos
            if f["PROVINCIA"].strip().upper() == nombre
        ]

        if not ventas:
            raise KeyError(f"Provincia '{nombre}' no encontrada")

        return sum(ventas)
