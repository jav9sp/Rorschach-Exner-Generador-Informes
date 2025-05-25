def unir_interpretaciones(lista):
    if not lista:
        return ""
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        return f"{lista[0]} y {lista[1]}"
    else:
        return ", ".join(lista[:-1]) + f" y {lista[-1]}"
