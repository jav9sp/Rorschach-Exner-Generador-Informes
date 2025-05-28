def evaluar_hvi(variables):
    """
    Evalúa la constelación HVI (índice de hipervigilancia).
    Se marca POSITIVO si se cumple la condición 1 y al menos 4 del resto.
    """

    resultado = "Negativo"

    # Condición 1 obligatoria
    sum_ft_tf_t = variables.get(
        "FT", 0) + variables.get("TF", 0) + variables.get("T", 0)
    if sum_ft_tf_t != 0:
        return {"HVI": "Negativo"}

    condiciones = 0
    if variables.get("Zf", 0) > 12:
        condiciones += 1
    if variables.get("Zd", 0) > 3.5:
        condiciones += 1
    if variables.get("S", 0) > 3:
        condiciones += 1
    if variables.get("TodoH", 0) > 6:
        condiciones += 1
    if variables.get("(H)", 0) + variables.get("(Hd)", 0) + variables.get("(Ad)", 0) > 3:
        condiciones += 1
    if variables.get("H", 0) + variables.get("A", 0) > variables.get("Hd", 0) + variables.get("Ad", 0) and variables.get("H", 0) + variables.get("A", 0) < 4:
        condiciones += 1
    if variables.get("Cg", 0) > 3:
        condiciones += 1

    if condiciones >= 4:
        resultado = "Positivo"

    return {
        "HVI": resultado,
    }
