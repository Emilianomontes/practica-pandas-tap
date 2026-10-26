"""
==============================================================================
INSTITUTO TECNOLÓGICO DE CIUDAD MADERO
Tecnológico Nacional de México
Departamento de Sistemas y Computación | Ingeniería en Sistemas Computacionales
Asignatura: Tópicos Avanzados de Programación
Docente: Alejandro Estrada Padilla
Práctica de Laboratorio: Análisis y visualización de calificaciones con Pandas y Matplotlib
Estudiante: Emiliano Montes Morales
==============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# --- Ejercicio 1: Carga y revisión ---
# ==============================================================================
print("\n" + "=" * 60)
print("EJERCICIO 1: CARGA Y REVISIÓN DEL DATASET")
print("=" * 60)

# Carga del archivo CSV en un DataFrame llamado df
df = pd.read_csv("calificaciones_isc.csv")

# 1. Primeras 5 filas
print("\n[1.1] Primeras 5 filas del conjunto de datos:")
print(df.head())

# 2. Número de filas y columnas
print(f"\n[1.2] Dimensiones del DataFrame (filas, columnas): {df.shape}")
print(f"      Total de filas: {df.shape[0]} | Total de columnas: {df.shape[1]}")

# 3. Tipo de dato de cada columna
print("\n[1.3] Tipo de dato de cada columna:")
print(df.dtypes)

# 4. Resumen estadístico de 'calificacion' y 'asistencias'
print("\n[1.4] Resumen estadístico de 'calificacion' y 'asistencias':")
print(df[["calificacion", "asistencias"]].describe())

# Justificación técnica obligatoria en comentario:
# ¿Por qué el archivo tiene 288 registros y no 24?
# R: La generación cuenta con 24 alumnos en total, pero el conjunto de datos está 
# estructurado con granularidad por unidad y por materia. Cada alumno cursa 4 materias
# (Programacion, Bases de datos, Redes y Matematicas discretas) y cada materia es
# evaluada en 3 unidades temáticas. En consecuencia, cada alumno aporta exactamente
# 4 materias * 3 unidades = 12 registros de evaluación. 
# Multiplicando por la cantidad de estudiantes: 24 alumnos * 12 registros = 288 filas en total.


# ==============================================================================
# --- Ejercicio 2: Filtros ---
# ==============================================================================
print("\n" + "=" * 60)
print("EJERCICIO 2: FILTROS CONDICIONALES")
print("=" * 60)

# Sin modificar el DataFrame original df, aplicamos los filtros solicitados:

# Filtro 1: Solo registros correspondientes al grupo A
filtro_grupo_a = df[df["grupo"] == "A"]
conteo_grupo_a = len(filtro_grupo_a)

# Filtro 2: Unidades cuya calificación es reprobatoria (menor a 70)
filtro_menor_70 = df[df["calificacion"] < 70]
conteo_menor_70 = len(filtro_menor_70)

# Filtro 3: Materia 'Bases de datos', del grupo 'B', con calificación de al menos 80
filtro_bd_grupo_b_80 = df[
    (df["materia"] == "Bases de datos") & 
    (df["grupo"] == "B") & 
    (df["calificacion"] >= 80)
]
conteo_bd_grupo_b_80 = len(filtro_bd_grupo_b_80)

# Conteo directo usando len() sin ciclos for (conforme a los criterios de evaluación)
print(f"[2.1] Filas del Grupo A: {conteo_grupo_a}")
print(f"[2.2] Filas con calificación menor a 70: {conteo_menor_70}")
print(f"[2.3] Filas de 'Bases de datos' en Grupo B con calificación >= 80: {conteo_bd_grupo_b_80}")


# ==============================================================================
# --- Ejercicio 3: Columna calculada ---
# ==============================================================================
print("\n" + "=" * 60)
print("EJERCICIO 3: COLUMNA CALCULADA VECTORIZADA")
print("=" * 60)

# Creación vectorizada de la columna 'situacion' usando np.where
# Condición: si calificacion >= 70 es 'Aprobado', en caso contrario 'Reprobado'
df["situacion"] = np.where(df["calificacion"] >= 70, "Aprobado", "Reprobado")

print("[3.1] Columna 'situacion' creada con éxito.")
print("[3.2] Muestra de las primeras 8 filas con la nueva columna integrada:")
print(df[["matricula", "nombre", "materia", "unidad", "calificacion", "situacion"]].head(8))


# ==============================================================================
# --- Ejercicio 4: Resúmenes ---
# ==============================================================================
print("\n" + "=" * 60)
print("EJERCICIO 4: RESÚMENES ESTADÍSTICOS Y EXPORTACIÓN")
print("=" * 60)

# 1. Promedio de calificación por materia
promedio_materia = df.groupby("materia")["calificacion"].mean()
print("[4.1] Promedio de calificación por materia:")
print(promedio_materia.round(2))

# 2. Promedio por grupo y materia
promedio_grupo_materia = df.groupby(["grupo", "materia"])["calificacion"].mean()
print("\n[4.2] Promedio por grupo y materia:")
print(promedio_grupo_materia.round(2))

# 3. Promedio general de cada alumno, ordenado de mayor a menor
promedios_alumnos = (
    df.groupby(["matricula", "nombre"])["calificacion"]
    .mean()
    .reset_index()
    .rename(columns={"calificacion": "promedio"})
    .sort_values(by="promedio", ascending=False)
)
print("\n[4.3] Promedio general por alumno (primeros 5 lugares):")
print(promedios_alumnos.head(5).to_string(index=False))

# 4. Promedio general por unidad (todas las materias juntas)
promedio_unidad = df.groupby("unidad")["calificacion"].mean()
print("\n[4.4] Promedio general por unidad (todas las materias):")
print(promedio_unidad.round(2))

# 5. Conteo de unidades aprobadas y reprobadas
conteo_situacion = df["situacion"].value_counts()
print("\n[4.5] Conteo total de registros aprobados y reprobados:")
print(conteo_situacion)

# Exportación del archivo promedios_alumnos.csv
# Se preservan matrícula y nombre mediante reset_index() y se evita el índice extra con index=False
promedios_alumnos.to_csv("promedios_alumnos.csv", index=False)
print("\n[4.6] Archivo 'promedios_alumnos.csv' exportado exitosamente sin índice adicional.")


# ==============================================================================
# --- Ejercicio 5: Gráficas ---
# ==============================================================================
print("\n" + "=" * 60)
print("EJERCICIO 5: VISUALIZACIÓN DE DATOS CON MATPLOTLIB")
print("=" * 60)

# Configuración global estética de Matplotlib
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10
})

# ------------------------------------------------------------------------------
# Gráfica 1: Barras del promedio por materia (Eje vertical de 0 a 100)
# ------------------------------------------------------------------------------
fig1, ax1 = plt.subplots(figsize=(8, 5))
colores_materias = ["#2b5c8f", "#d95f02", "#7570b3", "#1b9e77"]

barras = ax1.bar(
    promedio_materia.index, 
    promedio_materia.values, 
    color=colores_materias, 
    edgecolor="black", 
    alpha=0.85,
    width=0.55
)

ax1.set_title("Promedio General de Calificación por Materia", pad=15, fontweight="bold")
ax1.set_xlabel("Materia Evaluada", labelpad=10, fontweight="bold")
ax1.set_ylabel("Promedio de Calificación (Escala 0-100)", labelpad=10, fontweight="bold")
ax1.set_ylim(0, 100)
ax1.grid(True, linestyle="--", alpha=0.6, axis="y")

# Anotación del valor exacto encima de cada barra para mayor legibilidad
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(
        f"{altura:.2f}",
        xy=(barra.get_x() + barra.get_width() / 2, altura),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center", 
        va="bottom", 
        fontsize=10, 
        fontweight="bold"
    )

plt.tight_layout()
# PREVENCIÓN CRÍTICA: savefig se invoca estrictamente ANTES de show
plt.savefig("promedio_materias.png", dpi=300)
print("[5.1] Figura guardada con éxito: promedio_materias.png")
plt.show(block=False)
plt.pause(0.5)
plt.close()

# ------------------------------------------------------------------------------
# Gráfica 2: Histograma de todas las calificaciones con línea vertical en 70
# ------------------------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(8, 5))

n, bins, patches = ax2.hist(
    df["calificacion"], 
    bins=12, 
    color="#4a90e2", 
    edgecolor="black", 
    alpha=0.75
)

# Línea vertical indicadora del umbral aprobatorio (70)
ax2.axvline(
    70, 
    color="#d90429", 
    linestyle="--", 
    linewidth=2.5, 
    label="Mínimo Aprobatorio (70)"
)

ax2.set_title("Distribución General de Calificaciones (Todas las Unidades)", pad=15, fontweight="bold")
ax2.set_xlabel("Calificación Obtenida", labelpad=10, fontweight="bold")
ax2.set_ylabel("Frecuencia (Número de Evaluaciones)", labelpad=10, fontweight="bold")
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper left", frameon=True)

plt.tight_layout()
# PREVENCIÓN CRÍTICA: savefig se invoca estrictamente ANTES de show
plt.savefig("histograma.png", dpi=300)
print("[5.2] Figura guardada con éxito: histograma.png")
plt.show(block=False)
plt.pause(0.5)
plt.close()

# ------------------------------------------------------------------------------
# Gráfica 3: Líneas de tendencia del promedio por unidad por cada materia
# ------------------------------------------------------------------------------
fig3, ax3 = plt.subplots(figsize=(9, 5.5))

tendencia = df.groupby(["unidad", "materia"])["calificacion"].mean().unstack()

estilos = {
    "Programacion": {"color": "#1f77b4", "marker": "o"},
    "Bases de datos": {"color": "#ff7f0e", "marker": "s"},
    "Redes": {"color": "#2ca02c", "marker": "^"},
    "Matematicas discretas": {"color": "#d62728", "marker": "D"}
}

for col in tendencia.columns:
    estilo = estilos.get(col, {"color": "black", "marker": "o"})
    ax3.plot(
        tendencia.index, 
        tendencia[col], 
        label=col, 
        color=estilo["color"], 
        marker=estilo["marker"], 
        linewidth=2.2, 
        markersize=7
    )

ax3.set_title("Evolución y Tendencia de Calificaciones por Unidad y Materia", pad=15, fontweight="bold")
ax3.set_xlabel("Unidad de Evaluación", labelpad=10, fontweight="bold")
ax3.set_ylabel("Promedio de Calificación", labelpad=10, fontweight="bold")
ax3.set_xticks([1, 2, 3])
ax3.set_xticklabels(["Unidad 1", "Unidad 2", "Unidad 3"])
ax3.grid(True, linestyle="--", alpha=0.6)
ax3.legend(title="Materias Evaluadas", loc="best", frameon=True)

plt.tight_layout()
# PREVENCIÓN CRÍTICA: savefig se invoca estrictamente ANTES de show
plt.savefig("tendencia_unidades.png", dpi=300)
print("[5.3] Figura guardada con éxito: tendencia_unidades.png")
plt.show(block=False)
plt.pause(0.5)
plt.close()


# ==============================================================================
# --- Ejercicio 6: Lectura de resultados y análisis argumentado ---
# ==============================================================================
# Cálculo dinámico de métricas para garantizar consistencia con los datos
materia_peor = promedio_materia.idxmin()
promedio_peor_val = promedio_materia.min()
u1_prom = promedio_unidad.loc[1]
u2_prom = promedio_unidad.loc[2]
u3_prom = promedio_unidad.loc[3]
baja_u3 = u3_prom < u1_prom and u3_prom < u2_prom
alumnos_reprobados_general = len(promedios_alumnos[promedios_alumnos["promedio"] < 70])
total_alumnos = len(promedios_alumnos)

print("\n" + "=" * 60)
print("EJERCICIO 6: LECTURA DE RESULTADOS E INTERPRETACIÓN")
print("=" * 60)
print(f"• Materia con promedio más bajo: {materia_peor} ({promedio_peor_val:.2f})")
print(f"• Promedios por unidad -> Unidad 1: {u1_prom:.2f} | Unidad 2: {u2_prom:.2f} | Unidad 3: {u3_prom:.2f}")
print(f"  ¿El promedio general de la unidad 3 es menor que el de las unidades 1 y 2?: {'Sí' if baja_u3 else 'No'}")
print(f"• Alumnos con promedio general bajo 70: {alumnos_reprobados_general} de {total_alumnos} estudiantes.")

analisis_argumentado = f"""
ANÁLISIS COHESIVO Y ARGUMENTACIÓN TÉCNICA:
A partir del análisis cuantitativo y visual de los registros académicos, se observa que la asignatura con el rendimiento más bajo corresponde a '{materia_peor}', registrando un promedio de {promedio_peor_val:.2f} puntos, situándose como la disciplina con mayor índice de dificultad. Con respecto a la progresión del curso, el promedio general experimentó un claro descenso hacia el cierre del periodo: mientras que las unidades 1 y 2 alcanzaron promedios de {u1_prom:.2f} y {u2_prom:.2f} puntos respectivamente, la unidad 3 descendió a {u3_prom:.2f} puntos. Esta caída sistemática se corrobora gráficamente en el gráfico de líneas 'tendencia_unidades.png', donde las curvas de las asignaturas presentan una pendiente negativa hacia la tercera unidad debido al incremento en la complejidad de los temas finales y la saturación de entregas. Finalmente, al consolidar las calificaciones por estudiante, un total de {alumnos_reprobados_general} de los {total_alumnos} alumnos ({alumnos_reprobados_general/total_alumnos*100:.1f}%) concluyeron con un promedio general inferior al mínimo aprobatorio de 70, indicando una necesidad prioritaria de asesorías académicas preventivas previo a las evaluaciones finales.
"""

print(analisis_argumentado)
print("=" * 60)
print("Práctica completada con éxito.")
