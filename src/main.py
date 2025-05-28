import pandas as pd

from informe.generar_variables import generar_variables
from informe.generador_word import generar_informe

from utils.simplificar_estado import simplificar_estado

from evaluacion.datos_normativos import obtener_tabla_por_estilo, comparar_con_normativa

from interpretaciones.estrategia_interpretacion import determinar_estrategia_interpretacion
from interpretaciones.area_preliminares import interpretar_preliminares
from interpretaciones.area_procesamiento import interpretar_procesamiento
from interpretaciones.area_mediacion import interpretar_mediacion
from interpretaciones.area_ideacion import interpretar_ideacion
from interpretaciones.area_afectos import interpretar_afectos
from interpretaciones.area_autopercepcion import interpretar_autopercepcion
from interpretaciones.area_interpersonal import interpretar_interpersonal
from interpretaciones.area_control_estres import interpretar_control_estres
from interpretaciones.area_situacional import interpretar_estres_situacional

# Cargar archivo Excel
df = pd.read_excel("protocolo_prueba.xlsx")

# ! Indicar la edad y género del evaluado
edad = 38
genero = "M"  # F para Femenino, M para Masculino

# Generar variables del protocolo
variables = generar_variables(df, edad, genero)

# Obtener y aplicar normativa según tipo vivencial
estilo = variables.get("Tipo Vivencial", "Indefinido")
tabla = obtener_tabla_por_estilo(estilo, edad)
df_norm = comparar_con_normativa(variables, tabla)

estados = {
    row.VARIABLE: row.COMPARACIÓN
    for _, row in df_norm.iterrows()
}

estados_simples = {var: simplificar_estado(
    est) for var, est in estados.items()}

# Llamada a interpretaciones
estrategia_interpretacion = determinar_estrategia_interpretacion(variables)
preliminares = interpretar_preliminares(variables, estados_simples)
procesamiento = interpretar_procesamiento(df, variables, estados_simples)
mediacion = interpretar_mediacion(variables, estados_simples)
ideacion = interpretar_ideacion(variables, estados_simples)
afectos = interpretar_afectos(variables, estados_simples)
autopercepcion = interpretar_autopercepcion(variables, estados_simples)
interpersonal = interpretar_interpersonal(variables, estados_simples)
control_estres = interpretar_control_estres(variables, estados_simples)
estres_situacional = interpretar_estres_situacional(variables, estados_simples)

# Generar informe Word
generar_informe("informe_prueba.docx", {
    "0. Secuencia de Interpretación": estrategia_interpretacion,
    "1. Aspectos Preliminares": preliminares,
    "2. Procesamiento de la Información": procesamiento,
    "3. Mediación Cognitiva": mediacion,
    "4. Ideación": ideacion,
    "5. Afectos": afectos,
    "6. Autopercepción": autopercepcion,
    "7. Percepción Interpersonal": interpersonal,
    "8. Control y Tolerancia al Estrés": control_estres,
    "9. Estrés Situacional": estres_situacional,
    "Comparación con Normativa": df_norm
})
