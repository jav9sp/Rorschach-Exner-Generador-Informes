
def contar_localizaciones(columna):
    """
    Cuenta la frecuencia de localizaciones W, D, Dd, S y calcula W+D.
    """
    conteo_loc = {'W': 0, 'D': 0, 'W+D': 0, 'Dd': 0, 'S': 0}

    for loc in columna.dropna():
        loc = str(loc).upper()
        if 'S' in loc:
            conteo_loc['S'] += 1
        if 'W' in loc:
            conteo_loc['W'] += 1
        if 'DD' in loc:
            conteo_loc['Dd'] += 1
        elif 'D' in loc and 'DD' not in loc:
            conteo_loc['D'] += 1

    conteo_loc['W+D'] = conteo_loc['W'] + conteo_loc['D']
    return conteo_loc
