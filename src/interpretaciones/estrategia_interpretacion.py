def determinar_estrategia_interpretacion(variables):
    """
    Determina la estrategia de interpretación a seguir según la primera condición positiva.
    Devuelve una lista ordenada de áreas a explorar.
    """
    secuencias = [
        ("PTI", lambda v: v.get("PTI", 0) > 3, [
            "Ideación", "Mediación", "Procesamiento", "Controles",
            "Afectos", "Autopercepción", "Percepción Interpersonal"
        ]),
        (("DEPI", "CDI"), lambda v: v.get("DEPI", 0) > 5 and v.get("CDI", 0) > 3, [
            "Percepción interpersonal", "Autopercepción", "Controles",
            "Afectos", "Procesamiento", "Mediación", "Ideación"
        ]),
        ("DEPI", lambda v: v.get("DEPI", 0) > 5, [
            "Afectos", "Controles", "Autopercepción",
            "Percepción interpersonal", "Procesamiento", "Mediación", "Ideación"
        ]),
        ("D<AdjD", lambda v: v.get("PuntD", 0) < v.get("AdjD", 0), [
            "Controles", "Estrés situacional"
        ]),
        ("CDI", lambda v: v.get("CDI", 0) > 3, [
            "Controles", "Afectos", "Autopercepción",
            "Percepción interpersonal", "Procesamiento", "Mediación", "Ideación"
        ]),
        ("AdjD", lambda v: v.get("AdjD", 0) < 0, [
            "Controles"
        ]),
        ("Lambda", lambda v: v.get("Lambda", 0) > 0.99, [
            "Procesamiento", "Mediación", "Ideación",
            "Controles", "Afectos", "Autopercepción", "Percepción interpersonal"
        ]),
        ("Fr+rF", lambda v: v.get("Fr+rF", 0) > 0, [
            "Autopercepción", "Percepción interpersonal"
        ]),
        ("EB Introversivo", lambda v: v.get("Tipo Vivencial", "").lower() == "introversivo", [
            "Ideación", "Procesamiento", "Mediación",
            "Controles", "Afectos", "Autopercepción", "Percepción interpersonal"
        ]),
        ("EB Extroversivo", lambda v: v.get("Tipo Vivencial", "").lower() == "extroversivo", [
            "Afectos", "Autopercepción", "Percepción interpersonal",
            "Controles", "Procesamiento", "Mediación", "Ideación"
        ]),
        ("p>a+1", lambda v: v.get("p", 0) > v.get("a", 0) + 1, [
            "Ideación", "Procesamiento", "Mediación",
            "Controles", "Autopercepción", "Percepción interpersonal", "Afectos"
        ]),
        ("HVI", lambda v: v.get("HVI", "") == "Positivo", [
            "Ideación", "Procesamiento", "Mediación",
            "Controles", "Autopercepción", "Percepción interpersonal", "Afectos"
        ])
    ]

    for clave, condicion, secuencia in secuencias:
        if condicion(variables):
            return {
                "Variable activadora": clave,
                "Secuencia de exploración": secuencia
            }

    return {
        "Variable activadora": None,
        "Secuencia de exploración": []
    }
