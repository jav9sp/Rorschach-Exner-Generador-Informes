def interpretar_ideacion(variables, estados_simples):
    """
    INCOMPLETO
    Evalúa la ideación: estilo de pensamiento, activación cognitiva, coherencia, flexibilidad y elaboración lógica.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    articulo = "lo" if persona == "el evaluado" else "la"

    # Paso 1: EB Introversivo, Lambda, EBPer
    lambda_bruto = variables.get("Lambda", 0)
    eb = variables.get("Tipo Vivencial", "Indefinido")
    edad = variables.get("Edad")
    if eb == "Introversivo" and edad <= 12:
        interpretaciones.append("[EVALUAR MENOR DE 12 CON EB INTRATENSIVO]")

    if eb == "Introversivo":
        interpretaciones.append(
            F"Dado que {persona} tiene un tipo vivencial Introversivo, prefiere usar la ideación al resolver problemas y se inclina a considerar todas las posibles alternativas antes de tomar una decisión, por lo que no procesa emociones en el proceso y se basa fuertemente en su propia evaluación interna para elaborar juicios.")

    # ? Acá se debe evaluar EA>=4 y R>16. Ver p.119
    if eb == "Introversivo":
        if 7 <= edad < 18 and lambda_bruto > 1.3:
            interpretaciones.append("[PENDIENTE NIÑO EVITATIVO]")

        if edad > 18 and lambda_bruto > 1.2:
            interpretaciones.append("[PENDIENTE ADULTO EVITATIVO]")

    ebper = variables.get("EBPer", 0)
    if ebper != 0:
        interpretaciones.append("[PENDIENTE EBPer POSITIVO]")

    # Paso 2: a:p y Ma:Mp
    a_total = variables.get("a", 0)
    p_total = variables.get("p", 0)
    ma_total = variables.get("Ma", 0)
    mp_total = variables.get("Mp", 0)
    sum_t = variables.get("SumT", 0)
    pop = estados_simples.get("Populares", 0)
    ego = estados_simples.get("Ego", 0)
    cont_fd = variables.get("Fd", 0)
    sum_mov = variables.get("M") + variables.get("FM") + variables.get("m")

    if sum_mov < 4:
        interpretaciones.append(f"{persona.capitalize()} no proporcionó suficiente información respecto su funcionamiento ideativo como para realizar un análisis en profundidad, lo que impide estimar de qué manera utiliza sus recursos ideativos y cómo éstos {articulo} movilizan para interactuar con su entorno.")
    else:
        if p_total > a_total + 1:
            interpretaciones.append(f"{persona.capitalize()} muestra una actitud pasiva en sus procesos de ideación, por lo que tiende a asumir un rol pasivo en sus relaciones interpersonales y a no responsabilizarse por sus propias decisiones. Por este mismo motivo, suele refugiarse en la fantasía para satisfacer sus frustraciones de la vida real.")
        else:
            interpretaciones.append(
                f"{persona.capitalize()} muestra una tendencia a usar sus recursos ideativos de manera activa, lo que le permite tomar la iniciativa en la interacción con otros y asumir la responsabilidad de satisfacer sus necesidades mediante interacciones prácticas con su entorno.")

        # Nivel de dependencia
        interpretaciones.append(evaluar_dependencia(
            a_total, p_total, sum_t, pop, ego, cont_fd))

        # Rigidez Ideativa
        # ? Mejorar redacción
        if ((a_total >= 4 and p_total == 0) or (a_total == 0 and p_total >= 4)) or (a_total >= p_total * 3 or p_total >= a_total * 3):
            interpretaciones.append(
                f"Se observan rasgos de rigidez en su actividad ideativa, lo cual constituye un factor desfavorable de cara al tratamiento, dado que {persona} tenderá a aferrarse a su propio punto de vista, dificultando la introducción de procesos de cambio en su pensamiento y conducta.")
        else:
            interpretaciones.append(
                "Cuenta con una adecuada flexibilidad ideativa, por lo que es capaz de desarrollar nuevos patrones de pensamiento y conducta, factor positivo para el proceso terapéutico.")

        if ma_total > mp_total + 1:
            interpretaciones.append("[PENDIENTE Ma>Mp+1]")

    # Paso 3: HVI, OBS, MOR – Distorsiones que afectan la ideación
    if variables.get("HVI") == "Positivo":
        interpretaciones.append("[PENDIENTE HVI POSITIVO]")

    if variables.get("OBS") == "Positivo":
        interpretaciones.append("[PENDIENTE OBS POSITIVO]")

    if variables.get("MOR", 0) >= 2:
        interpretaciones.append(
            f"Se observa una marcada tendencia hacia el pesimismo en su actividad ideativa, que hace que {persona} tienda a manifestar prejuicios negativos sobre el futuro y a mantener expectativas poco favorables.")

    # Paso 4: Lado izquierdo del EB (FM+m)
    # ? Pendiente evaluación individual de cada lado, FM vs m
    mov_ina = variables.get("m", 0)

    if mov_ina > 1:
        interpretaciones.append("[PENDIENTE m AUMENTADA]")

    if estados_simples.get("FM+m") in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE FM+m ALTO - MUY ALTO]")

    if estados_simples.get("FM+m") == "normal":
        interpretaciones.append(
            f"Su actividad ideativa periférica muestra un adecuado nivel de activación, lo que indica que {persona} registra tanto sus necesidades primarias como secundarias insatisfechas según lo esperado sin producir un aumento en sus preocupaciones o malestar interno.")

    if estados_simples.get("FM+m") in ["bajo", "muy bajo"]:
        interpretaciones.append(
            f"Su actividad ideativa periférica muestra un bajo nivel de activación, lo que si bien indica que {persona} no experimenta un aumento de tensión por la insatisfacción de sus necesidades primarias o secundarias, se debe a que probablemente no está realizando un adecuado registro de estas.")

    # Paso 5: Intelec
    intelec = variables.get("Intelec", None)
    if intelec > 5:
        interpretaciones.append(
            f"Se observa que {persona} se sirve de la intelectualización como parte fundamental de su funcionamiento psicológico, lo que le permite mitigar el impacto de las emociones disfóricas, pero que {articulo} vuelve muy vulnerable a la desorganización en situaciones de sobrecarga emocional.")

    # Paso 6: Sum6, SumPon6 y Cod Críticos
    interpretaciones.append(evaluar_cod_especiales(variables))

    # Paso 7: MQ y distorsión de M
    interpretaciones.append("[VERIFICAR DISTORSIONES DE M]")

    # Paso 8: Cualidad de M
    interpretaciones.append("[VERIFICAR CUALIDAD DE M]")

    return interpretaciones


def evaluar_dependencia(a_total, p_total, sum_t, populares, ego, cont_fd):

    contador_dependencia = 0

    if p_total > a_total + 1:
        contador_dependencia += 1
    if sum_t > 1:
        contador_dependencia += 1
    if populares in ["alto", "muy alto"]:
        contador_dependencia += 1
    if ego in ["bajo", "muy bajo"]:
        contador_dependencia += 1
    if cont_fd > 0:
        contador_dependencia += 1

    return f"[INDICADORES DEPENDENCIA: {contador_dependencia}]"


def evaluar_cod_especiales(variables):
    dv_uno = variables.get("DV1", 0)
    dv_dos = variables.get("DV2", 0)
    dr_uno = variables.get("DR1", 0)
    dr_dos = variables.get("DR2", 0)
    inc_uno = variables.get("INC1", 0)
    inc_dos = variables.get("INC2", 0)
    fab_uno = variables.get("FAB1", 0)
    fab_dos = variables.get("FAB2", 0)
    alog = variables.get("ALOG", 0)
    contam = variables.get("CONTAM", 0)

    sum6 = variables.get("SumBrut6", 0)
    sumpon6 = variables.get("SumPon6", 0)

    return "[PENDIENTE ANÁLISIS CCEE]"
