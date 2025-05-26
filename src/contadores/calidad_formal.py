
def contar_calidad_fq(columna):
    """
    Cuenta la frecuencia de cada código FQ: +, o, u, -, sin.
    Devuelve claves con prefijo FQ.
    """
    claves = {'+': 'FQx+', 'o': 'FQxo',
              'u': 'FQxu', '-': 'FQx-', 'sin': 'FQxsin'}
    conteo = {v: 0 for v in claves.values()}

    for fq in columna.dropna():
        fq = str(fq).lower().strip()
        if fq in claves:
            conteo[claves[fq]] += 1
    return conteo
