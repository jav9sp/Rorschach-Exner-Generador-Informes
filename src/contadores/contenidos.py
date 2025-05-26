
CONTENIDOS_POSIBLES = [
    "H", "(H)", "Hd", "(Hd)", "Hx", "A", "(A)", "Ad", "(Ad)",
    "An", "Art", "Ay", "Bl", "Bt", "Cg", "Cl", "Ex", "Fi",
    "Fd", "Ge", "Hh", "Ls", "Na", "Sc", "Sx", "Xy", "Idio"
]


def contar_contenidos_completos(columna):
    conteo = {contenido: 0 for contenido in CONTENIDOS_POSIBLES}
    for entrada in columna.dropna():
        for valor in str(entrada).split(','):
            valor = valor.strip()
            if valor in conteo:
                conteo[valor] += 1
    return conteo
