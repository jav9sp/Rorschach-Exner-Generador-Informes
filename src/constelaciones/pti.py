from utils.unir_interpretaciones import unir_interpretaciones

numeros = {
    1: "un",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
}


def evaluar_pti(variables):
    """
    Evalúa la constelación PTI (trastornos de percepción-pensamiento).
    """
    condiciones = 0
    interpretaciones = []
    texto = ""

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # 1. XA% < 0.70 y WDA% < 0.75
    if variables.get("XA%", 1) < 0.70 and variables.get("WDA%", 1) < 0.75:
        condiciones += 1
        interpretaciones.append("bajo nivel de convencionalidad general")

    # 2. X-% > 0.29
    if variables.get("X-%", 0) > 0.29:
        condiciones += 1
        interpretaciones.append(
            "prevalencia de distorsiones en la interpretación de la realidad")

    # 3. Nvl-2 > 2 y FAB2 > 0
    if variables.get("Nvl-2", 0) > 2 and variables.get("FAB2", 0) > 0:
        condiciones += 1
        interpretaciones.append(
            "interpretaciones bizarras de la realidad y [FAB2]")

    # 4. (R < 17 y SumPon6 > 12) o (R > 16 y SumPon6 > 17)
    r = variables.get("R", 0)
    sumpon6 = variables.get("SumPon6", 0)
    if (r < 17 and sumpon6 > 12) or (r > 16 and sumpon6 > 17):
        condiciones += 1
        interpretaciones.append(
            "marcada presencia de interferencias en los procesos de pensamiento")

    # 5. M- > 1 o X-% > 0.40
    if variables.get("M-", 0) > 1 or variables.get("X-%", 0) > 0.40:
        condiciones += 1
        interpretaciones.append(
            "desorientación en el pensamiento deliberado")

    if condiciones > 0:
        texto = f"Respecto al índice de trastornos de la percepción y pensamiento, se observa {numeros[condiciones]} indicadores presentes, incluyendo {unir_interpretaciones(interpretaciones)}, lo que indica [INDICAR GRADO] rasgos psicóticos."

    return {"PTI": condiciones,
            "PTI TXT": texto}
