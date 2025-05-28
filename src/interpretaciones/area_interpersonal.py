
def interpretar_interpersonal(variables, estados_simples):
    """
    Interpreta el área de relaciones interpersonales: contacto, representación de otros, vínculo, cooperación.
    """

    interpretaciones = []
    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"

    # Paso 1: CDI y HVI
    cdi = variables.get("CDI", "Negativo")
    if cdi == "Positivo":
        interpretaciones.append(
            f"Se observa que {persona} cuenta con un índice de inhabilidad social positivo, lo que implica una serie de dificultades para relacionarse de manera adaptativa en la esfera social, llevándole a acumular tensión al estar en contacto con los demás.")

    hvi = variables.get("HVI", "Negativo")
    if hvi == "Positivo":
        interpretaciones.append("[PENDIENTE HVI POSITIVO]")

    # Paso 2: Relación a:p
    # ? Incorporar matices con P, T, Fd y Rigidez
    tot_a = variables.get("a", 0)
    tot_p = variables.get("p", 0)
    sum_mov = tot_a + tot_p

    ap_txt = ""
    if sum_mov > 4:
        if tot_p > tot_a + 1:
            ap_txt = "Muestra una tendencia a asumir un rol pasivo en la interacción con los demás, por lo que deja que ellos tomen la iniciativa, evita asumir la responsabilidad de sus decisiones y espera que su entorno actúe en función de sus necesidades."
        else:
            ap_txt = "Muestra una adecuada capacidad para asumir la iniciativa en la interacción con los demás, tomando responsabilidad de sus decisiones sin apoyarse en exceso en su entorno."

    interpretaciones.append(ap_txt)

    # Paso 3: Respuestas de comida (Fd) y textura (T)
    fd = variables.get("Fd", 0)
    if fd:
        interpretaciones.append("[PENDIENTE Fd PRESENTE]")

    sum_t = variables.get("SumT", 0)
    if sum_t == 0:
        interpretaciones.append(
            f"Su capacidad para identificar sus necesidades de contacto es menor a lo esperado, lo que indica que {persona} tiende a asumir una postura más reservada y cautelosa en la interacción con otros.")

    if sum_t == 1:
        interpretaciones.append(
            f"Su capacidad para identificar sus necesidades de contacto es adecuada, por lo que {persona} cuenta con disposición a establecer contacto con los demás según lo esperado.")

    if sum_t > 1:
        interpretaciones.append("[PENDIENTE SumT>1]")

    # Paso 4: Análisis de los contenidos humanos
    todo_h = estados_simples.get("TodoH", "Indefinido")
    todo_h_txt = ""
    if todo_h == "muy alto":
        todo_h_txt = ""
    if todo_h == "alto":
        todo_h_txt = ""
    if todo_h == "normal":
        todo_h_txt = ""
    if todo_h == "bajo":
        todo_h_txt = "Su interés en el componente humano se encuentra por debajo de lo esperado"
    if todo_h == "muy bajo":
        todo_h_txt = ""

    # ? Añadir matices sobre el tipo de contenido H predominante
    parrafo_cont_h = f"{todo_h_txt}, En cuanto a cómo construye las conceptualizaciones de los demás, "

    interpretaciones.append(parrafo_cont_h)

    # Paso 5: GHR:PHR
    # ? Interpretable si GHR+PHR > 2
    ghr = variables.get("GHR", 0)
    phr = variables.get("PHR", 0)

    if ghr + phr >= 3:
        if phr >= ghr:
            interpretaciones.append(
                f"Respecto a su eficacia interpersonal, se observan dificultades de adaptabilidad que llevan a {persona} a ser percibida de manera poco favorable por los demás. Además, dado que sus constructos sobre los demás contienen sesgos, su percepción de los otros y sobre los vínculos se encuentra alterada.")

        if ghr > phr:
            interpretaciones.append(
                f"Respecto a su eficacia interpersonal, se observa que {persona} es capaz de establecer vínculos positivos, profundos y empáticos con los demás.")

    # Paso 6: PER, COP y AG
    per = variables.get("PER", 0)  # * Significativo si es > 2
    cop = variables.get("COP", 0)
    ag = variables.get("AG", 0)

    if per > 2:
        interpretaciones.append("[PENDIENTE PER>2]")

    if cop == 0 and ag <= 1:
        interpretaciones.append("[PENDIENTE COP = 0 and AG <= 1]")

    if cop <= 1 and ag == 2:
        interpretaciones.append(
            f"Además, se observa que {persona} tiende a percibir la agresividad como componente natural en las relaciones personales, por lo que es más proclive a manifestar conductas agresivas hacia los demás.")

    if cop <= 2 and ag > 2:
        interpretaciones.append("[PENDIENTE COP <= 2 and AG > 2]")

    if cop == 2 and ag <= 1:
        interpretaciones.append("[PENDIENTE COP == 2 and AG <= 1]")

    if cop == 3 and ag == 2:
        interpretaciones.append("[PENDIENTE COP == 3 and AG == 2]")

    # Paso 7: Índice de aislamiento
    aisl = variables.get("Aisl/R", 0)

    if aisl > 0.33:
        interpretaciones.append("[PENDIENTE AISL>0.33]")
    if aisl > 0.25:
        interpretaciones.append("[PENDIENTE AISL>0.25]")

    # Paso 8: Contenidos de M y FM con pares.
    interpretaciones.append("[VERIFICAR CUALI DE FM O M CON PAR]")

    return interpretaciones
