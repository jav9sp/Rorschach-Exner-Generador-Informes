def interpretar_estres_situacional(variables, estados_simples):
    """
    Evalúa la presencia de estrés situacional agudo: indicadores de sobrecarga emocional, sensibilidad actual, y funcionamiento transitorio.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: PuntD relacionada con es y Adjes
    punt_d = variables.get("PuntD", None)
    adj_d = variables.get("AdjD", None)

    if punt_d != adj_d:
        interpretaciones.append("[DIFERENCIA PuntD Y AdjD PRESENTE]")
    else:
        interpretaciones.append(
            f"No se observan indicadores de aumento en el registro de tensión interna en {persona} por factores situacionales.")

    # Paso 2: Diferencia entre la puntuación D y AdjD
    # ? Aumento de tensión afecta en ideación periférica o afectos
    if punt_d < adj_d:
        interpretaciones.append(
            "[CONTROL ACTUAL < CONTROL HABITUAL - REVISAR m E Y]")

    if punt_d < 0 and adj_d < 0:
        interpretaciones.append("[SOBRECARGA HABITUAL, ALTA IMPULSIVIDAD]")

    # Paso 3: m e Y
    sum_m_ina = variables.get("m", 0)
    sum_y = variables.get("SumY", 0)

    if sum_m_ina > 1:
        interpretaciones.append("[AUMENTO MALESTAR IDEACIONAL]")

    if sum_y > 1:
        interpretaciones.append("[AUMENTO MALESTAR EMOCIONAL]")

    if sum_m_ina > 0 or sum_y > 0:
        if sum_m_ina >= sum_y * 3:
            interpretaciones.append(
                "[SOBRECARGA IDEACIONAL - PÉRDIDA CONTROL INMINENTE]")

        if sum_y >= sum_m_ina * 3:
            interpretaciones.append(
                "[SOBRECARGA EMOCIONAL - DESBORDE EMOCIONAL E INDEFENSIÓN]")

    # Paso 4: T, V, Ego, en relación con el historial
    sum_t = variables.get("SumT", 0)
    sum_v = variables.get("SumV", 0)
    ego_estado = estados_simples.get("Ego", "Indefinido")
    sum_reflejos = variables.get("Fr+rF", 0)

    if sum_t > 1:
        interpretaciones.append(
            "[VERIFICAR AUMENTO DE T - ¿PÉRDIDA RECIENTE? ¿DUELO NO ELABORADO?]")

    if sum_v > 0:
        interpretaciones.append("[VERIFICAR AUMENTO DE V]")

    if ego_estado in ["alto", "muy alto"] and sum_reflejos == 0 and sum_t > 1 and sum_v > 0:
        interpretaciones.append(
            "[RECALCULAR AdjD POR AUMENTO DE T O V - INCORPORAR HISTORIA CLÍNICA]")

    # Paso 5: PuntD en relación con C Pura, MQ- y MQsin
    c_pura = variables.get("C", 0)
    mq_sin = variables.get("MQsin", 0)
    mq_menos = variables.get("MQ-", 0)

    if punt_d >= 0:
        interpretaciones.append("[ADECUADO CONTROL GENERAL]")
    else:
        interpretaciones.append("[BAJO CONTROL GENERAL]")

    if c_pura > 0:
        interpretaciones.append("[C PURA PRESENTE]")

    if mq_sin > 0:
        interpretaciones.append("[MQsin PRESENTE]")

    if mq_menos > 0:
        interpretaciones.append("[MQ- PRESENTE]")

    # Paso 6: Respuestas complejas
    # ? Evaluar % de Compljs con m e Y
    compljs_sit = variables.get("CompljsSit/R", 0)

    if compljs_sit >= 0.5:
        interpretaciones.append("[ALTA COMPLEJIDAD INTELECTUAL SITUACIONAL")

    # Paso 7: CompljsColSH y CompljsSH
    compljs_col_y = variables.get("CompljsColY", 0)
    compljs_sh_y = variables.get("CompljsSHY", 0)

    if compljs_col_y:
        interpretaciones.append("[PRESENTE CompljsColY]")

    if compljs_sh_y:
        interpretaciones.append("[PRESENTE CompljsSHY]")

    return interpretaciones
