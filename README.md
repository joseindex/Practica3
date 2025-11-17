#  Práctica 3 – Validación del software a través de pruebas automatizadas

Esta práctica consiste en procesar información de un archivo CSV utilizando Python.  
El proyecto implementa funciones para limpiar, validar y analizar los datos, además de incluir pruebas automáticas con `unittest` y medición de cobertura con `coverage`.



## 📂 Estructura del Proyecto

Practica3/
│── src/
│ └── procesador.py # Lógica principal del procesamiento
│── tests/
│ └── test_procesador.py # Pruebas unitarias
│── data/
│ └── SRI_2023.csv # Archivo de datos utilizados
│── README.md # Documentación del proyecto


## 🧠 Funcionalidades Principales

El módulo `procesador.py` realiza operaciones como:

- ✔️ Cargar y validar registros del archivo CSV  
- ✔️ Calcular totales globales  
- ✔️ Obtener ventas por provincia  
- ✔️ Identificar la empresa con mayor recaudación  
- ✔️ Generar estructuras limpias para análisis posterior

  
## 🧪 Ejecución de Pruebas Unitarias

python -m unittest tests/test_procesador.py -v

## 🧪 Ver el reporte en la terminal
coverage report -m


Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/procesador.py            73     14    81%    ...
tests/test_procesador.py     37      0   100%
--------------------------------------------------------
TOTAL                        110    14    87%

## 🧪 Requisitos

Python 3.10 o superior

Instalar coverage 



