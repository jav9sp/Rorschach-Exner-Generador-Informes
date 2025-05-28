
def calcular_eb_ratio_es(det_dict, dets_resumidos):
    """Calcula eb como FM+m : SumC'+SumT+SumY+SumV"""
    fm = det_dict.get("FM", 0)
    m = det_dict.get("m", 0)
    sum_sh = (
        dets_resumidos.get("SumC'", 0) +
        dets_resumidos.get("SumT", 0) +
        dets_resumidos.get("SumY", 0) +
        dets_resumidos.get("SumV", 0)
    )
    sum_sh = sum_sh if sum_sh != 0 else 1
    return {
        "eb": f"{fm + m}:{sum_sh}",
        "es": fm + m + sum_sh,
        "FM+m": fm + m
    }


def calcular_eb_ea_ebper(det_dict, lambda_val):
    """
    Calcula EB, EA (suma de ambos), y EBPer si aplica.
    """
    m = det_dict.get("M", 0)
    fc = det_dict.get("FC", 0)
    cf = det_dict.get("CF", 0)
    c = det_dict.get("C", 0)

    sumponc = 0.5 * fc + 1.0 * cf + 1.5 * c

    eb = f"{m} : {sumponc}"
    ea = m + sumponc

    estilo_definido = (
        ea >= 4 and lambda_val < 1 and
        ((ea <= 10 and abs(m - sumponc) >= 2)
         or (ea > 10 and abs(m - sumponc) >= 2.5))
    )

    ebper = round(m / sumponc, 2) if estilo_definido and sumponc != 0 else 0

    return {
        "EB": eb,
        "EA": ea,
        "EBPer": ebper,
        "EA-es": ea - det_dict.get("es", 0)
    }
