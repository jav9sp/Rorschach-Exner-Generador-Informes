def interpretar_control_estres(variables, estados_simples):
    """
    INCOMPLETO
    Evalúa el control y tolerancia al estrés: capacidad de manejar demandas internas y externas, equilibrio emocional, y recursos disponibles.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: AdjD y CDI
    adj_d = variables.get("AdjD", None)
    cdi = variables.get("CDI", 0)
    edad = variables.get("Edad", None)

    # ? Añadir condicional de edad > 15

    if adj_d == 0:
        interpretaciones.append(
            f"{persona.capitalize()} cuenta con una adecuada capacidad para controlar y dirigir sus conductas ante las tensiones de la vida cotidiana, por lo que sus controles solo fallarían ante situaciones de estrés intenso, prolongado o inesperado.")

    if adj_d > 0:
        # ? Se debe evaluar distorsiones de EA, es<2 u EA<6, rasgos patológicos
        interpretaciones.append(f"{persona.capitalize()} cuenta con una capacidad para controlar y dirigir sus conductas ante las tensiones de la vida cotidiana que es mayor a lo esperado, indicando que cuenta con muchos más recursos para manejar los estados de tensión interna y las demandas del entorno.")

    if adj_d < 0:
        # ? Se debe considerar edad < 14, normal en esos casos -1 o -2
        interpretaciones.append(
            f"Se observa que {persona} no cuenta con una adecuada capacidad para controlar y dirigir sus conductas ante las tensiones de la vida cotidiana, por lo que se encuentra actualmente en un estado de sobrecarga, procesando mayor tensión interna de la que es capaz de manejar.")

    if cdi > 3:
        interpretaciones.append("Dado que cuenta con un índice de inhabilidad social positivo, su capacidad de control se ve muy disminuida en la mayoría de las situaciones socioafectivas, dando paso a conductas similares a las que tendría en situaciones de sobrecarga, por lo que corre un mayor riesgo de desorganización ante situaciones externas complejas.")

    # Paso 2: EA
    ea = estados_simples.get("EA", None)
    if ea == "muy alto":
        interpretaciones.append("[PENDIENTE EA MUY ALTO]")

    if ea == "alto":
        interpretaciones.append("[PENDIENTE EA ALTO]")

    if ea == "normal":
        interpretaciones.append("[PENDIENTE EA NORMAL")

    if ea == "bajo":
        interpretaciones.append("[PENDIENTE EA BAJO]")

    if ea == "muy bajo":
        interpretaciones.append(
            f"En cuanto a sus recursos disponibles, estos se encuentran muy por debajo de lo esperado, por lo que, independientemente del nivel de tensión interna que {persona} registra actualmente, implica un estado de vulnerabilidad crónica ante situaciones de estrés, por lo que requiere de un ambiente controlado y previsible para funcionar adaptativamente.")

    # ? Incluir verificación de que ambos lados de la EB sean mayores a cero
    sum_pon_c = variables.get("SumPonC", 0)
    tot_m = variables.get("M", 0)

    if tot_m == 0 and sum_pon_c > 3:
        # Abrumado por el afecto
        interpretaciones.append("[PENDIENTE M=0 Y SumPonC>3]")

    if tot_m > 3 and sum_pon_c == 0:
        # Mucha energía en evitar el intercambio
        interpretaciones.append("[PENDIENTE M>3 Y SumPonC=0]")

    if tot_m > 0 and sum_pon_c == 0:
        # Estilo coartado, sin recursos
        interpretaciones.append("[PENDIENTE M=3 Y SumPonC=0]")

    # Paso 3: EB, Lambda y EBPer
    lambda_estado = estados_simples.get("Lambda", "Indefinido")
    tipo_vivencial = variables.get("Tipo Vivencial", "Indefinido")
    ebper = variables.get("EBPer", 0)

    if lambda_estado in ["alto", "muy alto"]:
        interpretaciones.append(
            "[EVALUAR POSIBLE LADO EB CERO POR L ALTO Y ESTILO EVITATIVO]")

    if tipo_vivencial == "Extroversivo":
        interpretaciones.append(
            f"Dado que {persona} tiene un tipo vivencial {tipo_vivencial}, [COMPLETAR]")

    if tipo_vivencial == "Introversivo":
        interpretaciones.append(
            f"Dado que {persona} tiene un tipo vivencial {tipo_vivencial}, responde principalmente de manera ideacional, demorando la toma de decisiones y manteniendo las emociones al margen mientras soluciona problemas.")

    if tipo_vivencial == "Ambigual":
        interpretaciones.append(
            f"Dado que {persona} tiene un tipo vivencial {tipo_vivencial}, [COMPLETAR]")

    if ebper:
        interpretaciones.append("[PENDIENTE EBPer PRESENTE]")

    # Paso 4: es y Adjes
    valor_es = variables.get("es", None)
    nivel_es = estados_simples.get("es", "Indefinido")
    # nivel_adj_es = estados_simples.get("Adjes", None)

    if valor_es == 0:
        interpretaciones.append("[PENDIENTE es = 0]")

    # ? Si está elevada es se debe verificar qué lado
    # ? Si EA es elevada y es también hay que verificar eficacia
    if nivel_es in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE es ELEVADA]")

    # Paso 5: eb
    # eb_izq = variables.get("FM+m", 0)
    # eb_der = variables.get("SumSH", 0)
    # eb = variables.get("eb", None)

    interpretaciones.append("[PENDIENTE INTEGRAR VALORES eb]")

    return interpretaciones
