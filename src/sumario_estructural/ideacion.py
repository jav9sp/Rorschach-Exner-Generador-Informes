
def calcular_codigos_especiales(variables):
    """
    Calcula SumBrut6 (Raw Sum6) y WSum6 (SumPon6) a partir de las frecuencias de CC.EE.
    """
    claves_criticas = ["DV1", "DV2", "INC1", "INC2",
                       "DR1", "DR2", "FAB1", "FAB2", "ALOG", "CONTAM"]

    # SumBrut6: suma no ponderada de las 10 claves críticas
    sumbrut6 = sum(variables.get(k, 0) for k in claves_criticas)

    sum6ce = sum(variables.get(k, 0)
                 for k in claves_criticas if k.endswith("1"))
    sum6ce2 = sum(variables.get(k, 0)
                  for k in claves_criticas if k.endswith('2'))

    # Valores claves críticas
    dv1 = variables.get("DV1", 0)
    dv2 = variables.get("DV2", 0)
    inc1 = variables.get("INC1", 0)
    inc2 = variables.get("INC2", 0)
    dr1 = variables.get("DR1", 0)
    dr2 = variables.get("DR2", 0)
    fab1 = variables.get("FAB1", 0)
    fab2 = variables.get("FAB2", 0)
    alog = variables.get("ALOG", 0)
    contam = variables.get("CONTAM", 0)
    ab = variables.get("AB", 0)

    # WSum6: suma ponderada de los 10 códigos especiales críticos
    wsum6 = (1 * dv1 + 2 * dv2 + 2 * inc1 +
             4 * inc2 + 3 * dr1 + 6 * dr2 +
             4 * fab1 + 7 * fab2 + 5 * alog +
             7 * contam
             )

    return {
        "DV1": dv1,
        "DV2": dv2,
        "INC1": inc1,
        "INC2": inc2,
        "DR1": dr1,
        "DR2": dr2,
        "FAB1": fab1,
        "FAB2": fab2,
        "ALOG": alog,
        "CONTAM": contam,
        "AB": ab,
        "Sum6CE": sum6ce,
        "Sum6CE2": sum6ce2,
        "SumBrut6": sumbrut6,
        "SumPon6": wsum6
    }


def calcular_indicadores_ideacion(df, dic_variables):
    # Ma : Mp - contar M con subíndice a o p
    ma = 0
    mp = 0
    for fila in df[['Det', 'FQ']].dropna().itertuples():
        det = str(fila.Det)
        partes = det.split('.')
        for parte in partes:
            if parte.startswith('M'):
                if 'a' in parte:
                    ma += 1
                if 'p' in parte:
                    mp += 1

    # Nvl-2: calidad formal - y nivel 2
    nvl_2 = df[(df['FQ'] == '-') & (df['Nivel'] == 2)].shape[0]

    # M-: M con calidad formal -
    m_menos = 0
    for fila in df[['Det', 'FQ']].dropna().itertuples():
        det = str(fila.Det)
        partes = det.split('.')
        for parte in partes:
            if parte.startswith('M') and str(fila.FQ) == '-':
                m_menos += 1

    # MQsin: M con calidad formal vacía o no codificada
    m_qsin = 0
    for fila in df[['Det', 'FQ']].dropna().itertuples():
        det = str(fila.Det)
        partes = det.split('.')
        for parte in partes:
            if parte.startswith('M') and str(fila.FQ) == 'sin':
                m_qsin += 1

    return {
        "a:p": f"{dic_variables.get('a', 0)}:{dic_variables.get('p', 0)}",
        "Ma:Mp": f"{ma}:{mp}",
        "Ma": ma,
        "Mp": mp,
        "MQ-": m_menos,
        "MQsin": m_qsin,
        "Intelec": (
            2 * dic_variables.get("AB", 0) +
            dic_variables.get("Art", 0) +
            dic_variables.get("Ay", 0)
        ),
        "MOR": dic_variables.get("MOR", 0),
        "Nvl-2": nvl_2
    }
