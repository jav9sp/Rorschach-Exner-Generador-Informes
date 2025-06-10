from evaluacion.factores_riesgo import evaluar_factores
from utils.unir_interpretaciones import unir_interpretaciones


def interpretar_preliminares(variables, estados_simples):
    persona = "el evaluado" if variables.get(
        "Genero") == "M" else "la evaluada"

    interpretaciones = []

    intro = f"En el presente documento se describen los principales hallazgos sobre el funcionamiento cognitivo y psíquico {persona} tras la aplicación del test de Rorschach."

    r_total = variables.get("R", 0)
    l_lambda = variables.get("Lambda", 0)

    validez = verificar_validez(r_total, l_lambda)
    interpretaciones.append(f"{intro} {validez}")

    interpretaciones.append(verificar_alto_rendimiento(persona, variables))

    interpretaciones.extend(verificar_productividad(
        persona, variables, estados_simples))

    s_con = variables.get("SCON TXT")
    interpretaciones.append(s_con)

    interpretaciones.extend(evaluar_factores(variables, estados_simples))

    interpretaciones.append(
        f"A continuación, se describen las principales conclusiones sobre el funcionamiento de {persona} en cada una de sus áreas.")

    return interpretaciones


def verificar_validez(r_total, l_lambda):
    """
    Verifica si el protocolo es válido.
    Inválido si R<14 y Lambda>0.99
    """

    if l_lambda > 0.99 and r_total < 14:
        return "Se constata que su disposición durante la evaluación no fue suficientemente cooperativa, por lo que se considera el protocolo como inválido al no contar con la información suficiente para establecer una interpretación estable en el tiempo."

    return "Se constata que su disposición durante la evaluación fue cooperativa, por lo que el protocolo se considera como válido y que la información recopilada es suficiente para establecer conclusiones estables en el tiempo."


def verificar_productividad(persona, variables, estados_simples):
    """
    Calcula el nivel de productividad evaluando múltiples variables.
    Devuelve dos párrafos: uno con fortalezas y otro con dificultades, usando unir_interpretaciones().
    """
    intro_alto = "En cuanto a su rendimiento intelectual, sus principales fortalezas se observan en "
    intro_normal = ""
    intro_bajo = "Por otro lado, sus dificultades se manifiestan principalmente en "

    # Diccionarios de interpretación por variable
    interpretaciones = {
        "R": {
            "muy alto": "un nivel de productividad muy por encima de lo esperado",
            "normal": "un adecuado nivel de productividad",
            "alto": "un nivel de productividad por sobre lo esperado",
            "bajo": "un nivel de productividad bajo lo esperado",
            "muy bajo": "un muy bajo nivel de productividad, que apunta a la presencia de limitaciones cognitivas",
        },
        "DQ+": {
            "muy alto": "[PENDIENTE DQ+ MUY ALTO]",
            "normal": "capacidad para realizar trabajo de análisis y síntesis según lo esperado",
            "alto": "[PENDIENTE DQ+ ALTO]",
            "bajo": "baja capacidad de análisis y síntesis",
            "muy bajo": "su dificultad para realizar trabajo de análisis y síntesis",
        },
        "XA%": {
            "muy alto": "[PENDIENTE XA% MUY ALTO]",
            "alto": "[PENDIENTE XA% ALTO]",
            "normal": "adecuado ajuste perceptivo",
            "bajo": "[PENDIENTE XA% BAJO]",
            "muy bajo": "su marcada tendencia a realizar interpretaciones poco convencionales de la realidad",
        },
        "Compljs": {
            "muy alto": "[PENDIENTE Compljs MUY ALTO]",
            "alto": "[PENDIENTE Compljs ALTO]",
            "normal": "[PENDIENTE Compljs NORMAL]",
            "bajo": "baja capacidad para procesar múltiples estímulos a la vez",
            "muy bajo": "su marcada simplicidad cognitiva que le impide trabajar con múltiples estímulos a la vez",
        },
        "Zf": {
            "muy alto": "[PENDIENTE Zf MUY BAJO]",
            "alto": "[PENDIENTE Zf BAJO]",
            "normal": "[PENDIENTE Zf NORMAL]",
            "bajo": "[PENDIENTE Zf BAJO]",
            "muy bajo": "una baja motivación en la tarea de relacionar los estímulos del entorno de manera significativa y darle sentido",
        },
        "SumV": {
            "muy alto": "[PENDIENTE SumV MUY ALTO]",
            "alto": "[PENDIENTE SumV ALTO]",
            "normal": "[PENDIENTE SumV NORMAL]",
            "bajo": "[PENDIENTE SumV BAJO]",
            "muy bajo": "[PENDIENTE SumV MUY BAJO]",
        },
        "Zsum": {
            "muy alto": "[PENDIENTE Zsum MUY ALTO]",
            "alto": "[PENDIENTE Zsum ALTO]",
            "normal": "[PENDIENTE Zsum NORMAL]",
            "bajo": "[PENDIENTE Zsum BAJO]",
            "muy bajo": "[PENDIENTE Zsum MUY BAJO]",
        },
        "W": {
            "muy alto": "[PENDIENTE W MUY ALTO]",
            "alto": "[PENDIENTE W ALTO]",
            "normal": "[PENDIENTE W NORMAL]",
            "bajo": "[PENDIENTE W BAJO]",
            "muy bajo": "[PENDIENTE W MUY BAJO]",
        },
        "FD": {
            "muy alto": "[PENDIENTE FD MUY ALTO]",
            "alto": "[PENDIENTE FD ALTO]",
            "normal": "[PENDIENTE FD NORMAL]",
            "bajo": "[PENDIENTE FD BAJO]",
            "muy bajo": "[PENDIENTE FD MUY BAJO]",
        },
        "DQv": {
            "muy alto": "[PENDIENTE DQv MUY ALTO]",
            "alto": "[PENDIENTE DQv ALTO]",
            "normal": "[PENDIENTE DQv NORMAL]",
            "bajo": "[PENDIENTE DQv BAJO]",
            "muy bajo": "[PENDIENTE DQv MUY BAJO]",
        },
        "Intereses": {
            "muy alto": "[PENDIENTE Intereses MUY ALTO]",
            "alto": "[PENDIENTE Intereses ALTO]",
            "normal": "[PENDIENTE Intereses NORMAL]",
            "bajo": "[PENDIENTE Intereses BAJO]",
            "muy bajo": "[PENDIENTE Intereses MUY BAJO]",
        },
    }

    # Separo interpretaciones por funcionamiento
    funcionamiento_alto = []
    funcionamiento_adecuado = []
    funcionamiento_bajo = []

    for variable, niveles in interpretaciones.items():
        valor = estados_simples.get(variable)
        if valor:
            interpretacion = niveles.get(valor.lower())
            if not interpretacion:
                continue

            if valor.lower() == "normal":
                funcionamiento_adecuado.append(interpretacion)
            elif valor.lower() in ["alto", "muy alto"]:
                funcionamiento_alto.append(interpretacion)
            else:
                funcionamiento_bajo.append(interpretacion)
        else:
            funcionamiento_bajo.append(
                f"no se encontró información suficiente para el indicador {variable}"
            )

    parrafos = []

    if funcionamiento_adecuado:
        normales = unir_interpretaciones(funcionamiento_adecuado)
        parrafos.append(f"{intro_normal}{normales}.")

    if funcionamiento_alto:
        altos = unir_interpretaciones(funcionamiento_alto)
        parrafos.append(f"{intro_alto}{altos}")

    if funcionamiento_bajo:
        bajos = unir_interpretaciones(funcionamiento_bajo)
        parrafos.append(f"{intro_bajo}{bajos}.")

    parrafos.append("[INCLUIR INTERPRETACIÓN USO DEL LENGUAJE]")

    return parrafos


def verificar_alto_rendimiento(persona, variables):
    """
    Verifica si la persona cuenta con la constelación de alto CI
    Retorna la interpretación si es verdadero o None
    """

    dq_plus = variables.get("DQ+", 0)
    z_sum = variables.get("Zsum", 0)
    w_sum = variables.get("W", 0)
    dq_vaga = variables.get("DQv", 0)

    if dq_plus > 4 and z_sum > 30 and w_sum > 12 and dq_vaga == 0:
        return f"Se observa que {persona} reúne indicadores suficientes para encontrarse dentro de un rendimiento cognitivo cualitativamente superior a la media, pese a ello, es recomendado contrastar esto mediante un examen más profundo para corroborarlo."

    return None
