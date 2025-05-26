import json
import os

# Normalización de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "..", "data", "dscore_conversion.json")
json_path = os.path.normpath(json_path)

# Cargar tabla de conversión desde JSON externo
with open(json_path, "r", encoding="utf-8") as f:
    D_SCORE_CONVERSION = json.load(f)


def calcular_dscore(ea_menos_es):
    """Devuelve el Dscore basado en la tabla de conversión externa."""
    clave = str(round(ea_menos_es, 1))
    return D_SCORE_CONVERSION.get(clave, 0)


def calcular_adj_es(variables):
    """Calcula Adj es restando m y SumY (ajustando 1 unidad si están presentes)."""
    m = variables.get("m", 0)
    if m > 1:
        m = 1

    y = variables.get("SumY", 0)
    if y > 1:
        y = 1
    es = variables.get("es", 0)

    return es - m - y


def calcular_adj_d(ea, adj_es):
    """Calcula AdjD como EA - Adj es y lo convierte a Dscore."""
    ea_menos_adj_es = round(ea - adj_es, 2)
    return calcular_dscore(ea_menos_adj_es)
