
from typing import Literal

from contadores.determinantes import contar_determinantes
from contadores.puntaje_z import calcular_zscore
from contadores.calidad_evolutiva import contar_calidad_dq
from contadores.calidad_formal import contar_calidad_fq
from contadores.localizacion import contar_localizaciones
from contadores.contenidos import contar_contenidos_completos

from utils.contar_valores_coma import contar_valores_coma

from sumario_estructural.ideacion import calcular_codigos_especiales, calcular_indicadores_ideacion
from sumario_estructural.basicos import calcular_r, calcular_lambda, calcular_dets_resumidos
from sumario_estructural.dscore_adjes_adjd import calcular_adj_es, calcular_adj_d, calcular_dscore
from sumario_estructural.eb import calcular_eb_ea_ebper, calcular_eb_ratio_es
from sumario_estructural.afectos import calcular_afectos, calcular_estilo_vivencial
from sumario_estructural.interpersonal import calcular_interpersonal
from sumario_estructural.mediacion import calcular_mediacion
from sumario_estructural.procesamiento import calcular_procesamiento
from sumario_estructural.autopercepcion import calcular_autopercepcion

from constelaciones.generar_constelaciones import generar_constelaciones

Genero = Literal["M", "F"]


def generar_variables(df_respuestas, edad, genero: Genero):
    variables = {}

    variables["Edad"] = edad
    variables["Genero"] = genero

    # Localizaciones
    conteo_loc = contar_localizaciones(df_respuestas['Loc'])
    variables.update(conteo_loc)

    # Calidad Evolutiva
    conteo_dq = contar_calidad_dq(df_respuestas['DQ'])
    variables.update(conteo_dq)

    # Determinantes y subíndices
    resumen_determinantes, resumen_subindices, categorias = contar_determinantes(
        df_respuestas['Det'], df_respuestas['FQ'])
    variables.update(resumen_determinantes)
    variables.update(resumen_subindices)
    variables.update(categorias)

    # Calidad Formal, Contenidos, Fenómenos Especiales
    resumen_calidad_fq = contar_calidad_fq(df_respuestas['FQ'])
    variables.update(resumen_calidad_fq)
    variables.update(contar_contenidos_completos(df_respuestas['Contenidos']))
    variables.update(contar_valores_coma(df_respuestas['CC.EE.']))

    # Puntaje Z
    variables.update(calcular_zscore(df_respuestas['Lam'], df_respuestas['Z']))

    # Códigos especiales
    variables.update(calcular_codigos_especiales(variables))

    # Sumario Estructural Principal
    variables.update(calcular_r(df_respuestas))
    variables.update(calcular_lambda(df_respuestas, resumen_determinantes))
    variables.update(calcular_dets_resumidos(resumen_determinantes))
    variables.update(calcular_eb_ratio_es(variables, variables))
    variables.update(calcular_eb_ea_ebper(variables, variables['Lambda']))

    estilo = calcular_estilo_vivencial(
        variables['EB'], variables['EA'])
    variables['Tipo Vivencial'] = estilo

    variables['PuntD'] = calcular_dscore(variables['EA-es'])
    variables['Adjes'] = calcular_adj_es(variables)
    variables['AdjD'] = calcular_adj_d(variables['EA'], variables['Adjes'])

    # Índices estructurales secundarios
    variables.update(calcular_afectos(df_respuestas, variables))
    variables.update(calcular_interpersonal(variables))
    variables.update(calcular_indicadores_ideacion(df_respuestas, variables))
    variables.update(calcular_mediacion(df_respuestas))
    variables.update(calcular_procesamiento(df_respuestas, variables))
    variables.update(calcular_autopercepcion(df_respuestas, variables))

    # Constelaciones
    variables.update(generar_constelaciones(variables, edad))

    return variables
