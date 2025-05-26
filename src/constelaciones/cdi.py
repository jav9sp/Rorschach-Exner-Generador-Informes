
def evaluar_cdi(variables):
    """
    Evalúa la constelación CDI (inhabilidad social).
    Requiere 4 de 5 condiciones.
    """
    condiciones = 0
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    texto = ""

    if variables.get("EA", 0) < 6 or variables.get("AdjD", 0) < 0:
        condiciones += 1
    if variables.get("COP", 0) < 2 and variables.get("AG", 0) < 2:
        condiciones += 1
    if variables.get("SumPonC", 10) < 2.5 or variables.get("Afr", 1) < 0.46:
        condiciones += 1
    if variables.get("p", 0) > variables.get("a", 0) + 1 or variables.get("H", 0) < 2:
        condiciones += 1

    extra = 0
    if variables.get("SumT", 0) > 1:
        extra += 1
    if variables.get("Aisl/R", 0) > 0.24:
        extra += 1
    if variables.get("Fd", 0) > 0:
        extra += 1

    if (condiciones >= 4 or (condiciones == 3 and extra > 0)):
        texto = f"Se observa que {persona} cuenta con un índice de inhabilidad social positivo, lo que implica una serie de dificultades para relacionarse de manera adaptativa en la esfera social, llevándole a acumular tensión al estar en contacto con los demás."

    return {
        "CDI": condiciones,
        "CDI TXT": texto
    }
