def interpretar_autopercepcion(variables, estados_simples):
    """
    Interpreta el área de autopercepción: identidad, introspección, representación del yo y del cuerpo.
    """

    interpretaciones = []
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    vocal = "o" if variables["Genero"] == "M" else "a"

    # Paso 1: OBS y HVl
    obs = variables.get("OBS")  # Negativo o Positivo
    if obs == "Positivo":
        interpretaciones.append("[PENDIENTE OBS POSITIVO]")

    hvi = variables.get("HVI")  # Negativo o Positivo
    if hvi == "Positivo":
        interpretaciones.append("[PENDIENTE HVI POSITIVO]")

    # Paso 2: Índice de egocentrismo y reflejos
    # ? Incluir presencia o ausencia de reflejos
    ego = estados_simples.get("Ego", "Indefinido")
    if ego == "muy alto":
        interpretaciones.append(
            f"Su índice de egocentrismo se encuentra muy por encima de lo esperado, lo que indica que {persona} se encuentra excesivamente autocentrad{vocal}, tiende a despreocuparse de su mundo exterior y a otorgar demasiada prioridad a su propio punto de vista.")

    if ego == "alto":
        interpretaciones.append(
            f"Su índice de egocentrismo se encuentra elevado en relación con lo esperado, lo que indica que {persona} tiene una inusual preocupación por sí mism{vocal}, tiende a despreocuparse de su mundo exterior y a otorgar demasiada prioridad a su propio punto de vista.")

    if ego == "normal":
        interpretaciones.append(
            f"Su índice de egocentrismo se encuentra dentro de los parámetros esperados, por lo que la preocupación que {persona} tiene sobre sí mism{vocal} es adecuada, pudiendo prestar atención a sus necesidades personales sin descuidar su entorno.")

    if ego == "bajo":
        interpretaciones.append("[PENDIENTE EGO BAJO]")

    if ego == "muy bajo":
        interpretaciones.append("[PENDIENTE EGO MUY BAJO]")

    # ? Presencia de autovaloración negativa y baja autoestima
    sum_v = variables.get("SumV", 0)
    mor = variables.get("MOR", 0)

    if sum_v > 0 or mor > 2:
        interpretaciones.append("[PENDIENTE AUTOVALORACIÓN NEGATIVA]")
    else:
        interpretaciones.append(
            "No muestra indicadores de autovaloración negativa, por lo que es posible afirmar que cuenta con una adecuada autoestima.")

    reflejos = variables.get("Fr+rF", 0)
    if reflejos:
        interpretaciones.append(
            f"Además, se observan indicadores de narcisismo, por lo que {persona} tiende a sobrestimar su valía personal, lo que indica inmadurez personal.")

    # Paso 3: FD y V en relación con la historia personal
    fd = variables.get("FD", 0)
    if fd > 2:
        interpretaciones.append("[PENDIENTE FD>2]")

    if sum_v > 0 and (sum_v + fd > 2):
        interpretaciones.append("[PENDIENTE V+FD>2]")

    # Paso 5: An y Xy
    an = variables.get("An", 0)
    xy = variables.get("Xy", 0)

    if an + xy > 3:
        interpretaciones.append("[PENDIENTE AN+XY > 3]")

    if an + xy == 2:
        interpretaciones.append("[REVISAR DISTORSIONES AN+XY = 2]")

    # Paso 6: MOR y contenidos asociados
    if mor > 2:
        interpretaciones.append("[VERIFICAR CONTENIDOS MOR]")

    # Paso 7: H:(H)+Hd+(HD), revisión de FQ y contenidos de categoría H-, GHR.PHR
    # ? Debe interpretarse en conjunto si es que HVI es Positivo

    h_pura = variables.get("H", 0)
    sum_hd = variables.get("Hd", 0)
    sum_h_img = variables.get("(H)", 0)
    sum_hd_img = variables.get("(Hd)", 0)
    todo_h = estados_simples.get("TodoH", "Indefinido")
    ghr = variables.get("GHR", 0)
    phr = variables.get("PHR", 0)
    hx = variables.get("Hx", 0)

    todo_h_txt = ""
    if todo_h == "muy alto":
        todo_h_txt = "[PENDIENTE TODOH MUY ALTO]"

    if todo_h == "alto":
        todo_h_txt = "[PENDIENTE TODOH ALTO]"

    if todo_h == "normal":
        todo_h_txt = f"Su interés en el componente humano se encuentra dentro de lo esperado, por lo que {persona} es capaz de realizar trabajo de identificación para construir su autoconcepto."

    if todo_h == "bajo":
        todo_h_txt = f"Se observan dificultades en los procesos de identificación que derivan del bajo interés que {persona} tiene por el componente humano, lo cual apunta a la presencia de conflictos de identidad, de autoimagen o de relación con los demás."

    if todo_h == "muy bajo":
        todo_h_txt = "[PENDIENTE TODOH MUY BAJO]"

    if h_pura > sum_hd + sum_h_img + sum_hd_img:
        interpretaciones.append("[PENDIENTE H > (H)+Hd+(Hd)]")
    else:
        interpretaciones.append("[PENDIENTE H < (H)+Hd+(Hd)]")

    # Tipo de H dominante
    # h_dom = ""

    # hd_dom = "Por otro lado, se observa que tiende a construir las conceptualizaciones sobre sí mismo de manera parcializada y sesgada, lo que refleja inmadurez en la percepción que tiene de sí mismo."

    # ima_h_dom = "Se observa que lo hace desde un distanciamiento del mundo real, es decir, a partir de datos fantaseados, reflejando inmadurez y una construcción de su autoconcepto basada principalmente en la fantasía"

    # ima_hd_dom = ""

    interpretaciones.append("[PENDIENTE ANÁLISIS H DOMINANTE]")

    # Si aparece Hx
    if hx:
        interpretaciones.append(
            "Además, se observa una tendencia a establecer aspectos del autoconcepto mediante la intelectualización, lo que puede derivar en la incorporación de distorsiones importantes.")

    interpretaciones.append(f"{todo_h_txt}")

    if ghr < phr:
        interpretaciones.append(
            f"Por otro lado, {persona} muestra una tendencia a incorporar aspectos desadaptativos o distorsionadores que hacen que la construcción que hace sobre las conceptualizaciones sobre sí mism{vocal} tenga una menor efectividad para producir respuestas adaptativas en su funcionamiento auto perceptivo.")
    else:
        interpretaciones.append("[PENDIENTE GHR>PHR]")

    # Paso 8: Búsqueda de proyecciones en:
    # 8a: Respuestas con FQ-
    # 8b: Respuestas MOR
    # 8c: Respuestas de movimientos
    # 8d: Sobre elaboraciones verbales

    interpretaciones.append(
        "[VERIFICAR PROYECCIONES EN FQ-, MOR, M Y VERBALES]")

    return interpretaciones
