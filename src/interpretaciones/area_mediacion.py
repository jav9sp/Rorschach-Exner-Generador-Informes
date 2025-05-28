def interpretar_mediacion(variables, estados_simples):
    """
    INCOMPLETO
    Interpreta la mediación cognitiva, es decir, el ajuste perceptivo de la persona evaluada.
    """

    interpretaciones = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    articulo = "lo" if persona == "M" else "la"

    # PREVIOS: R, OBS y L

    # Paso 1: XA%, WDA% y X+%
    # ? Normales entre 0.78 y 0.9
    xa_bruto = variables.get("XA%", 0)
    wda_bruto = variables.get("WDA%", 0)

    if xa_bruto >= 0.96 and wda_bruto >= 0.96:
        interpretaciones.append(f"{persona.capitalize()} muestra una adecuada capacidad para ejercer control cognitivo sobre su percepción e interpretación de la realidad según lo esperado, pero se observa una marcada tendencia a ser muy convencional, por lo que actúa en base a las demandas de su entorno, evita cometer errores y elimina la expresión de su creatividad y originalidad.")

    elif 0.78 <= xa_bruto <= 0.9 and 0.78 <= wda_bruto <= 0.9:
        interpretaciones.append(
            f"{persona.capitalize()} muestra una adecuada capacidad para ejercer control cognitivo sobre su percepción e interpretación de la realidad según lo esperado, por lo que es capaz de percibir la realidad como lo hace la mayoría la mayor parte del tiempo.")

    elif xa_bruto <= 0.78 and wda_bruto <= 0.78:
        interpretaciones.append(
            f"{persona.capitalize()} muestra dificultades para ejercer control cognitivo sobre su percepción e interpretación de la realidad, por lo que tiende a comportarse de manera poco convencional [EVALUAR DESVIACIÓN - CORTE EN 0.78] [aumentando el riesgo de conflictos de comunicación con su entono y su capacidad para generar conductas que respondan adecuadamente a las demandas de su entorno.]")

    else:
        interpretaciones.append(
            F"[PENDIENTE EVALUACIÓN XA% {xa_bruto} Y WDA% {wda_bruto}]")

    # Paso 2: FQsin
    fqs = variables.get("FQxsin", 0)
    if fqs:
        interpretaciones.append(
            "[PENDIENTE FQsin PRESENTE, VERIFICAR CONTENIDO QUE ACOMPAÑA A FQsin]")

    # Paso 3: X-%, FQ- y S-
    # ? X-% > 0.2 es significativo
    x_menos_porc = variables.get("X-%", 0)
    nvl_dos = variables.get("Nvl-2", 0)
    fq_menos = estados_simples.get("FQx-", 0)
    s_menos_porc = estados_simples.get("S-%", 0)

    if x_menos_porc > 0.2:
        interpretaciones.append("[PENDIENTE X-% > 0.2]")

    if x_menos_porc > 0.2 and nvl_dos > 0.4:
        interpretaciones.append("[VERIFICAR INTERFERENCIAS Nvl-2]")

    if x_menos_porc > 0.2 and s_menos_porc < 0.4:
        interpretaciones.append("[INTERFERENCIAS GENERALIZADAS S-% < 0.4]")

    if fq_menos in ["alto", "muy alto"]:
        interpretaciones.append("[EVALUAR HOMOGENEIDAD DE F-]")

    # Paso 4: Respuestas populares
    populares = estados_simples.get("Populares", "Indefinido")
    if populares == "muy alto":
        interpretaciones.append(
            f"Su capacidad para identificar aquellos elementos más habituales del campo estimular está muy aumentada, por lo que su adecuación perceptiva está muy por encima de la comparación normativa. Esto indica que {persona} es es mucho más consciente de las exigencias sociales y tiende a acumular malestar si no cumple con las expectativas del entorno.")

    if populares == "alto":
        interpretaciones.append(
            f"Su capacidad para identificar aquellos elementos más habituales del campo estimular está levemente aumentada, por lo que su adecuación perceptiva es mayor a la comparación normativa. Esto indica que {persona} es más sensible a las exigencias sociales y tiende a proteger mucho su identidad percibida.")

    if populares == "normal":
        interpretaciones.append(
            f"Su capacidad para identificar aquellos elementos más habituales del campo estimular es adecuada, por lo que su adecuación perceptiva se ajusta a la comparación normativa. Esto indica que {persona} tiene una adecuada sensibilidad a las exigencias sociales y es capaz de actuar de manera convencional en escenarios socialmente obvios.")

    if populares == "bajo":
        interpretaciones.append(
            f"Su capacidad para identificar aquellos elementos más habituales del campo estimular está levemente disminuida, por lo que su adecuación perceptiva en relación con la comparación normativa es menor. Esto indica que {persona} tiene una sensibilidad menor a las exigencias sociales que lo llevan a actuar de manera menos convencional en escenarios socialmente obvios.")

    if populares == "muy bajo":
        interpretaciones.append(
            f"Su capacidad para identificar aquellos elementos más habituales del campo estimular está muy disminuida, por lo que su adecuación perceptiva en relación con la comparación normativa se encuentra muy por debajo. Esto indica que {persona} tiene una muy baja sensibilidad a las exigencias sociales [EVALUAR DESAJUSTES] [lo que indica un pobre contacto con la realidad] por lo que no será capaz de comportarse convencionalmente incluso en situaciones sociales obvias.")

    # Paso 5: Frecuencia de FQ+
    fq_plus = variables.get("FQx+", 0)
    if fq_plus > 4:
        interpretaciones.append(
            f"Si bien {persona} muestra una buena capacidad perceptiva y alta motivación, muestra una tendencia marcada a la búsqueda de exactitud, [indicando rasgos perfeccionistas u obsesivos].")

    # Paso 6: X+% y Xu%
    x_plus_porc = variables.get("X+%", 0)
    xu = estados_simples.get("Xu%", 0)
    if x_plus_porc < 0.78 and xu in ["alto", "muy alto"]:
        interpretaciones.append(f"Las posibles dificultades de {persona} se evidencian en su excesivo autocentramiento, lo que {articulo} lleva a sesgar sus percepciones según sus propias necesidades y a aferrarse a su punto de vista, rechazando perspectivas más convencionales de la realidad o la posibilidad de adoptar otros enfoques. Esto podría volverse problemático, especialmente si el entorno le exige ajustarse a las expectativas sociales, en cuyo caso las probabilidades de conflicto aumentan.")

    if x_plus_porc < 0.78 and xu == "normal":
        interpretaciones.append("[PENDIENTE Xu% NORMAL]")

    return interpretaciones
