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


def calcular_zscore(columna_lam, columna_z):
    """
    Devuelve un diccionario con Zf, Zsum, Zest (esperado), Zd y estilo cognitivo.
    """

    puntajes_por_lamina_y_codigo = {
        'I': {'zw': 1.0, 'za': 4.0, 'zd': 6.0, 'zs': 3.5},
        'II': {'zw': 4.5, 'za': 3.0, 'zd': 5.5, 'zs': 4.5},
        'III': {'zw': 5.5, 'za': 3.0, 'zd': 4.0, 'zs': 4.5},
        'IV': {'zw': 2.0, 'za': 4.0, 'zd': 3.5, 'zs': 5.0},
        'V': {'zw': 1.0, 'za': 2.5, 'zd': 5.0, 'zs': 4.0},
        'VI': {'zw': 2.5, 'za': 2.5, 'zd': 6.0, 'zs': 6.5},
        'VII': {'zw': 2.5, 'za': 1.0, 'zd': 3.0, 'zs': 4.0},
        'VIII': {'zw': 4.5, 'za': 3.0, 'zd': 3.0, 'zs': 4.0},
        'IX': {'zw': 5.5, 'za': 2.5, 'zd': 4.5, 'zs': 5.0},
        'X': {'zw': 5.5, 'za': 4.0, 'zd': 4.5, 'zs': 6.0}
    }

    zvalores = []

    for lamina, codigo in zip(columna_lam, columna_z):
        z = puntajes_por_lamina_y_codigo.get(
            lamina.upper(), {}).get(str(codigo).lower())
        if z is not None:
            zvalores.append(z)

    zf = len(zvalores)
    zsum = sum(zvalores)
    zest = zest_data.get(zf, None)
    zd = zsum - zest if zest is not None else 0

    if zest is None:
        estilo_cognitivo = "No interpretable"
    elif zd > 3.5:
        estilo_cognitivo = "Hiperincorporador"
    elif zd < -3.5:
        estilo_cognitivo = "Hipoincorporador"
    else:
        estilo_cognitivo = "Normal"

    return {
        "Zf": zf,
        "Zsum": round(zsum, 2),
        "Zest": zest,
        "Zd": round(zd, 2) if zest is not None else None,
        "Estilo Cognitivo": estilo_cognitivo
    }
