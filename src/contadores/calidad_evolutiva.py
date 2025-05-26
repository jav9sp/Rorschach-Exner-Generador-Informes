
def contar_calidad_dq(columna):
    """
    Cuenta la frecuencia de cada código DQ: +, o, v/+, v.
    Devuelve claves con prefijo DQ.
    """
    claves = {'+': 'DQ+', 'o': 'DQo', 'v/+': 'DQv/+', 'v': 'DQv'}
    conteo = {v: 0 for v in claves.values()}

    for dq in columna.dropna():
        dq = str(dq).lower().strip()
        if dq in claves:
            conteo[claves[dq]] += 1
    return conteo
