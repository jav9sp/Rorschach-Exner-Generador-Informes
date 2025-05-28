
def calcular_afectos(df, variables):
    r_total = len(df)

    # FC : CF+C+Cn
    fc = variables.get("FC", 0)
    cf = variables.get("CF", 0)
    c = variables.get("C", 0)
    cn = variables.get("Cn", 0)
    total_c = fc + cf + c + cn
    fc_vs_otros = f"{fc}:{cf + c + cn}"

    # C pura
    c_pura = sum(1 for d in df["Det"].dropna() if d.strip() == "C")

    # SumC':SumPonC
    sumcprima = variables.get(
        "FC'", 0) + variables.get("C'F", 0) + variables.get("C'", 0)
    sumponc = calcular_sumponc(variables)["SumPonC"]
    sumc_vs_sumponc = f"{sumcprima}:{sumponc}"

    # Afr
    laminas_afr = df[df["Lam"].isin(
        ["viii", "ix", "x", "VIII", "IX", "X"])].shape[0]
    otras_laminas = r_total - \
        laminas_afr if (r_total - laminas_afr) != 0 else 1
    afr = round(laminas_afr / otras_laminas, 2)

    # S
    total_s = sum(1 for loc in df["Loc"].dropna() if "S" in str(loc).upper())

    # Complj:R
    respuestas_complejas = df["Det"].dropna().apply(
        lambda d: "." in str(d)).sum() or 0
    complj_vs_r = f"{respuestas_complejas}:{r_total}"

    # CP
    cp = variables.get("CP", 0)

    # CompljsColSH y CompljsSH
    col_det = {"FC", "CF", "C"}
    sh_det = {"FC'", "C'F", "C'", "FY", "YF",
              "Y", "FV", "VF", "V", "FT", "TF", "T"}

    complj_colsh = 0
    complj_sh = 0
    sum_sh = sum(variables.get(det, 0) for det in sh_det)

    for det in df["Det"].dropna():
        partes = [p.strip() for p in str(det).split('.')]
        if len(partes) < 2:
            continue

        tiene_color = any(p in col_det for p in partes)
        tiene_sombreado = any(p in sh_det for p in partes)
        total_sombreado = sum(1 for p in partes if p in sh_det)

        if tiene_color and tiene_sombreado:
            complj_colsh += 1
        if total_sombreado >= 2:
            complj_sh += 1

    return {
        "FC:CF+C+Cn": fc_vs_otros,
        "C Pura": c_pura,
        "SumC':SumPonC": sumc_vs_sumponc,
        "Afr": afr,
        "S": total_s,
        "Complj:R": complj_vs_r,
        "CP": cp,
        "SumPonC": sumponc,
        "Cn": cn,
        "FC+CF+C+Cn": total_c,
        "Compljs": respuestas_complejas,
        "Compljs/R": round(respuestas_complejas / r_total, 2),
        "CompljsColSH": complj_colsh,
        "CompljsSH": complj_sh,
        "SumSH": sum_sh
    }


def calcular_sumponc(det_dict) -> dict:
    """Calcula SumPonC: 0.5*FC + 1.0*CF + 1.5*C"""
    return {
        "SumPonC": (
            0.5 * det_dict.get("FC", 0) +
            1.0 * det_dict.get("CF", 0) +
            1.5 * det_dict.get("C", 0))
    }


def calcular_estilo_vivencial(eb: str, ea: float) -> str:
    """
    Determina el estilo vivencial (Introversivo, Extroversivo, Ambigual, Indefinido)
    en base a la diferencia entre M y SumPonC en el EB, y al valor de EA.
    """
    try:
        m, c = map(float, eb.split(':'))
        diff = abs(m - c)

        if ea < 4 or m == 0 or c == 0:
            return "Indefinido"
        if diff < 2:
            return "Ambigual"
        elif m > c:
            return "Introversivo"
        else:
            return "Extroversivo"
    except ValueError:
        return "Error al calcular el Tipo Vivencial"
