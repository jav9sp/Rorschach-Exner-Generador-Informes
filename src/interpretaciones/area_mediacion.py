def interpretar_mediacion(variables, estados_simples):
    """
    Interpreta la mediación cognitiva, es decir, el ajuste perceptivo de la persona evaluada.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # PREVIOS: R, OBS y L

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
            ajuste_general_txt = f"Se observa que {persona} es capaz de ejercer control cognitivo sobre sus percepciones e interpretar la realidad según los niveles de convencionalidad esperados."
        if xa_estado == "bajo" and wda_estado == "bajo":
            ajuste_general_txt = f"[PENDIENTE]{persona}"
        if xa_estado == "muy bajo" and wda_estado == "muy bajo":
            ajuste_general_txt = f"[PENDIENTE]{persona}"

    interpretaciones.append(ajuste_general_txt)

    # Paso 2: FQsin
    fqs = variables.get("FQxsin", None)
    fq_sin_txt = ""
    if fqs:
        fq_sin_txt = "[PENDIENTE]"

    interpretaciones.append(fq_sin_txt)

    # Paso 3: X-%, FQ- y S-
    x__menos_porc = estados_simples.get("X-%", None)
    fq_menos = estados_simples.get("FQx-", None)
    s_menos = estados_simples.get("S-%", None)

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
        populares_txt = f"Por otro lado, se observa que tiene una menor capacidad para ajustar su conducta según lo socialmente esperado, por lo que {persona} podría enfrentar dificultades de adaptación incluso en situaciones sociales obvias.."
    if populares == "muy bajo":
        populares_txt = "[PENDIENTE]"

    interpretaciones.append(populares_txt)

    # Paso 5: Frecuencia de FQ+
    fq_plus = variables.get("FQx+", None)
    if fq_plus > 4:
        interpretaciones.append(
            f"Si bien {persona} muestra una buena capacidad perceptiva y alta motivación, muestra una tendencia marcada a la búsqueda de exactitud, indicando rasgos perfeccionistas u obsesivos.")

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

    interpretaciones.append(x_plus_txt)

    xu_porc = estados_simples.get("Xu%", None)
    xu_txt = ""
    if xu_porc == "muy alto":
        xu_txt = f"Además, se observa que {persona} tiene una marcada tendencia a añadir sesgos a sus percepciones en función de sus necesidades y a manifestar un alto autocentramiento que le dificulta ver las cosas como lo hacen los demás. Esto implica que puede llegar a presentar dificultades de comunicación y conflictos con su entorno si se le somete a altas expectativas sociales."
    if xu_porc == "alto":
        xu_txt = f"Por otro lado, se observa que {persona} tiene una tendencia a sesgar sus percepciones en función de sus propias necesidades, lo cual le permite expresar su individualidad y creatividad, pero puede llegar a generar conflictos de comunicación si las demandas de convencionalidad del entorno son muy altas."
    if xu_porc == "normal":
        xu_txt = "[PENDIENTE]"
    if xu_porc == "bajo":
        xu_txt = "[PENDIENTE]"
    if xu_porc == "muy bajo":
        xu_txt = "[PENDIENTE]"

    interpretaciones.append(xu_txt)

    return interpretaciones
