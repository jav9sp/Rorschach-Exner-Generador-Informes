
def calcular_procesamiento(df, dic_variables):

    # W:D:Dd usando la función contar_localizaciones
    wdd_ratio = f"{dic_variables.get('W')}:{dic_variables.get('D')}:{dic_variables.get('Dd')}"

    # W:M
    total_w = dic_variables.get('W')
    total_m = 0
    for d in df['Det'].dropna():
        total_m += sum(1 for part in str(d).split('.') if part.startswith('M'))
    wm_ratio = f"{total_w}:{total_m}"

    # Zd = Zsum - Zest
    zf = dic_variables.get("Zf", 0)
    zd = dic_variables.get("Zd", 0)

    # PSV
    psv = dic_variables.get("PSV", 0)

    # DQ+
    dq_plus = df[df['DQ'] == '+'].shape[0]

    # DQv
    dq_v = df[df['DQ'] == 'v'].shape[0]

    return {
        "Zf": zf,
        "W:D:Dd": wdd_ratio,
        "W:M": wm_ratio,
        "Zd": zd,
        "PSV": psv,
        "DQ+": dq_plus,
        "DQv": dq_v
    }
