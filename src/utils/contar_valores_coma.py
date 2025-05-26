
def contar_valores_coma(columna):
    """
    Cuenta valores separados por coma dentro de una columna de respuestas.
    """
    conteo = {}
    for entrada in columna.dropna():
        for valor in str(entrada).split(','):
            valor = valor.strip()
            if valor:
                conteo[valor] = conteo.get(valor, 0) + 1
    return conteo
