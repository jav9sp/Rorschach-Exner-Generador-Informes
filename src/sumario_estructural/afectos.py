
def calcular_afectos(df, variables):
    r_total = len(df)

    # FC : CF+C+Cn
    fc = variables.get("FC", 0)
    cf = variables.get("CF", 0)
    c_pura = variables.get("C", 0)
    cn = variables.get("Cn", 0)
    total_c = fc + cf + c_pura + cn
    fc_vs_otros = f"{fc}:{cf + c_pura + cn}"

    # C pura
    c_pura = sum(1 for d in df["Det"].dropna() if d.strip() == "C")

    # SumC':SumPonC
    sumcprima = variables.get(
        "FC'", 0) + variables.get("C'F", 0) + variables.get("C'", 0)
    sumponc = calcular_sumponc(fc, cf, c_pura)
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
    respuestas_complejas = df["Det"].dropna().str.contains(r'\.').sum() or 0
    complj_vs_r = f"{respuestas_complejas}:{r_total}"

    # CP
    cp = variables.get("CP", 0)

    # CompljsColSH y CompljsSH
    col_det = {"FC", "CF", "C"}
    sh_det = {"FC'", "C'F", "C'", "FV", "VF", "V", "FT", "TF", "T"}
    sit_det = {"FY", "YF", "Y"}
    tot_sh_det = sh_det.union(sit_det)
    mov_det = {"m"}

    complj_col_sh = 0
    complj_col_y = 0
    complj_sh_sh = 0
    complj_sh_y = 0
    complj_mov = 0
    sum_sh = sum(variables.get(det, 0) for det in sh_det)

    for det in df["Det"].dropna():
        partes = [p.strip() for p in str(det).split('.')]
        if len(partes) < 2:
            continue

        tiene_color = any(p in col_det for p in partes)
        tiene_sombreado = any(p in tot_sh_det for p in partes)
        tiene_situacional = any(p in sit_det for p in partes)
        tiene_movimiento = any(p in mov_det for p in partes)
        total_sombreado = sum(1 for p in partes if p in tot_sh_det)

        # NOTA: Una misma respuesta puede contabilizarse en más de una categoría de complejidad.
        # Esto es intencional, ya que pueden coexistir componentes (color + sombreado + situacional, etc.)
        if tiene_color and tiene_situacional:
            complj_col_sh += 1
            complj_col_y += 1
        if total_sombreado >= 2 and tiene_situacional:
            complj_sh_sh += 1
            complj_sh_y += 1
        if tiene_color and tiene_sombreado:
            complj_col_sh += 1
        if total_sombreado >= 2:
            complj_sh_sh += 1
        if tiene_movimiento:
            complj_mov += 1

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
        "CompljsSit/R": complj_sh_y / respuestas_complejas if respuestas_complejas else 0,
        "CompljsColSH": complj_col_sh,
        "CompljsColY": complj_col_y,
        "CompljsSHY": complj_sh_y,
        "CompljsSH": complj_sh_sh,
        "CompljsMov": complj_mov,
        "SumSH": sum_sh
    }


def calcular_sumponc(fc, cf, c_pura):
    """Calcula SumPonC: 0.5*FC + 1.0*CF + 1.5*C"""
    return (0.5 * fc + 1.0 * cf + 1.5 * c_pura)


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
