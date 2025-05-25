def interpretar_control_estres(variables, estados_simples):
    """
    Evalúa el control y tolerancia al estrés: capacidad de manejar demandas internas y externas, equilibrio emocional, y recursos disponibles.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: AdjD y CDI
    adj_d = variables.get("AdjD", None)
    cdi = variables.get("CDI", 0)
    edad = variables.get("Edad", None)

    adj_d_txt = ""
    if adj_d == 0:
        adj_d_txt = f"{persona.capitalize()} cuenta con una adecuada capacidad para controlar y dirigir sus conductas ante las tensiones de la vida cotidiana, por lo que sus controles solo fallarían ante situaciones de estrés intenso, prolongado o inesperado."
    if adj_d > 0:
        pass
    if adj_d < 0:
        pass

    cdi_txt = ""
    if cdi > 3:
        cdi_txt = "Dado que cuenta con un índice de inhabilidad social positivo, su capacidad de control se ve muy disminuida en la mayoría de las situaciones socioafectivas, dando paso a conductas similares a las que tendría en situaciones de sobrecarga, por lo que corre un mayor riesgo de desorganización ante situaciones externas complejas."

    interpretaciones.append(adj_d_txt)
    interpretaciones.append(cdi_txt)

    # Paso 2: EA
    ea = estados_simples.get("EA", None)
    ea_txt = ""
    if ea == "muy alto":
        ea_txt = ""
    if ea == "alto":
        ea_txt = ""
    if ea == "normal":
        ea_txt = ""
    if ea == "bajo":
        ea_txt = ""
    if ea == "muy bajo":
        ea_txt = f"En cuanto a sus recursos disponibles, estos se encuentran muy por debajo de lo esperado, por lo que, independientemente del nivel de tensión interna que {persona} registra actualmente, implica un estado de vulnerabilidad crónica ante situaciones de estrés, por lo que requiere de un ambiente controlado y previsible para funcionar adaptativamente."

    # ? Incluir verificación de que ambos lados de la EB sean mayores a cero

    sum_pon_c = variables.get("SumPonC", 0)
    tot_m = variables.get("M", 0)

    if tot_m == 0 and sum_pon_c > 3:
        # Abrumado por el afecto
        pass

    if tot_m > 3 and sum_pon_c == 0:
        # Mucha energía en evitar el intercambio
        pass

    interpretaciones.append(ea_txt)

    # Paso 3: EB y Lambda
    lambda_ = estados_simples.get("Lambda", None)
    tipo_vivencial = variables.get("Tipo Vivencial", "Indefinido")
    if lambda_ == "muy alto":
        pass
    if lambda_ == "alto":
        pass
    if lambda_ == "normal":
        pass
    if lambda_ == "bajo":
        pass
    if lambda_ == "muy bajo":
        pass

    if tipo_vivencial == "Extroversivo":
        pass
    if tipo_vivencial == "Introversivo":
        pass
    if tipo_vivencial == "Ambigual":
        pass
    if tipo_vivencial == "Indefinido":
        pass

    # Paso 4: es y Adjes
    valor_es = variables.get("es", None)
    nivel_es = estados_simples.get("es", "Indefinido")
    nivel_adj_es = estados_simples.get("Adjes", None)

    if valor_es == 0:
        # Malo porque no tiene sensibilidad a sus propias necesidades
        pass

    if nivel_es in ["alto", "muy alto"]:
        # Malo porque desorganización es latente
        pass

    # ? Si está elevada es se debe verificar qué lado
    # ? Si EA es elevada y es también hay que verificar eficacia

    # Paso 5: eb
    eb_izq = variables.get("FM+m", 0)
    eb_der = variables.get("SumSH", 0)
    eb = variables.get("eb", None)

    return interpretaciones
