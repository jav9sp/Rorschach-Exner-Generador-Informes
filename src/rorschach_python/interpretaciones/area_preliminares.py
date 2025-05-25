from evaluacion.factores_riesgo import evaluar_factores


def interpretar_preliminares(variables, comparativa):
    persona = "del evaluado" if variables.get(
        "Genero") == "M" else "de la evaluada"

    interpretaciones = []

    inicio = f"En el presente documento se describen los principales hallazgos sobre el funcionamiento cognitivo y psíquico {persona} tras la aplicación del test de Rorschach."
    validez = verificar_validez(persona, variables)
    s_con = variables.get("SCON TXT")

    interpretaciones.append(f"{inicio} {validez}")
    interpretaciones.extend(verificar_productividad(persona, comparativa))
    interpretaciones.append(s_con)
    interpretaciones.append(evaluar_factores(variables, comparativa))

    interpretaciones.append(
        f"A continuación, se describen las principales conclusiones sobre el funcionamiento {persona} en cada una de sus áreas.")

    return interpretaciones


def verificar_validez(persona, variables):
    """
    Verifica si el protocolo es válido.
    Inválido si R<14 y Lambda>0.99
    """

    r_total = variables.get("R")
    l_lambda = variables.get("Lambda")

    if l_lambda > 0.99 and r_total < 14:
        return f"Se constata que la disposición {persona} durante la prueba no fue suficientemente cooperativa, por lo que se considera el protocolo como inválido al no contar con la información suficiente para establecer una interpretación estable en el tiempo."

    return f"Se constata que la disposición {persona} durante la prueba fue cooperativa, por lo que el protocolo es válido y las conclusiones que se presentan a continuación son estables en el tiempo."


def verificar_productividad(persona, df_comparativa):
    """
    Calcula el nivel de productividad evaluando DQ+, FQ, R, Compljs, Zf, Introspección (FD o V), M, Intereses, Lenguaje, Zsum, W y DQv
    """
    textos = []

    introduccion = f"En cuanto al rendimiento intelectual de {persona}, sus principales fortalezas se observan en "

    # Diccionarios de interpretación por variable
    interpretaciones = {
        "R": {
            "muy bajo": "un muy bajo nivel de productividad, que apunta a la presencia de limitaciones cognitivas,",
            "bajo": "un nivel de productividad bajo lo esperado",
            "normal": "un adecuado nivel de productividad",
            "alto": "un nivel de productividad por sobre lo esperado",
            "muy alto": "un nivel de productividad muy por encima de lo esperado"
        },
        "DQ+": {
            "muy bajo": "su dificultad para realizar trabajo de análisis y síntesis ",
            "bajo": "...",
            "normal": "capacidad para realizar trabajo de análisis y síntesis según lo esperado ",
            "alto": "...",
            "muy alto": "..."
        },
        "XA%": {
            "muy bajo": "su marcada tendencia a realizar interpretaciones poco convencionales de la realidad ",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "Compljs": {
            "muy bajo": "su marcada simplicidad cognitiva que le impide trabajar con múltiples estímulos a la vez ",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "Zf": {
            "muy bajo": "su falta de iniciativa en la tarea de relacionar los estímulos del entorno y darle sentido ",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "SumV": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "Zsum": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "W": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "FD": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "DQv": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "Intereses": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        },
        "Lenguaje": {
            "muy bajo": "...",
            "bajo": "...",
            "normal": "...",
            "alto": "...",
            "muy alto": "..."
        }
    }

    # Seperar las interpretaciones según funcionamiento adecuado o bajo
    funcionamiento_adecuado = []
    funcionamiento_bajo = []

    for variable, niveles in interpretaciones.items():
        valor = df_comparativa.get(variable)
        if valor:
            interpretacion = niveles.get(valor.lower())
            if not interpretacion:
                continue  # Salta si el valor no es esperado

            if valor.lower() in ["normal", "alto", "muy alto"]:
                funcionamiento_adecuado.append(interpretacion)
            elif valor.lower() in ["bajo", "muy bajo"]:
                funcionamiento_bajo.append(interpretacion)
        else:
            funcionamiento_bajo.append(
                f"No se encontró información suficiente para el indicador {variable}.")

    # Combinar todo en un solo bloque
    textos = [introduccion]
    if funcionamiento_adecuado:
        textos.extend(funcionamiento_adecuado)
    if funcionamiento_bajo:
        textos.append(
            "Por otro lado, sus dificultades se manifiestan principalmente en ")
        textos.extend(funcionamiento_bajo)

    return textos
