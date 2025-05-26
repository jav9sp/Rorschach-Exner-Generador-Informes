

def calcular_mediacion(df):
    total_r = len(df)
    if total_r == 0:
        return {k: 0 for k in ["XA%", "WDA%", "X-%", "S-", "Populares", "X+%", "Xu%"]}

    # Normalizar columnas para evitar errores
    df = df.copy()
    df["FQ"] = df["FQ"].astype(str).str.strip()
    df["Loc"] = df["Loc"].astype(str).str.strip().str.upper()

    # XA%: FQ en + o o u / total
    fq_xa = df["FQ"].isin(["+", "o", "u"]).sum()
    xa_pct = round(fq_xa / total_r, 2)

    # WDA%: Loc W o D y FQ en + o o u
    wd_mask = df["Loc"].isin(["W", "D"])
    fq_valid = df["FQ"].isin(["+", "o", "u"])
    fq_wda = df[wd_mask & fq_valid].shape[0]
    total_wd = df[wd_mask].shape[0]
    wda_pct = round(fq_wda / total_wd, 2) if total_wd != 0 else 0

    # X-%: FQ == '-' / total
    x_neg_pct = round((df["FQ"] == "-").sum() / total_r, 2) or 0

    # X+%: FQ == '+' o 'o'
    x_pos_pct = round(df["FQ"].isin(["+", "o"]).sum() / total_r, 2) or 0

    # XU%: FQ == 'u'
    xu_pct = round((df["FQ"] == "u").sum() / total_r, 2) or 0

    # S-: Loc contiene S y FQ == '-'
    s_neg = df[df["Loc"].str.contains("S") & (df["FQ"] == "-")].shape[0] or 0

    # P: respuestas populares
    p = (df["Populares"].astype(str).str.lower() == "p").sum() or 0

    return {
        "XA%": float(xa_pct),
        "WDA%": float(wda_pct),
        "X+%": float(x_pos_pct),
        "Xu%": float(xu_pct),
        "X-%": float(x_neg_pct),
        "S-": s_neg,
        "S-%": "[PENDIENTE]",
        "Populares": p,
    }
