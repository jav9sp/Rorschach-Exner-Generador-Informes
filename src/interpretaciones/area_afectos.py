
def interpretar_afectos(variables, estados_simples):
    """
    INCOMPLETO
    Evalúa los rasgos afectivos: estilo vivencial, madurez emocional, expresión afectiva y regulación.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: DEPI y CDI
    depi = variables.get("DEPI", 0)
    interpretaciones.append(variables.get("DEPI TXT"))

    cdi = variables.get("CDI", 0)
    if depi > 5 and cdi < 4:
        interpretaciones.append("[PENDIENTE DEPI>5 Y CDI<4]")
    if depi > 5 and cdi > 3:
        interpretaciones.append("[PENDIENTE DEPI>5 Y CDI>3]")

    if depi < 6 and cdi > 3:
        interpretaciones.append(
            f"Además, se observa que {persona} cuenta con un índice de inhabilidad social positivo, por lo que enfrenta múltiples dificultades en la esfera social, pudiendo generar depresiones secundarias en el mediano largo plazo.")

    # Paso 2: Lambda, EB Extroversivo, EBPer
    lambda_estado = estados_simples.get("Lambda", None)
    tipo_vivencial = variables.get("Tipo Vivencial", None)
    ebper = variables.get("EBPer", "-")

    if tipo_vivencial == "Indefinido":
        interpretaciones.append(
            f"No se observa suficiente información para determinar el tipo vivencial de {persona}, por lo tanto, no es posible estimar su estilo de respuesta base a los estímulos del entorno.")

    if tipo_vivencial == "Introversivo":
        interpretaciones.append(
            "Su tipo vivencial es introversivo, por lo que su respuesta base a los estímulos del entorno es de tipo cognitiva, usa predominantemente la ideación y no procesa emociones mientras resuelve problemas y toma decisiones.")

    if tipo_vivencial == "Extroversivo":
        interpretaciones.append(
            "Su tipo vivencial es extroversivo, por lo que su respuesta base a los estímulos del entorno es de tipo emocional, suele tener intercambios emocionales más espontáneos y el contacto social es fundamental para su funcionamiento general.")

    if tipo_vivencial == "Ambigual":
        interpretaciones.append(
            f"Su tipo vivencial es ambigual, por lo que su respuesta base a los estímulos es internamente inconsistente, pudiendo responder de manera racional o emocional a los mismos estímulos de manera impredecible. Esto hace que {persona} tienda a cometer más errores en la toma de decisiones y sea particularmente vulnerable ante las situaciones de estrés.")

    if lambda_estado in ["alto", "muy alto"] and tipo_vivencial == "Extratensivo":
        interpretaciones.append("[PENDIENTE L ALTO Y EXTRATENSIVO]")

    if ebper != '-':
        interpretaciones.append("[PENDIENTE EBPer PRESENTE]")

    # Paso 3: Análisis del lado derecho de la eb
    sum_v = estados_simples.get("SumV", "Indefinido")
    sum_t = estados_simples.get("SumT", "Indefinido")
    sum_y = estados_simples.get("SumY", "Indefinido")
    sum_c_prima = estados_simples.get("SumC'", "Indefinido")

    sum_sh_txt = ""

    if sum_v in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE SumV ALTO - MUY ALTO]")

    if sum_t in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE SumT ALTO - MUY ALTO]")

    if sum_y in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE SumY ALTO - MUY ALTO]")

    if sum_c_prima in ["alto", "muy alto"]:
        interpretaciones.append("[PENDIENTE SumC' ALTO - MUY ALTO]")

    interpretaciones.append(sum_sh_txt)

    # Paso 4: SumC': SumPonC
    tot_c_prima = variables.get("SumC'", 0)
    sum_pon_c = variables.get("SumPonC", 0)

    if tot_c_prima >= sum_pon_c:
        extern_txt = f"Por otro lado, {persona} muestra una tendencia a internalizar sus emociones en lugar de externalizarlas. Esto resulta en una acumulación de tensión interna que puede derivar hacia el cuerpo y dar paso a trastornos psicosomáticos al mediano largo plazo."
    else:
        extern_txt = f"Por otro lado, {persona} muestra capacidad para externalizar sus emociones según lo esperado, lo que le permite realizar intercambios emocionales y disminuir la acumulación de tensión interna."

    interpretaciones.append(extern_txt)

    # Paso 5: Proporción afectiva (Afr)
    afr = estados_simples.get("Afr", "Indefinido")
    if afr == "muy alto":
        interpretaciones.append("[PENDIENTE AFR MUY ALTO]")

    if afr == "alto":
        interpretaciones.append("[PENDIENTE AFR ALTO]")

    if afr == "normal":
        interpretaciones.append(
            f"Además, muestra una adecuada responsividad a la estimulación emocional, por lo que {persona} tiende a incrementar su productividad en situaciones emocionalmente estimulantes, tal como se esperaría. Asimismo, busca este tipo de entornos de manera apropiada.")

    if afr == "bajo":
        interpretaciones.append("[PENDIENTE AFR BAJO]")

    if afr == "muy bajo":
        interpretaciones.append(
            f"Su nivel de interés por procesar estímulos afectivos se encuentra muy por debajo de lo esperado, alcanzando una tendencia a rehuir de la estimulación emocional, lo que indica que {persona} siente incomodidad ante los afectos y tiende a retraerse socialmente.")

    # Paso 6: índice de intelectualización
    intelec = variables.get("Intelec")
    if intelec > 3:
        interpretaciones.append("[PENDIENTE INTELEC>3]")

    # Paso 7: Proyección de color (CP)
    cp = variables.get("CP", 0)
    if cp > 0:
        interpretaciones.append("[PENDIENTE CP PRESENTE]")

    # Paso 8: FC:CF+C y C Pura
    fc = variables.get("FC", 0)
    cf = variables.get("CF", 0)
    c_pura = variables.get("C", 0)

    # ? Esperado FC:CF+C > 2:1 con C cero
    # ? Integrar aparición de contenidos críticos Bl, Sx, Fi

    if fc > (cf + c_pura) * 3 or (fc > 0 and (cf + c_pura == 0)):
        interpretaciones.append(
            f"En cuanto a la espontaneidad de sus descargas afectivas, se observa que {persona} tiende a sobre controlar sus intercambios afectivos, por lo que no puede relajarse cuando maneja sus emociones. [VERIFICAR RELACIONES INTERPERSONALES E INTEGRAR SI C' ES AUMENTADO]")

    # Paso 9: Espacio blanco (S)
    # Paso 10: Respuestas complejas (relación con Z y EB), composición y cualidad, complejas por m o Y, Complj.Col-SH y Complj.SH.

    return interpretaciones
