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


def evaluar_depi(variables):
    """
    Evalúa la constelación DEPI (depresión).
    Se marca positiva si se cumplen al menos 5 condiciones.
    """
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    condiciones = 0
    interpretaciones = []
    factor_cognitivo = 0
    factor_afectivo = 0
    factor_social = 0
    texto = ""

    if variables.get("SumV", 0) > 0 or variables.get("FD", 0) > 2:
        condiciones += 1
        interpretaciones.append(
            "marcada tendencia a la introspección negativa")

        if variables.get("FD", 0) > 2:
            factor_cognitivo += 1
        if variables.get("SumV", 0) > 0:
            factor_afectivo += 1

    if variables.get("CompljsColSH", 0) > 0:
        condiciones += 1
        factor_afectivo += 1
        interpretaciones.append(
            "fuerte presencia de elementos disfóricos en su elaboración cognitiva")
    elif variables.get("S", 0) > 2:
        condiciones += 1
        factor_afectivo += 1
        interpretaciones.append("marcada tendencia oposicionista")

    egoc = variables.get("Ego", 0)
    if egoc < 0.33:
        condiciones += 1
        factor_cognitivo += 1
        interpretaciones.append("bajo índice de egocentrismo")
    if egoc > 0.44 and variables.get("Fr+rF", 0) == 0:
        condiciones += 1
        factor_cognitivo += 1
        interpretaciones.append("alto índice de egocentrismo (sin narcisismo)")

    if variables.get("Afr", 1) < 0.46:
        condiciones += 1
        factor_afectivo += 1
        interpretaciones.append(
            "baja responsividad cognitiva a la estimulación emocional")
    elif variables.get("Compljs", 10) < 4:
        condiciones += 1
        factor_cognitivo += 1
        interpretaciones.append("baja complejidad intelectual")

    if variables.get("SumSH", 0) > variables.get("FM+m", 0):
        condiciones += 1
        factor_afectivo += 1
        interpretaciones.append(
            "aumento de tensión interna por el registro de elementos disfóricos")
    elif variables.get("SumC'", 0) > 2:
        condiciones += 1
        factor_afectivo += 1
        interpretaciones.append("aumento la represión de elementos disfóricos")

    if variables.get("MOR", 0) > 2:
        condiciones += 1
        factor_cognitivo += 1
        interpretaciones.append(
            "marcada presencia de negativismo en la ideación")
    elif variables.get("Intelec", 0) > 3:
        condiciones += 1
        factor_cognitivo += 1
        interpretaciones.append(
            "marcada tendencia a usar la intelectualización")

    if variables.get("COP", 0) < 2:
        condiciones += 1
        factor_social += 1
        interpretaciones.append(
            "falta de atribuciones positivas a la interacción con los demás")
    elif variables.get("Aisl/R", 0) > 0.24:
        condiciones += 1
        factor_social += 1
        interpretaciones.append("una tendencia a asilarse socialmente")

    if condiciones < 5:
        texto = f"La constelación de depresión marca negativo, lo que permite descartar la presencia de depresión actual. Pese a ello, {persona} muestra {numeros[condiciones]} indicadores, incluyendo {unir_interpretaciones(interpretaciones)}."

    if condiciones == 5:
        texto = f"Se observa que {persona} cuenta con cinco indicadores de la constelación de depresión que, si bien no afirma que cuente con un diagnóstico de depresión activa, indica que se encuentra vulnerable a caer en estados depresivos o sufrir alteraciones bruscas del estado de ánimo."

    if condiciones > 5:
        texto = generar_depi_positivo(
            persona, factor_cognitivo, factor_afectivo, factor_social)

    return {
        "DEPI": condiciones,
        "DEPI TXT": texto
    }


def generar_depi_positivo(persona, factor_cognitivo, factor_afectivo, factor_social):
    # Determinar las áreas afectadas
    areas_afectadas = []
    if factor_cognitivo > 0:
        areas_afectadas.append("cognitiva")
    if factor_afectivo > 0:
        areas_afectadas.append("afectiva")
    if factor_social > 0:
        areas_afectadas.append("social")

    # Texto de áreas afectadas
    if len(areas_afectadas) == 1:
        areas_txt = f"sobre el área {areas_afectadas[0]}"
    elif len(areas_afectadas) == 2:
        areas_txt = f"sobre las áreas {areas_afectadas[0]} y {areas_afectadas[1]}"
    else:
        areas_txt = f"en las áreas {", ".join(
            areas_afectadas[:-1]) + f" y {areas_afectadas[-1]}"}"

    # Normalización
    norm_cognitivo = factor_cognitivo / 4
    norm_afectivo = factor_afectivo / 4
    norm_social = factor_social / 1

    # Determinar área más afectada y severidad
    max_valor = max(norm_cognitivo, norm_afectivo, norm_social)
    if max_valor == norm_cognitivo:
        principal = "cognitiva"
    elif max_valor == norm_afectivo:
        principal = "afectiva"
    else:
        principal = "social"

    # Clasificación de severidad
    if max_valor <= 0.33:
        severidad = "leve"
    elif max_valor <= 0.66:
        severidad = "moderado"
    else:
        severidad = "mayor"

    return f"La constelación de depresión marca positivo, lo que indica que {persona} se encuentra enfrentando un trastorno afectivo que perturba su estado emocional, teniendo un mayor impacto {areas_txt}, siendo la {principal} la que muestra un deterioro {severidad} en relación con su potencial de funcionamiento."
