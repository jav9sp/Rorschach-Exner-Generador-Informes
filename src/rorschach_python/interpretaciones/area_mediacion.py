def interpretar_mediacion(variables, estados_simples):
    """
    Interpreta la mediación cognitiva, es decir, el ajuste perceptivo de la persona evaluada.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: XA% y WDA%
    xa_bruto = variables.get("XA%", None)
    wda_bruto = variables.get("WDA%", None)
    xa_estado = estados_simples.get("XA%", None)
    wda_estado = estados_simples.get("WDA%", None)

    ajuste_general_txt = ""
    if xa_bruto == 1 and wda_bruto == 1:
        ajuste_general_txt = f"{persona.capitalize()} muestra una adecuada capacidad para ejercer control cognitivo sobre sus percepciones e interpretaciones de la realidad según lo esperado, pero se observa una marcada tendencia a ser muy convencional, por lo que actúa en base a las demandas de su entorno, evita cometer errores y elimina la expresión de su creatividad y originalidad."
    else:
        if xa_estado == "alto" and wda_estado == "alto":
            ajuste_general_txt = f"Se observa que {persona} es capaz de ejercer control cognitivo sobre sus percepciones e interpretar la realidad como lo hace la mayoría según lo esperado, mostrando un nivel de convencionalidad mayor al esperado."
        if xa_estado == "normal" and wda_estado == "normal":
            ajuste_general_txt = f"Se observa que {persona} es capaz de ejercer control cognitivo sobre sus percepciones e interpretar la realidad como lo hace la mayoría según lo esperado"
        if xa_estado == "bajo" and wda_estado == "bajo":
            ajuste_general_txt = f"[PENDIENTE]{persona}"
        if xa_estado == "muy bajo" and wda_estado == "muy bajo":
            ajuste_general_txt = f"[PENDIENTE]{persona}"

    # Paso 2: FQsin
    fqs = variables.get("FQxsin", None)
    fqs_txt = ""
    if fqs:
        fqs_txt = "[PENDIENTE]"

    # Paso 3: X%, FQ- y S-
    x_porc = estados_simples.get("X%", None)
    fq_menos = estados_simples.get("FQ-", None)
    s_menos = estados_simples.get("S-", None)

    # Aquí podrías hacer combinaciones lógicas, o interpretar por separado
    if fq_menos == "alto" or s_menos == "alto":
        interpretaciones.append(
            "• Se observa una alta frecuencia de FQ- o S-, lo que indica distorsión en la evaluación de la realidad.")
    elif fq_menos == "normal" and s_menos == "normal":
        interpretaciones.append(
            "• La frecuencia de FQ- y S- se encuentra en niveles normales, lo que sugiere estabilidad perceptiva.")

    # Paso 4: Respuestas populares
    populares = estados_simples.get("Populares", None)
    populares_txt = ""
    if populares == "muy alto":
        populares_txt = "[PENDIENTE]"
    if populares == "alto":
        populares_txt = "[PENDIENTE]"
    if populares == "normal":
        populares_txt = f"Por otro lado, se observa que su capacidad para responder convencionalmente según lo socialmente esperado es adecuada, por lo que {persona} será capaz de comportarse de manera adaptativa en situaciones socialmente obvias."
    if populares == "bajo":
        populares_txt = "[PENDIENTE]"
    if populares == "muy bajo":
        populares_txt = "[PENDIENTE]"

    # Paso 5: Frecuencia de FQ+
    fq_plus = estados_simples.get("FQ+", None)
    fq_plus_txt = ""
    if fq_plus == "muy alto":
        fq_plus_txt = "[PENDIENTE]"
    if fq_plus == "alto":
        fq_plus_txt = "[PENDIENTE]"
    if fq_plus == "normal":
        fq_plus_txt = "[PENDIENTE]"
    if fq_plus == "bajo":
        fq_plus_txt = "[PENDIENTE]"
    if fq_plus == "muy bajo":
        fq_plus_txt = "[PENDIENTE]"

    # Paso 6: X+% y Xu%
    x_plus = estados_simples.get("X+%", None)
    x_plus_txt = ""
    if x_plus == "muy alto":
        x_plus_txt = "[PENDIENTE]"
    if x_plus == "alto":
        x_plus_txt = "[PENDIENTE]"
    if x_plus == "normal":
        x_plus_txt = "[PENDIENTE]"
    if x_plus == "bajo":
        x_plus_txt = "[PENDIENTE]"
    if x_plus == "muy bajo":
        x_plus_txt = "[PENDIENTE]"

    xu = estados_simples.get("Xu%", None)
    xu_txt = ""
    if xu == "muy alto":
        xu_txt = f"Además, se observa que {persona} tiene una marcada tendencia a añadir sesgos a sus percepciones en función de sus necesidades y a manifestar un alto autocentramiento que le dificulta ver las cosas como lo hacen los demás. Esto implica que puede llegar a presentar dificultades de comunicación y conflictos con su entorno si se le somete a altas expectativas sociales."
    if xu == "alto":
        xu_txt = "[PENDIENTE]"
    if xu == "normal":
        xu_txt = "[PENDIENTE]"
    if xu == "bajo":
        xu_txt = "[PENDIENTE]"
    if xu == "muy bajo":
        xu_txt = "[PENDIENTE]"

    primer_parrafo = f"{ajuste_general_txt}"
    segundo_parrafo = f"{fqs_txt}"
    tercer_parrafo = f"{fq_plus_txt}"
    cuarto_parrafo = f"{populares_txt}"
    quinto_parrafo = f"{x_plus_txt} {xu_txt}"

    interpretaciones.append(primer_parrafo)
    interpretaciones.append(segundo_parrafo)
    interpretaciones.append(tercer_parrafo)
    interpretaciones.append(cuarto_parrafo)
    interpretaciones.append(quinto_parrafo)

    return interpretaciones
