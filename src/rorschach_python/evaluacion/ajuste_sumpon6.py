
def clasificar_sumpon6_por_edad(sumpon6, edad, r):
    """
    Clasifica el valor de SumPon6 como alto o no significativo según edad y R.
    """
    if r >= 17:
        if 5 <= edad <= 7:
            return "Alto" if sumpon6 > 20 else "No significativo"
        elif 8 <= edad <= 10:
            return "Alto" if sumpon6 > 19 else "No significativo"
        elif 11 <= edad <= 13:
            return "Alto" if sumpon6 > 18 else "No significativo"
    else:
        if 5 <= edad <= 7:
            return "Alto" if sumpon6 > 16 else "No significativo"
        elif 8 <= edad <= 10:
            return "Alto" if sumpon6 > 15 else "No significativo"
        elif 11 <= edad <= 13:
            return "Alto" if sumpon6 > 14 else "No significativo"

    return "No aplica ajuste por edad"
