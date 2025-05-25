
def calcular_autopercepcion(df, dic_variables):
    r = len(df)

    # Fr+rF determinantes
    fr_rf = 0
    for d in df['Det'].dropna():
        fr_rf += sum(1 for v in str(d).split('.') if v in ['Fr', 'rF'])

    # Respuestas pares
    pares = df[df['Par'] == 2].shape[0]

    # I.Egoc
    i_egoc = round((3 * fr_rf + pares * 2) / r, 2) if r != 0 else 0

    return {
        "Ego": i_egoc,
        "Fr+rF": fr_rf,
        "SumV": sum(dic_variables.get(k, 0) for k in ['FV', 'VF', 'V']),
        "Fd": dic_variables.get('Fd', 0),
        "An+Xy": dic_variables.get('An', 0) + dic_variables.get('Xy', 0),
        "MOR": dic_variables.get('MOR', 0),
        "H:(H)+Hd+(Hd)": f"{dic_variables.get('H', 0)}:{dic_variables.get('(H)', 0) + dic_variables.get('Hd', 0) + dic_variables.get('(Hd)', 0)}",
        "Pares": pares
    }
