import json
import os


# Normalización de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "..", "data", "egocentrismo_ajustes.json")
json_path = os.path.normpath(json_path)


def clasificar_indice_egoc(egoc_valor, edad):
    """Clasifica el índice de egocentrismo según edad hasta los 16 años."""
    if edad > 16:
        return "Usar tablas por tipo vivencial"

    with open(json_path, encoding="utf-8") as f:
        ajustes = json.load(f)

    if str(edad) not in ajustes:
        return "Edad fuera de rango"

    min_val, max_val = ajustes[str(edad)]
    if egoc_valor < min_val:
        return "Bajo (Significativo)"
    elif egoc_valor > max_val:
        return "Alto (Significativo)"
    return "Dentro del rango"
