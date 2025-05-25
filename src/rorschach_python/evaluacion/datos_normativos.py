import pandas as pd
import json

# Rutas a los archivos normativos JSON
RUTAS_ESTILOS = {
    "Extroversivo": "data/muestraExtroRo.json",
    "Introversivo": "data/muestraIntroRo.json",
    "Ambigual": "data/muestraAmbigualRo.json",
    "Indefinido": "data/muestraTotalRo.json",
    "Total": "data/muestraTotalRo.json",
    "15 Años": "data/muestra15Anios.json",
    "14 Años": "data/muestra14Anios.json"
}


def obtener_tabla_por_estilo(estilo, edad):
    """
    Carga y devuelve el DataFrame de normativa correspondiente al estilo vivencial.
    Si es menor a 17 años devuelve tabla según edad.
    """

    if edad > 16:
        if estilo not in RUTAS_ESTILOS:
            raise ValueError(f"Estilo no reconocido: {estilo}")

        ruta = RUTAS_ESTILOS[estilo]
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        print(f"Cargada tabla {estilo}")
        return pd.DataFrame(datos)

    if edad == 15:
        ruta = RUTAS_ESTILOS["15 Años"]
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        print("Cargada tabla de 15 años")
        return pd.DataFrame(datos)

    if edad == 15:
        ruta = RUTAS_ESTILOS["14 Años"]
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        print("Cargada tabla de 14 años")
        return pd.DataFrame(datos)


def comparar_con_normativa(resultados, tabla):
    """
    Compara los resultados del evaluado con media y desviación estándar (columna DT).
    Devuelve un DataFrame con VARIABLE, MEDIA, DT, VALOR, COMPARACIÓN.
    """
    comparaciones = []

    for _, row in tabla.iterrows():
        variable = row.get('VARIABLE', '<desconocida>')
        # Leer media y DT (limpiando corchetes)
        try:
            media = float(str(row['MEDIA']).replace(',', '.'))
            dt_raw = str(row['DT']).replace(',', '.').strip('[]')
            dt = float(dt_raw)
        except ValueError:
            comparaciones.append((
                variable,
                row.get('MEDIA', '-'),
                row.get('DT', '-'),
                "-",
                "Datos normativos inválidos"
            ))
            continue

        valor = resultados.get(variable, None)

        if valor is None:
            estado = "No disponible"
        else:
            # Intentamos convertir a float: acepta ints, numpy types, strings numéricas...
            try:
                valor_num = float(valor)
            except ValueError:
                estado = "Tipo no numérico"
            else:
                # cuántas SDs de distancia sobre/ bajo la media
                diff = valor_num - media
                sd_units = diff / dt if dt != 0 else 0

                if abs(sd_units) <= 1:
                    estado = "Dentro del rango"
                elif abs(sd_units) <= 2:
                    estado = ("Levemente por encima" if sd_units > 0
                              else "Levemente por debajo")
                else:
                    estado = ("Marcadamente por encima" if sd_units > 0
                              else "Marcadamente por debajo")

        comparaciones.append((
            variable,
            media,
            dt,
            valor,
            estado
        ))

    return pd.DataFrame(
        comparaciones,
        columns=["VARIABLE", "MEDIA", "DT", "VALOR", "COMPARACIÓN"]
    )
