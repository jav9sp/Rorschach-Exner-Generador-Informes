
def evaluar_factores(variables, estados_simple):
    resultados = []

    persona = "el evaluado" if variables["Genero"] == "M" else "la evaluada"
    lambda_estado = estados_simple.get("Lambda", "Indefinido")
    eb = variables.get("Tipo Vivencial", 0)

    # Factor 1 - Ideacional con EB Intro + Lambda↓
    if eb == "Introversivo" and (lambda_estado in ["bajo", "muy bajo"]):
        resultados.append(f"Se observa que {persona} tienen bajas probabilidades de desarrollar futuros desajustes psíquicos los cuales, en caso de ocurrir, estarían vinculados a su estilo de funcionamiento ideacional, la falta de intercambio afectivo y la evitación de la toma de decisiones.")

    # Factor 1 - Afectivo con EB Extra + Lambda↓
    if eb == "Extroversivo" and (lambda_estado in ["bajo", "muy bajo"]):
        resultados.append(f"Se observa que {persona} tienen bajas probabilidades de desarrollar futuros desajustes psíquicos los cuales, en caso de ocurrir, estarían vinculados a su estilo de funcionamiento afectivo, su espontaneidad en la descarga de afectos y la toma de decisiones impulsiva.")

    # Factor 4 - Ambiguai + Lambda↑
    if eb == "Ambigual" and (lambda_estado in ["bajo", "muy bajo"]):
        resultados.append(
            f"Se observa que {persona} tienen un nivel de riesgo medio a desarrollar futuros desajustes psíquicos importantes, los cuales estarían vinculados a su estilo de funcionamiento inconsistente a la hora de resolver problemas y tomar decisiones.")

    # Factor 4 - EB Intro + Lambda↑
    if eb == "Introversivo" and (lambda_estado in ["alto", "muy alto"]):
        resultados.append(
            f"Se observa que {persona} tienen un nivel de riesgo medio a desarrollar futuros desajustes psíquicos importantes, los cuales estarían vinculados a su estilo de funcionamiento ideacional evitativo, su pensamiento simple y excesivo control sobre los afectos.")

    # Factor 5 - EB Extra + Lambda↑
    if eb == "Extroversivo" and (lambda_estado in ["alto", "muy alto"]):
        resultados.append(f"Se observa que {persona} tienen un nivel de riesgo medio a desarrollar futuros desajustes psíquicos importantes, los cuales estarían vinculados a su estilo de funcionamiento afectivo evitativo, su baja modulación de las descargas afectivas y su pensamiento demasiado concreto.")

    # Factor 8 - Ambiguai + Lambda↑
    if eb == "Ambigual" and (lambda_estado in ["alto", "muy alto"]):
        resultados.append(
            f"Se observa que {persona} tienen altas probabilidades de desarrollar futuros desajustes psíquicos importantes importantes debido a la marcada inconsistencia interna, su estilo de pensamiento demasiado simple y la dificultad para controlar los afectos.")

    if eb == "Indefinido":
        resultados.append(
            f"No existe información suficiente para estimar la presencia de factores de riesgo que alerten sobre posibles desajustes psíquicos importantes que {persona} pueda desarrollar en el corto mediano plazo.")

    # Variables desfavorables adicionales
    adicionales = []
    intro_adicionales = f"Por otro lado, se observa que {persona}"
    adicionales.append(intro_adicionales)

    # hvi = variables.get("HVI")
    # cdi = variables.get("CDI")
    # sum_s = estados_simple.get("S", "Indefinido")
    # intelec = estados_simple.get("Intelec", "Indefinido")
    # fr_rf = estados_simple.get("Fr+rF", "Indefinido")

    return resultados
