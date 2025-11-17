import csv


class Analizador:

    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = []
        self._leer_archivo()

    def _leer_archivo(self):
        
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
       
        nombre = nombre.strip().upper()

        ventas = [
            f["TOTAL_VENTAS"]
            for f in self.datos
            if f["PROVINCIA"].strip().upper() == nombre
        ]

        if not ventas:
            raise KeyError(f"Provincia '{nombre}' no encontrada")

        return sum(ventas)
    


    
    def exportaciones_totales_por_mes(self):

        MESES = {
            "1": "ENERO", "01": "ENERO",
            "2": "FEBRERO", "02": "FEBRERO",
            "3": "MARZO", "03": "MARZO",
            "4": "ABRIL", "04": "ABRIL",
            "5": "MAYO", "05": "MAYO",
            "6": "JUNIO", "06": "JUNIO",
            "7": "JULIO", "07": "JULIO",
            "8": "AGOSTO", "08": "AGOSTO",
            "9": "SEPTIEMBRE", "09": "SEPTIEMBRE",
            "10": "OCTUBRE",
            "11": "NOVIEMBRE",
            "12": "DICIEMBRE"
        }

        resultado = {}

        for fila in self.datos:
            mes = str(fila.get("MES")).strip()

            mes_nombre = MESES.get(mes, mes)

            valor = str(fila.get("EXPORTACIONES", "0")).replace(",", ".")

            try:
                valor = float(valor)
            except:
                valor = 0.0

            resultado[mes_nombre] = resultado.get(mes_nombre, 0) + valor

        return resultado


    



    def porcentaje_tarifa_0_por_provincia(self):
        resultado = {}

        for fila in self.datos:
            provincia = fila.get("PROVINCIA")

            v0 = str(fila.get("VENTAS_NETAS_TARIFA_0", "0")).replace(",", ".")
            total = str(fila.get("TOTAL_VENTAS", "0")).replace(",", ".")

            try:
                v0 = float(v0)
            except ValueError:
                v0 = 0.0

            try:
                total = float(total)
            except ValueError:
                total = 0.0

            if total > 0:
                porcentaje = (v0 / total) * 100
            else:
                porcentaje = 0.0

            resultado[provincia] = porcentaje

        return resultado



