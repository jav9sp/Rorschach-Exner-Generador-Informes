
def interpretar_afectos(variables, estados_simples):
    """
    Evalúa los rasgos afectivos: estilo vivencial, madurez emocional, expresión afectiva y regulación.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: DEPI y CDI
    depi = variables.get("DEPI", 0)
    depi_txt = variables.get("DEPI TXT")

    interpretaciones.append(depi_txt)

    cdi = variables.get("CDI", 0)

    if depi > 5 and cdi < 4:
        pass

    if depi > 5 and cdi > 3:
        pass

    if depi < 6 and cdi > 3:
        interpretaciones.append(
            f"Además, se observa que {persona} cuenta con un índice de inhabilidad social positivo, por lo que enfrenta múltiples dificultades en la esfera social, pudiendo generar depresiones secundarias en el mediano largo plazo.")

    # Paso 2: Lambda, EB Extroversivo, EBPer
    lambda_ = estados_simples.get("Lambda", None)
    eb = variables.get("Tipo Vivencial", None)
    ebper = variables.get("EBPer", None)

    eb_txt = ""
    if eb == "Indefinido":
        eb_txt = f"No se observa suficiente información para determinar el tipo vivencial de {persona}, por lo tanto, no es posible estimar su estilo de respuesta base a los estímulos del entorno."
    if eb == "Introversivo":
        eb_txt = "Su tipo vivencial es introversivo, por lo que su respuesta base a los estímulos del entorno es de tipo cognitiva, usa predominantemente la ideación y no procesa emociones mientras resuelve problemas y toma decisiones."
    if eb == "Extroversivo":
        eb_txt = "Su tipo vivencial es extroversivo, por lo que su respuesta base a los estímulos del entorno es de tipo emocional, suele tener intercambios emocionales más espontáneos y el contacto social es fundamental para su funcionamiento general."
    if eb == "Ambigual":
        eb_txt = f"Su tipo vivencial es ambigual, por lo que su respuesta base a los estímulos es internamente inconsistente, pudiendo responder de manera racional o emocional a los mismos estímulos de manera impredecible. Esto hace que {persona} tienda a cometer más errores en la toma de decisiones y sea particularmente vulnerable ante las situaciones de estrés."

    if lambda_ in ["alto", "muy alto"] and eb == "Extratensivo":
        # Es extratensivo evitativo
        pass

    interpretaciones.append(eb_txt)

    # Paso 3: Análisis del lado derecho de la eb
    sum_v = estados_simples.get("SumV", "Indefinido")
    sum_t = estados_simples.get("SumT", "Indefinido")
    sum_y = estados_simples.get("SumY", "Indefinido")
    sum_c_prima = estados_simples.get("SumC'", "Indefinido")

    sum_sh_txt = ""

    if sum_v in ["alto", "muy alto"]:
        pass
    if sum_t in ["alto", "muy alto"]:
        pass
    if sum_y in ["alto", "muy alto"]:
        pass
    if sum_c_prima in ["alto", "muy alto"]:
        pass

    interpretaciones.append(sum_sh_txt)

    # Paso 4: SumC': SumPonC
    tot_c_prima = variables.get("SumC'", 0)
    sum_pon_c = variables.get("SumPonC", 0)

    if tot_c_prima >= sum_pon_c:
        extern_txt = f"Por otro lado, {persona} muestra una tendencia a internalizar sus emociones en lugar de externalizarlas. Esto resulta en una acumulación de tensión interna que puede derivar hacia el cuerpo y dar paso a trastornos psicosomáticos al mediano largo plazo."
    else:
        extern_txt = f"Por otro lado, {persona} muestra capacidad para externalizar sus emociones según lo esperado, lo que le permite realizar intercambios emocionales y disminuir la acumulación de tensión interna."

    # Paso 5: Proporción afectiva (Afr)
    afr = estados_simples.get("Afr", "Indefinido")
    afr_txt = ""
    if afr == "muy alto":
        pass
    if afr == "alto":
        pass
    if afr == "normal":
        afr_txt = f"Además, muestra una adecuada responsividad a la estimulación emocional, por lo que {persona} tiende a incrementar su productividad en situaciones emocionalmente estimulantes, tal como se esperaría. Asimismo, busca este tipo de entornos de manera apropiada."
    if afr == "bajo":
        pass
    if afr == "muy bajo":
        afr_txt = f"Su nivel de interés por procesar estímulos afectivos se encuentra muy por debajo de lo esperado, alcanzando una tendencia a rehuir de la estimulación emocional, lo que indica que {persona} siente incomodidad ante los afectos y tiende a retraerse socialmente."

    parrafo = f"{extern_txt} {afr_txt}"

    interpretaciones.append(parrafo)

    # Paso 6: índice de intelectualización
    intelec = variables.get("Intelec")

    if intelec > 3:
        pass

    # Paso 7: Proyección de color (CP)
    cp = variables.get("CP", 0)

    if cp > 0:
        pass

    # Paso 8: FC:CF+C y C Pura
    # Paso 9: Espacio blanco (S)
    # Paso 10: Respuestas complejas (relación con Z y EB), composición y cualidad, complejas por m o Y, Complj.Col-SH y Complj.SH.

    return interpretaciones
