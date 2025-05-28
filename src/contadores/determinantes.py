
def contar_determinantes(columna_det, columna_fq):
    """
    Cuenta determinantes y subíndices de movimiento en las respuestas codificadas.
    Además, si hay M en la respuesta, clasifica según calidad formal (MQ+ MQo MQ- MQsin).
    """
    conteo_general = {"F": 0, "M": 0, "FM": 0, "m": 0,
                      "C": 0, "CF": 0, "FC": 0, "C'": 0, "C'F": 0, "FC'": 0,
                      "T": 0, "TF": 0, "FT": 0, "V": 0, "VF": 0, "FV": 0,
                      "Y": 0, "YF": 0, "FY": 0, "FD": 0, "rF": 0, "Fr": 0}
    conteo_subindices = {"a": 0, "p": 0}
    conteo_mq = {"MQ+": 0, "MQo": 0, "MQu": 0, "MQ-": 0, "MQsin": 0}

    for det, fq in zip(columna_det.dropna(), columna_fq.dropna()):
        tiene_m = False

        # Determinantes: detectar bases y sufijos
        for valor in str(det).split('.'):
            valor = valor.strip()
            if not valor:
                continue

            # Separar base y sufijo
            idx = min([valor.find(s) for s in ['ap', 'pa', 'a', 'p']
                      if s in valor] + [len(valor)])
            base = valor[:idx]
            sufijo = valor[idx:].lower()

            conteo_general[base] = conteo_general.get(base, 0) + 1

            if 'a' in sufijo:
                conteo_subindices['a'] += 1
            if 'p' in sufijo:
                conteo_subindices['p'] += 1

            if base == 'M':
                tiene_m = True

        # Evaluar calidad formal si hay M
        if tiene_m:
            fq = str(fq).lower().strip()
            if fq == '+':
                conteo_mq["MQ+"] += 1
            elif fq == 'o':
                conteo_mq["MQo"] += 1
            elif fq == 'u':
                conteo_mq["MQu"] += 1
            elif fq == '-':
                conteo_mq["MQ-"] += 1
            else:
                conteo_mq["MQsin"] += 1

    conteo_general.update(conteo_mq)
    return conteo_general, conteo_subindices
