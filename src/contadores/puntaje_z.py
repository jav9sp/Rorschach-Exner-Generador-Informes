import json
import os

# Normalización de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "..", "data", "zscore_conversion.json")
json_path = os.path.normpath(json_path)

# Cargar tabla de conversión desde archivo JSON
with open(json_path, encoding="utf-8") as f:
    zest_data = json.load(f)
    zest_data = {
        int(k): float(v) if isinstance(v, (int, float)) else None
        for k, v in zest_data.items()
    }


def calcular_zscores(columna_z):
    """
    Devuelve un diccionario con Zf, Zsum, Zest (esperado), Zd y estilo cognitivo.
    """
    columna_z = columna_z.dropna()
    zf = len(columna_z)
    zsum = columna_z.sum()
    zest = zest_data.get(zf, None)
    zd = zsum - zest if zest is not None else 0

    if zd is None:
        estilo_cognitivo = "No interpretable"
    elif zd > 3.5:
        estilo_cognitivo = "Hiperincorporador"
    elif zd < -3.5:
        estilo_cognitivo = "Hipoincorporador"
    else:
        estilo_cognitivo = "Normal"

    return {
        "Zf": zf,
        "Zsum": float(zsum),
        "Zest": zest,
        "Zd": round(zd, 2) if zd is not None else None,
        "Estilo Cognitivo": estilo_cognitivo
    }
