def interpretar_autopercepcion(variables, estados_simples):
    """
    Interpreta el área de autopercepción: identidad, introspección, representación del yo y del cuerpo.
    """

    interpretaciones = []
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    vocal = "o" if persona == "el evaluado" else "a"

    # Paso 1: OBS y HVl
    obs = variables.get("OBS")  # Negativo o Positivo
    hvi = variables.get("HVI")  # Negativo o Positivo

    # Paso 2: Índice de egocentrismo y reflejos
    ego = estados_simples.get("Ego", "Indefinido")
    ego_txt = ""
    if ego == "muy alto":
        ego_txt = f"Su índice de egocentrismo se encuentra muy por encima de lo esperado, lo que indica que {persona} se encuentra excesivamente autocentrad{vocal}, tiende a despreocuparse de su mundo exterior y a otorgar demasiada prioridad a su propio punto de vista."
    if ego == "alto":
        ego_txt = f"Su índice de egocentrismo se encuentra elevado en relación con lo esperado, lo que indica que {persona} tiene una inusual preocupación por sí mism{vocal}, tiende a despreocuparse de su mundo exterior y a otorgar demasiada prioridad a su propio punto de vista."
    if ego == "normal":
        ego_txt = ""
    if ego == "bajo":
        ego_txt = ""
    if ego == "muy bajo":
        ego_txt = ""

    sum_v = variables.get("SumV", 0)
    mor = variables.get("MOR", 0)

    autoval_txt = ""
    if sum_v > 0 or mor > 2:
        autoval_txt = ""
    else:
        autoval_txt = "No se observan indicadores de autovaloración negativa, por lo que en principio cuenta con una adecuada autoestima."

    reflejos = variables.get("Fr+rF", 0)
    reflejos_txt = ""
    if reflejos > 0:
        reflejos_txt = f"Además, se observan indicadores de narcisismo, por lo que {persona} tiende a sobrestimar su valía personal, lo que indica inmadurez personal."

    parrafo = f"{ego_txt} {autoval_txt} {reflejos_txt}"
    interpretaciones.append(parrafo)

    # Paso 3: FD y V en relación con la historia personal
    # Paso 5: An y Xy

    an = variables.get("An", 0)
    xy = variables.get("Xy", 0)

    if an + xy > 3:
        # Distorsión de la autoimagen, hipocondria
        pass

    # Paso 6: MOR y contenidos asociados

    # Paso 7: H:(H)+Hd+(HD), revisión de FQ y contenidos de categoría H-, GHR.PHR
    todo_h = estados_simples.get("TodoH", "Indefinido")
    todo_h_txt = ""
    if todo_h == "muy alto":
        todo_h_txt = ""
    if todo_h == "alto":
        todo_h_txt = ""
    if todo_h == "normal":
        todo_h_txt = ""
    if todo_h == "bajo":
        todo_h_txt = f"Se observan dificultades en los procesos de identificación que derivan del bajo interés que {persona} tiene por el componente humano, lo cual apunta a la presencia de conflictos de identidad, de autoimagen o de relación con los demás."
    if todo_h == "muy bajo":
        todo_h_txt = ""

    interpretaciones.append(todo_h_txt)

    # ? Añadir matices sobre el tipo de contenido H predominante
    h_dom = ""
    hd_dom = "Por otro lado, se observa que tiende a construir las conceptualizaciones sobre sí mismo de manera parcializada y sesgada, lo que refleja inmadurez en la percepción que tiene de sí mismo."
    ima_h_dom = ""
    ima_hd_dom = ""
    hx_txt = "Además, se observa una tendencia a establecer aspectos del autoconcepto mediante la intelectualización, lo que puede derivar en la incorporación de distorsiones importantes."

    ghr = variables.get("GHR", 0)
    phr = variables.get("PHR", 0)

    ghr_phr_txt = ""

    if ghr < phr:
        ghr_phr_txt = f"{persona} muestra aspectos que lo llevan a distorsionar la percepción que tiene de sí mismo, por lo que las conceptualizaciones que genera sobre su autoconcepto son menos efectivas para responder de manera adaptativa."
    else:
        ghr_phr_txt = "[PENDIENTE]"

    interpretaciones.append(ghr_phr_txt)

    # Paso 8: Búsqueda de proyecciones en:
    # 8a: Respuestas con FQ
    # 8b: Respuestas MOR
    # 8c: Respuestas de movimientos
    # 8d: Sobreelaboraciones verbales

    return interpretaciones
