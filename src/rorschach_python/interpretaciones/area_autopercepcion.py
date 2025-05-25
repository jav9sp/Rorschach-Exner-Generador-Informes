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
        ego_txt = f"Su índice de egocentrismo se encuentra muy por encima de lo esperado, lo que indica que {persona} se encuentra excesivamente autocentrada, tiende a despreocuparse de su mundo exterior y a otorgar demasiada prioridad a su propio punto de vista."
    if ego == "alto":
        ego_txt = ""
    if ego == "normal":
        ego_txt = ""
    if ego == "bajo":
        ego_txt = ""
    if ego == "muy bajo":
        ego_txt = ""

    reflejos = variables.get("Fr+rF", 0)
    reflejos_txt = ""
    if reflejos:
        reflejos_txt = "[PENDIENTE]"

    parrafo = f"{ego_txt} {reflejos_txt}"
    interpretaciones.append(parrafo)

    # Paso 3: FD y V en relación con la historia personal
    # Paso 5: An y Xy
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

    # ? Añadir matices sobre el tipo de contenido H predominante

    interpretaciones.append(todo_h_txt)

    # Paso 8: Búsqueda de proyecciones en:
    # 8a: Respuestas con FQ
    # 8b: Respuestas MOR
    # 8c: Respuestas de movimientos
    # 8d: Sobreelaboraciones verbales

    return interpretaciones
