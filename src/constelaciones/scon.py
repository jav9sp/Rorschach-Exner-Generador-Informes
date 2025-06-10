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


def evaluar_scon(variables, edad):
    """
    Evalúa la constelación S-CON (Suicidio) según criterios definidos.
    Devuelve un párrafo con interpretación clínica.
    """

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    if edad < 15:
        return "No aplica por edad"

    condiciones = 0
    interpretaciones = []
    texto = ""

    if variables.get("SumV", 0) + variables.get("FD", 0) > 2:
        condiciones += 1
        interpretaciones.append(
            "una alta tendencia a la introspección negativa")

    if variables.get("CompljsColSH", 0) > 0:
        condiciones += 1
        interpretaciones.append(
            "una fuerte presencia de elementos disfóricos en su elaboración cognitiva")

    egoc = variables.get("Ego", 0)
    if egoc < 0.31:
        condiciones += 1
        interpretaciones.append("un bajo índice de egocentrismo")
    if egoc > 0.44:
        condiciones += 1
        interpretaciones.append("un alto índice de egocentrismo")

    if variables.get("MOR", 0) > 3:
        condiciones += 1
        interpretaciones.append(
            "una alta presencia de negativismo en la ideación")

    zd = variables.get("Zd", 0)
    if zd > 3.5:
        condiciones += 1
        interpretaciones.append(
            "dificultad para tomar decisiones debido a exceso de análisis")
    if zd < -3.5:
        condiciones += 1
        interpretaciones.append(
            "impulsividad en la toma de decisiones al resolver problemas")

    es = variables.get("es", 0)
    ea = variables.get("EA", 0)
    if es > ea:
        condiciones += 1
        interpretaciones.append(
            "un aumento en el registro de tensión interna y falta de recursos para manejarla")

    if variables.get("CF", 0) + variables.get("C", 0) > variables.get("FC", 0):
        condiciones += 1
        interpretaciones.append(
            "falta de modulación en la descarga de afectos")

    if variables.get("X+%", 1) < 0.70:
        condiciones += 1
        interpretaciones.append("un bajo ajuste perceptivo general")

    if variables.get("S", 0) > 3:
        condiciones += 1
        interpretaciones.append(
            "un estilo confrontacional que puede aumentar el conflicto con el entorno")

    p = variables.get("Populares", 0)
    if p < 3:
        condiciones += 1
        interpretaciones.append("una baja capacidad de ajuste a la norma")
    elif p > 8:
        condiciones += 1
        interpretaciones.append(
            "una excesiva tendencia a ajustarse a la norma")

    if variables.get("H", 0) < 2:
        condiciones += 1
        interpretaciones.append("un bajo interés en el componente humano")

    if variables.get("R", 0) < 17:
        condiciones += 1
        interpretaciones.append("un bajo nivel de productividad")

    # Generar párrafo si es positivo
    if condiciones <= 8:
        texto = (
            "La constelación de suicidio marca negativo, lo que permite descartar la presencia de conductas autolesivas en el corto mediano plazo. "
            f"Pese a ello, se observa {numeros[condiciones]} indicadores presentes, incluyendo {unir_interpretaciones(interpretaciones)}."
        )

    if condiciones >= 8:
        texto = f"La constelación de suicidio marca positivo, por lo que existe un peligro inminente de que {persona} incurra en conductas autolesivas en el corto mediano plazo, lo cual requiere un abordaje urgente."

    resultado = "Positivo" if condiciones >= 8 else "Negativo"

    return {"SCON": resultado,
            "SCON TXT": texto}
