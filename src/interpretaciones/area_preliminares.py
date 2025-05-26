from evaluacion.factores_riesgo import evaluar_factores


def interpretar_preliminares(variables, estados_simples):
    persona = "el evaluado" if variables.get(
        "Genero") == "M" else "la evaluada"

    interpretaciones = []

    intro = f"En el presente documento se describen los principales hallazgos sobre el funcionamiento cognitivo y psíquico {persona} tras la aplicación del test de Rorschach."

    validez = verificar_validez(persona, variables)
    interpretaciones.append(f"{intro} {validez}")

    interpretaciones.extend(verificar_productividad(persona, estados_simples))

    s_con = variables.get("SCON TXT")
    interpretaciones.append(s_con)

    interpretaciones.append(evaluar_factores(variables, estados_simples))

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
            "bajo": "baja capacidad de análisis y síntesis",
            "normal": "capacidad para realizar trabajo de análisis y síntesis según lo esperado ",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "XA%": {
            "muy bajo": "su marcada tendencia a realizar interpretaciones poco convencionales de la realidad ",
            "bajo": "[PENDIENTE]",
            "normal": "adecuado ajuste perceptivo",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "Compljs": {
            "muy bajo": "su marcada simplicidad cognitiva que le impide trabajar con múltiples estímulos a la vez ",
            "bajo": "baja capacidad para procesar múltiples estímulos a la vez",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "Zf": {
            "muy bajo": "una baja motivación en la tarea de relacionar los estímulos del entorno de manera significativa y darle sentido",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "SumV": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "Zsum": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "W": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "FD": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "DQv": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "Intereses": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
        },
        "Lenguaje": {
            "muy bajo": "[PENDIENTE]",
            "bajo": "[PENDIENTE]",
            "normal": "[PENDIENTE]",
            "alto": "[PENDIENTE]",
            "muy alto": "[PENDIENTE]"
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
