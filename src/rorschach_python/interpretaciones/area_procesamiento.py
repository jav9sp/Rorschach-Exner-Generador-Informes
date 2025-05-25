
def interpretar_procesamiento(data_respuestas, variables, estados_simples):
    """
    Interpreta el área de procesamiento de la información a partir de indicadores formales.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Evaluar L, EB, OBS y HVI
    # ? Todo esto debería estar en un primer párrafo
    lambda_ = estados_simples.get("Lambda", "Indefinido")
    lambda_txt = ""
    if lambda_ == "muy alto":
        lambda_txt = f"Se observa que {persona} muestra una marcada tendencia a usar sus recursos de manera conservadora y sobre simplificar sus percepciones al analizar al campo estimular, evitando las ambigüedades y la incorporación de información emocional, lo que lo lleva a perder parte importante de la información del medio."
    if lambda_ == "alto":
        pass
    if lambda_ == "normal":
        pass
    if lambda_ == "bajo":
        pass
    if lambda_ == "muy bajo":
        pass

    # Paso 1: Zf – Actividad exploratoria
    # ? En este párrafo podría estar Zf, Acercamiento y Patrones
    zf = estados_simples.get("Zf", None)
    zf_txt = ""
    if zf == "muy alto":
        pass
    if zf == "alto":
        pass
    if zf == "normal":
        pass
    if zf == "bajo":
        pass
    if zf == "muy bajo":
        zf_txt = "Su motivación por organizar la información del entorno y relacionarla de manera significativa se encuentra muy por debajo de lo esperado, por lo que realiza un nulo esfuerzo creativo en sus elaboraciones."

    # Paso 2: W:D:Dd – Estilo de acercamiento (global vs. detalle)
    w = estados_simples.get("W", "Indefinido")
    d = estados_simples.get("D", "Indefinido")
    dd = estados_simples.get("Dd", "Indefinido")

    estilo_normal = all([w == "normal", d == "normal", dd == "normal"])

    acercamiento = ""

    if estilo_normal:
        acercamiento = f"El estilo de acercamiento a los estímulos de {persona} es equilibrado, por lo que es capaz de trabajar de manera teórica y captar la totalidad del campo estimular, así como trabajar de manera más práctica identificando los elementos más obvios e importantes."

    # Paso 3: Secuencia de enfoque
    secuencia = evaluar_secuencia_localizacion(data_respuestas, persona)

    # Paso 4: W:M – Comparación entre producción visual y producción ideativa
    ambicion_intelectual = calcular_ambicion_intelectual(variables)

    # Paso 5: Zd – Estilo de esfuerzo cognitivo
    zd = variables.get("Estilo Cognitivo", "Indefinido")
    zd_txt = ""
    if zd == "Normal":
        zd_txt = "Su estilo de procesamiento es normal, lo que le permite discriminar la información importante de la accesoria al examinar el campo estimular, facilitando su resolución de problemas y toma de decisiones."
    if zd == "Hipoincorporador":
        zd_txt = "Su estilo cognitivo es hipoincorporador, por lo que no espera a integrar toda la información importante a la hora de resolver problemas, reflejando impulsividad y negligencia en su proceso de toma de decisiones."
    if zd == "Hiperincorporador":
        zd_txt = "Su estilo cognitivo es hiperincorporador, por lo que tiende a querer recopilar toda la información del entorno sin discriminar aquella importante de la accesoria, llevándole a abrumarse con información y paralizarse al resolver problemas o tomar decisiones."

    # Paso 6: PSV – Control cognitivo

    # Paso 7: DQ – Calidad del procesamiento

    # Paso 8: Secuencia DQ

    primer_parrafo = f"{lambda_txt}"
    segundo_parrafo = f"{zf_txt} {acercamiento} {secuencia}"
    tercer_parrafo = f"{ambicion_intelectual}"
    cuarto_parrafo = f"{zd_txt}"

    interpretaciones.append(primer_parrafo)
    interpretaciones.append(segundo_parrafo)
    interpretaciones.append(tercer_parrafo)
    interpretaciones.append(cuarto_parrafo)

    return interpretaciones


def calcular_ambicion_intelectual(variables):
    """
    Calcula la proporción de W:M según el tipo vivencial
    """
    tipo_vivencial = variables.get("Tipo Vivencial", "Indefinido").lower()
    total_w = variables.get("W", 0)
    total_m = variables.get("M", 0)

    if total_w and total_m and total_m > 0:
        proporcion_real = total_w / total_m

        # Proporciones esperadas según tipo vivencial
        proporciones_esperadas = {
            "introversivo": 1.5,
            "ambigual": 2,
            "indefinido": 2,
            "extratensivo": 3
        }

        proporcion_esperada = proporciones_esperadas.get(
            tipo_vivencial, "Indefinido")

        if proporcion_esperada:
            margen = 1.25  # tolerancia de +/- 1.25

            if abs(proporcion_real - proporcion_esperada) <= margen:
                return "En cuanto a su ambición intelectual, se muestra adecuada en relación con los recursos creativos, por lo que es capaz de plantearse metas realistas y poner en marcha los recursos suficientes para llevarla a cabo."
            elif proporcion_real > (proporcion_esperada + margen):
                # W>M
                return "En cuanto a su ambición intelectual, se muestra aumentada en relación con los recursos creativos que dispone para llevarla a cabo, por lo que tiende a plantearse metas poco realistas y a frustrarse en el proceso."
            elif proporcion_real < (proporcion_esperada - margen):
                # W<M
                return "En cuanto a su ambición intelectual, se muestra disminuida en relación con los recursos creativos que dispone para llevarla a cabo, por lo que tiende a plantearse metas conservadoras y más bajas de lo que es capaz de lograr."
    else:
        return "No se cuenta con información suficiente sobre W y M para evaluar la proporción en el contexto del tipo vivencial."


def evaluar_secuencia_localizacion(df_protocolo, persona):
    """
    Evalúa si el sujeto sigue patrones secuenciales coherentes en las localizaciones W, D y Dd.
    Retorna interpretación (str): análisis cualitativo del estilo de procesamiento.
    """

    # Orden jerárquico de localización
    orden_localizacion = {'W': 3, 'D': 2, 'DD': 1}

    # Filtrar columnas necesarias y limpiar datos
    datos = df_protocolo[['Lam', 'Loc']].dropna()
    datos['Loc'] = datos['Loc'].str.upper()

    def secuencia_ordenada(localizaciones):
        """Verifica si la secuencia contiene W, D y Dd en orden ascendente o descendente."""
        unicas = list(dict.fromkeys(localizaciones)
                      )  # mantener orden sin duplicados
        filtradas = [l for l in unicas if l in orden_localizacion]
        if set(filtradas) >= {'W', 'D', 'DD'}:
            valores = [orden_localizacion[l] for l in filtradas]
            return valores == sorted(valores) or valores == sorted(valores, reverse=True)
        return False

    conteo_laminas_con_patron = 0

    for _, grupo in datos.groupby('Lam'):
        locs = grupo['Loc'].tolist()
        if len(locs) < 2:
            continue  # se necesita más de una respuesta

        filtradas = [l for l in locs if l in orden_localizacion]
        if len(set(filtradas)) < 3:
            continue  # debe incluir W, D y Dd

        ordenada = secuencia_ordenada(filtradas)

        if ordenada:
            conteo_laminas_con_patron += 1

    # Interpretación según cantidad de láminas con patrón definido
    if conteo_laminas_con_patron >= 2:
        interpretacion = f"Se observa que {persona} cuenta con patrones de registro consistentes y metódicos, por lo que es capaz de recopilar la información del entonro de manera ordenada y predecible, lo cual constituye un indicador importante de eficacia en esta tarea."
    else:
        interpretacion = f"Se observa que {persona} no cuenta con patrones de registro consistentes y metódicos, por lo que no es capaz de organizar sus recursos de manera eficaz para recoger la información del entorno."

    return interpretacion
