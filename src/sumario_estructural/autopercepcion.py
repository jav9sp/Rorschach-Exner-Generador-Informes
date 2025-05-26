
def calcular_autopercepcion(df, variables):
    r = len(df)

    # Fr+rF determinantes
    fr_rf = 0
    for d in df['Det'].dropna():
        fr_rf += sum(1 for v in str(d).split('.') if v in ['Fr', 'rF'])

    # Respuestas pares
    pares = df[df['Par'] == 2].shape[0]

    # I.Egoc
    i_egoc = round((3 * fr_rf + pares) / r, 2)

    return {
        "Ego": i_egoc,
        "Fr+rF": fr_rf,
        "SumV": sum(variables.get(k, 0) for k in ['FV', 'VF', 'V']),
        "Fd": variables.get('Fd', 0),
        "An+Xy": variables.get('An', 0) + variables.get('Xy', 0),
        "MOR": variables.get('MOR', 0),
        "H:(H)+Hd+(Hd)": f"{variables.get('H', 0)}:{variables.get('(H)', 0) + variables.get('Hd', 0) + variables.get('(Hd)', 0)}",
        "Pares": pares
    }
