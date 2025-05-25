
def calcular_r(df):
    """Cantidad total de respuestas (R)."""
    return {"R": len(df)}


def calcular_lambda(df, det_dict):
    """Calcula Lambda: F / (R - F)"""
    r = len(df)
    f_pura = det_dict.get("F", 0)
    no_f = r - f_pura if (r - f_pura) != 0 else 1
    return {"Lambda": round(f_pura / no_f, 2)}


def sumar_determinantes(det_dict, claves):
    """Suma total de apariciones para una lista de determinantes."""
    return sum(det_dict.get(k, 0) for k in claves)


def calcular_dets_resumidos(det_dict):
    """Calcula SumC', SumT, SumV, SumY desde los determinantes."""
    return {
        "SumC'": sumar_determinantes(det_dict, ["FC'", "C'F", "C'"]),
        "SumT":  sumar_determinantes(det_dict, ["FT", "TF", "T"]),
        "SumV":  sumar_determinantes(det_dict, ["FV", "VF", "V"]),
        "SumY":  sumar_determinantes(det_dict, ["FY", "YF", "Y"])
    }
