def calcular_interpersonal(dic_variables):
    r_total = dic_variables.get("R", 0)

    # COP : AG
    cop = dic_variables.get("COP", 0)
    ag = dic_variables.get("AG", 0)
    cop_vs_ag = f"{cop}:{ag}"

    # GHR : PHR
    ghr = dic_variables.get("GHR", 0)
    phr = dic_variables.get("PHR", 0)
    ghr_vs_phr = f"{ghr}:{phr}"

    # a : p
    a = dic_variables.get("a", 0)
    p = dic_variables.get("p", 0)
    a_vs_p = f"{a}:{p}"

    # Fd
    fd = dic_variables.get("Fd", 0)

    # SumT
    sumt = dic_variables.get(
        "FT", 0) + dic_variables.get("TF", 0) + dic_variables.get("T", 0)

    # H total: H, Hd, (H), (Hd)
    h_total = sum(dic_variables.get(k, 0)
                  for k in ["H", "Hd", "(H)", "(Hd)"])

    # H pura
    h_pura = dic_variables.get("H", 0)

    # Hx
    hx = dic_variables.get("Hx", 0)

    # PER
    per = dic_variables.get("PER", 0)

    # Aisl/R: (Bt + Ge + Ls + 2*(Cl + Na)) / R
    numerador = (
        dic_variables.get("Bt", 0) +
        dic_variables.get("Ge", 0) +
        dic_variables.get("Ls", 0) +
        2 * (dic_variables.get("Cl", 0) + dic_variables.get("Na", 0))
    )
    aisl_vs_r = round(numerador / r_total, 2) if r_total != 0 else 0

    return {
        "COP:AG": cop_vs_ag,
        "COP": cop,
        "AG": ag,
        "GHR": ghr,
        "PHR": phr,
        "GHR:PHR": ghr_vs_phr,
        "a:p": a_vs_p,
        "Fd": fd,
        "SumT": sumt,
        "TodoH": h_total,
        "H": h_pura,
        "Hx": hx,
        "PER": per,
        "Aisl/R": aisl_vs_r
    }
