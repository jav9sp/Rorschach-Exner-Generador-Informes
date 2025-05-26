# TODO: Generar la interpretación
# Me gusta la estructura de reglas, quizá podría agregarla a todas

def evaluar_obs(variables):
    """
    Evalúa la constelación OBS (estilo obsesivo).
    Se marca POSITIVO si se cumple una o más de las condiciones finales.
    """
    # Reglas básicas (1 a 5)
    reglas = [
        variables.get("Dd", 0) > 3,
        variables.get("Zf", 0) > 12,
        variables.get("Zd", 0) > 3.0,
        variables.get("Populares", 0) > 7,
        variables.get("FQ+", 0) > 1
    ]

    total_reglas = sum(reglas)

    resultado = "Negativo"
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    texto = f"{persona}"

    # Condiciones de activación
    if all(reglas):
        resultado = "Positivo"
    if total_reglas >= 2 and variables.get("FQ+", 0) > 3:
        resultado = "Positivo"
    if total_reglas >= 3 and variables.get("X+%", 0) > 0.89:
        resultado = "Positivo"
    if variables.get("DQ+", 0) > 3 and variables.get("X+%", 0) > 0.89:
        resultado = "Positivo"

    return {
        "OBS": resultado,
        "OBS TXT": texto
    }
