import json
import os


def clasificar_indice_egoc(egoc_valor, edad):
    """Clasifica el índice de egocentrismo según edad hasta los 16 años."""
    if edad > 16:
        return "Usar tablas por tipo vivencial"

    ruta = os.path.join("data", "egocentrismo_ajustes.json")
    with open(ruta, encoding="utf-8") as f:
        ajustes = json.load(f)

    if str(edad) not in ajustes:
        return "Edad fuera de rango"

    min_val, max_val = ajustes[str(edad)]
    if egoc_valor < min_val:
        return "Bajo (Significativo)"
    elif egoc_valor > max_val:
        return "Alto (Significativo)"
    return "Dentro del rango"
