def interpretar_ideacion(variables, estados_simples):
    """
    Evalúa la ideación: estilo de pensamiento, activación cognitiva, coherencia, flexibilidad y elaboración lógica.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: EB Introversivo, Lambda, EBPer
    lambda_ = estados_simples.get("Lambda", "Indefinido")
    lambda_txt = ""
    if lambda_ == "muy alto":
        lambda_txt = "• El control cognitivo elevado (Lambda) permite regular los procesos ideativos de forma estructurada."
    if lambda_ == "alto":
        lambda_txt = "• El control cognitivo elevado (Lambda) permite regular los procesos ideativos de forma estructurada."
    if lambda_ == "normal":
        lambda_txt = "• El control cognitivo elevado (Lambda) permite regular los procesos ideativos de forma estructurada."
    if lambda_ == "bajo":
        lambda_txt = "• El control cognitivo elevado (Lambda) permite regular los procesos ideativos de forma estructurada."
    if lambda_ == "muy bajo":
        lambda_txt = "• El control cognitivo elevado (Lambda) permite regular los procesos ideativos de forma estructurada."

    eb = variables.get("Tipo Vivencial", "Indefinido")
    if eb == "Introversivo":
        interpretaciones.append(f"{persona}")

    ebper = variables.get("EBPer", "-")
    ebper_txt = ""
    if ebper != "-":
        ebper_txt = ""

    # Paso 2: a:p y Ma:Mp – Activación cognitiva
    a_total = variables.get("a", 0)
    p_total = variables.get("p", 0)
    ma_total = variables.get("Ma", 0)
    mp_total = variables.get("Mp", 0)
    sum_t = variables.get("SumT", 0)
    populares = estados_simples.get("Populares", 0)
    ego = estados_simples.get("Ego", 0)
    cont_fd = estados_simples.get("Fd", 0)

    ap_txt = ""
    if p_total > a_total + 1:
        ap_txt = f"{persona.capitalize()} muestra una actitud pasiva en sus procesos de ideación, por lo que tiende a asumir un rol pasivo en sus relaciones interpersonales y a no responsabilizarse por sus propias decisiones. Por este mismo motivo, suele refugiarse en la fantasía para satisfacer sus frustraciones de la vida real."
    else:
        ap_txt = f"{persona.capitalize()} muestra una tendencia a usar sus recursos ideativos de manera activa, lo que le permite tomar la iniciativa en la interacción con otros y asumir la responsabilidad de satisfacer sus necesidades mediante interacciones prácticas con su entorno."

    interpretaciones.append(ap_txt)

    flexibilidad = ""
    if ((a_total >= 4 and p_total == 0) or (a_total == 0 and p_total >= 4)) or (a_total >= 3 * p_total or p_total >= 3 * a_total):
        flexibilidad = f"Se observan rasgos de rigidez en su actividad ideativa, lo cual constituye un factor desfavorable de cara al tratamiento, dado que {persona} tenderá a aferrarse a su propio punto de vista, dificultando la introducción de procesos de cambio en su pensamiento y conducta."
    else:
        flexibilidad = "Pese a lo anterior, se observa que cuenta con una adecuada flexibilidad ideativa, por lo que es capaz de desarrollar nuevos patrones de pensamiento y conducta según lo esperado."

    interpretaciones.append(flexibilidad)

    if ma_total > mp_total + 1:
        ma_vs_mp_txt = "Escapa a la fantasía como mecanismo defensivo ante cualquier situación displacentera."

    # Paso 3: HVI, OBS, MOR – Distorsiones que afectan la ideación
    if variables.get("HVI") == "Positivo":
        pass
    if variables.get("OBS") == "Positivo":
        pass
    if variables.get("MOR", 0) >= 2:
        pass

    # Paso 4: Lado izquierdo del EB (FM+m)
    izq_eb_txt = ""
    if estados_simples.get("FM+m") in ["alto", "muy alto"]:
        izq_eb_txt = ""
        pass
    if estados_simples.get("FM+m") == "normal":
        izq_eb_txt = ""
        pass
    if estados_simples.get("FM+m") in ["bajo", "muy bajo"]:
        izq_eb_txt = f"Muestra un bajo nivel de activación de la ideación periférica producto de necesidades internas básicas y secundarias insatisfechas, lo que no significa que estas no existan, sino que {persona} está eliminando el registro de ellas."

    interpretaciones.append(izq_eb_txt)

    # Paso 5: Intelec
    intelec = variables.get("Intelec", None)
    if intelec > 5:
        interpretaciones.append("[INCORPORAR INTERPRETACIÓN INTELEC]")

    # Paso 6: Sum6, SumPon6 y Cod Críticos
    sum6 = variables.get("SumBrut6", 0)
    sumpon6 = variables.get("SumPon6", 0)
    if sum6 > 2:
        pass
    if sumpon6 > 2:
        pass
    interpretaciones.append("[INCORPORAR INTERPRETACIÓN DE CCEE]")

    # Paso 7: MQ y distorsión de M
    interpretaciones.append("[VERIFICAR DISTORSIONES DE M]")

    # Paso 8: Cualidad de M
    interpretaciones.append("[VERIFICAR CUALIDAD DE M]")

    return interpretaciones
