
def clasificar_afr_por_edad(afr_valor, edad):
    """
    Clasifica el valor de Afr según los rangos de edad.
    """
    if 5 <= edad <= 6:
        return "Bajo" if afr_valor < 0.57 else "Normal"
    elif 7 <= edad <= 9:
        return "Bajo" if afr_valor < 0.50 else "Normal"
    elif 10 <= edad <= 13:
        return "Bajo" if afr_valor < 0.53 else "Normal"
    else:
        return "No aplica ajuste por edad"
