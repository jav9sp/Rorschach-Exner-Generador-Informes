
def interpretar_procesamiento(df, variables, estados_simples):
    """
    INCOMPLETO
    Interpreta el área de procesamiento de la información a partir de indicadores formales.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Evaluar L, EB, OBS y HVI
    lambda_ = estados_simples.get("Lambda", "Indefinido")
    if lambda_ == "muy alto":
        interpretaciones.append(f"{persona.capitalize()} muestra una marcada tendencia a usar sus recursos de manera económica y sobre simplificar sus percepciones al analizar al campo estimular, evitando las ambigüedades y la incorporación de información emocional, lo que lo lleva a perder parte importante de la información del medio.")

    if lambda_ == "alto":
        interpretaciones.append("[PENDIENTE LAMBDA ALTO]")

    if lambda_ == "normal":
        interpretaciones.append(f"{persona.capitalize()} es capaz de usar sus recursos cognitivos de manera equilibrada, siendo capaz de simplificar sus percepciones en justa medida, incorporando la información emocional y realizando un registro eficiente de la información del entorno.")

    if lambda_ == "bajo":
        interpretaciones.append("[PENDIENTE LAMBDA BAJO]")

    if lambda_ == "muy bajo":
        interpretaciones.append("[PENDIENTE LAMBDA MUY BAJO]")

    obs = variables.get("OBS", "Indefinido")

    if obs == 'Positivo':
        interpretaciones.append("[PENDIENTE OBS POSITIVO]")

    hvi = variables.get("HVI", "Indefinido")

    if hvi == 'Positivo':
        interpretaciones.append("[PENDIENTE HVI POSITIVO]")

    # Paso 1: Zf – Frecuencia de Actividad Organizativa
    zf = estados_simples.get("Zf", None)

    if zf == "muy alto":
        interpretaciones.append(
            f"Su iniciativa y motivación en la tarea de organizar los estímulos del entorno y relacionarlos de manera significativa está muy por encima de lo esperado, por lo que {persona} realiza un esfuerzo mayor en su procesamiento de información [que puede estar relacionado a características perfeccionistas o un alto rendimiento].")

    if zf == "alto":
        interpretaciones.append(
            f"Su iniciativa y motivación en la tarea de organizar los estímulos del entorno y relacionarlos de manera significativa se encuentra por encima de lo esperado, por lo que {persona} realiza un alto esfuerzo cognitivo en el procesamiento de información.")

    if zf == "normal":
        interpretaciones.append(
            f"Su iniciativa y motivación en la tarea de organizar los estímulos del entorno y relacionarlos de manera significativa se encuentra dentro de lo esperado, por lo que {persona} realiza un adecuado esfuerzo cognitivo en el procesamiento de información.")

    if zf == "bajo":
        interpretaciones.append(
            f"Su iniciativa y motivación en la tarea de organizar los estímulos del entorno y relacionarlos de manera significativa es menor a lo esperado, por lo que {persona} realiza un menor esfuerzo cognitivo en el procesamiento de la información.")

    if zf == "muy bajo":
        interpretaciones.append(
            "Su iniciativa y motivación en la tarea de organizar la información del entorno y relacionarla de manera significativa se encuentra muy por debajo de lo esperado, lo cual [apunta a la presencia de limitaciones cognitivas o un potencial intelectual inhibido por factores emocionales].")

    # Paso 2: W:D:Dd – Estilo de acercamiento
    w = estados_simples.get("W", "Indefinido")
    d = estados_simples.get("D", "Indefinido")
    dd = estados_simples.get("Dd", "Indefinido")

    interpretaciones.append(interpretar_acercamiento(w, d, dd, persona))

    # Paso 3: Secuencia de enfoque
    interpretaciones.append(evaluar_secuencia_localizacion(df, persona))

    # Paso 4: W:M – Ambición Intelectual
    tipo_vivencial = variables.get("Tipo Vivencial", "Indefinido")
    sum_w = variables.get("W", 0)
    sum_m = variables.get("M", 0)

    ambicion_intelectual = calcular_ambicion_intelectual(
        tipo_vivencial, sum_w, sum_m)
    interpretaciones.append(ambicion_intelectual)

    # Paso 5: Zd – Estilo de esfuerzo cognitivo
    zd = variables.get("Estilo Cognitivo", "Indefinido")

    if zd == "Normal":
        interpretaciones.append(
            "Su estilo de procesamiento es normal, lo que le permite discriminar la información importante de la accesoria al examinar el campo estimular, facilitando su resolución de problemas y toma de decisiones.")

    if zd == "Hipoincorporador":
        interpretaciones.append(
            "Su estilo cognitivo es hipoincorporador, por lo que no espera a integrar toda la información importante a la hora de resolver problemas, reflejando impulsividad y negligencia en su proceso de toma de decisiones.")

    if zd == "Hiperincorporador":
        interpretaciones.append("Su estilo cognitivo es hiperincorporador, por lo que tiende a querer recopilar toda la información del entorno sin discriminar aquella importante de la accesoria, llevándole a abrumarse con información y paralizarse al resolver problemas o tomar decisiones.")

    # Paso 6: PSV
    psv = variables.get("PSV", 0)

    if psv:
        interpretaciones.append("[PENDIENTE PSV PRESENTE]")

    # Paso 7: DQ – Calidad del procesamiento
    # ? Acá debería existir un análisis entre DQ y FQ
    dq_plus = estados_simples.get("DQ+", "Indefinido")
    dq_o = estados_simples.get("DQo", "Indefinido")
    dq_v = estados_simples.get("DQv", "Indefinido")
    dq_v_plus = estados_simples.get("DQv/+", "Indefinido")

    interpretaciones.append("[PENDIENTE VER CALIDAD DQ]")

    # Paso 8: Secuencia DQ
    interpretaciones.append("[PENDIENTE VER SECUENCIA DQ]")

    return interpretaciones


def calcular_ambicion_intelectual(tipo_vivencial, sum_w, sum_m):
    """
    Calcula la proporción de W:M según el tipo vivencial
    """
    if sum_w and sum_m and sum_m > 0:
        proporcion_real = sum_w / sum_m

        # Proporciones esperadas según tipo vivencial
        proporciones_esperadas = {
            "Introversivo": 1.5,
            "Ambigual": 2,
            "Extroversivo": 3,
            "Indefinido": 2
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
        interpretacion = f"Se observa que {persona} cuenta con patrones de registro consistentes y metódicos, por lo que es capaz de recopilar la información del entorno de manera ordenada y predecible, lo cual constituye un indicador importante de eficacia en esta tarea."
    else:
        interpretacion = f"Se observa que {persona} no cuenta con patrones de registro consistentes y metódicos, por lo que no es capaz de organizar sus recursos de manera eficaz para recoger la información del entorno."

    return interpretacion


def interpretar_acercamiento(w, d, dd, persona):
    estilo_normal = all([w == "normal", d == "normal", dd == "normal"])

    if estilo_normal:
        return (
            f"Su estilo de acercamiento a los estímulos es equilibrado, por lo que {persona} es capaz de trabajar de manera teórica y captar la totalidad del campo estimular, así como trabajar de manera más práctica identificando los elementos más obvios e importantes."
        )

    frases = []

    if w in ["alto", "muy alto"] and d in ["bajo", "muy bajo"]:
        frases.append(
            f"Su estilo de acercamiento a los estímulos es principalmente teórico y global, por lo que {persona} tiende a invertir mayor energía en la resolución de problemas, disminuyendo su capacidad de trabajo práctico y la identificación de los detalles más obvios del campo estimular.")

    if w in ["bajo", "muy bajo"] and d in ["alto", "muy alto"]:
        frases.append(
            f"Su estilo de acercamiento a los estímulos es principalmente práctico y económico, por lo que {persona} tiende a identificar rápidamente los elementos más obvios del campo estimular e invertir menor energía en la resolución de problemas, disminuyendo su capacidad de trabajo teórico."
        )

    if dd in ["alto", "muy alto"]:
        frases.append(
            "Además, se observa una marcada tendencia a realizar un acercamiento más personal a los estímulos, centrando su atención en elementos que pasan desapercibidos para la mayoría, lo que refleja una pérdida de la visión de conjunto y de eficacia práctica en la resolución de problemas. [Además, esto se relaciona con rasgos perfeccionistas o una actitud huidiza ante la complejidad y una mayor inseguridad en la toma de decisiones.]"
        )

    if not frases:
        return "[FALTA INTERPRETACIÓN W:D:Dd]"

    return " ".join(frases)
