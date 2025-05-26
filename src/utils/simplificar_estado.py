
def simplificar_estado(texto):
    if texto == "Dentro del rango":
        return "normal"
    if texto == "Levemente por encima":
        return "alto"
    if texto == "Levemente por debajo":
        return "bajo"
    if texto == "Marcadamente por encima":
        return "muy alto"
    if texto == "Marcadamente por debajo":
        return "muy bajo"
    return "indefinido"
