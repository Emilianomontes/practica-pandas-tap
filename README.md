# Práctica de Laboratorio: Análisis y Visualización de Calificaciones con Pandas y Matplotlib

**Tecnológico Nacional de México | Instituto Tecnológico de Ciudad Madero**  
**Departamento:** Sistemas y Computación  
**Carrera:** Ingeniería en Sistemas Computacionales  
**Asignatura:** Tópicos Avanzados de Programación  
**Docente:** Alejandro Estrada Padilla  
**Estudiante:** Emiliano Montes Morales  

---

## 📋 Descripción del Proyecto
Esta práctica implementa una solución integral en Python para el análisis exploratorio, agregación estadística, manipulación tabular y visualización de datos de una generación de Ingeniería en Sistemas Computacionales (24 alumnos, 2 grupos, 4 materias y 3 unidades temáticas: 288 registros).

El proyecto se presenta en dos formatos equivalentes:
- **`practica_pandas.py`**: Script de Python con bloques de comentarios visuales y diseño modular.
- **`practica_pandas.ipynb`**: Jupyter Notebook interactivo con celdas de Markdown que explican la lógica de cada bloque.

---

## 📁 Estructura del Repositorio
```text
practica_pandas/
├── calificaciones_isc.csv         # Dataset de entrada con 288 registros
├── practica_pandas.py             # Script ejecutable en Python
├── practica_pandas.ipynb          # Jupyter Notebook estructurado
├── promedios_alumnos.csv          # CSV exportado con matrícula, nombre y promedio
├── promedio_materias.png          # Gráfica de barras (escala 0-100)
├── histograma.png                 # Histograma de calificaciones con corte en 70
├── tendencia_unidades.png         # Gráfica de líneas de tendencia por unidad
├── Practica_Pandas_Matplotlib.pdf # Enunciado y rúbrica oficial
└── README.md                      # Documentación completa y reporte de resultados
```

---

## 🛠️ Ejercicios Resueltos y Buenas Prácticas Aplicadas

### Ejercicio 1. Carga y revisión
- Lectura de `calificaciones_isc.csv` con `pd.read_csv()`.
- Inspección de `head()`, `shape`, `dtypes` y resumen estadístico `describe()`.
- **Justificación:** El archivo contiene **288 filas** porque 24 estudiantes cursan 4 materias evaluadas en 3 unidades ($24 \times 4 \times 3 = 288$).

### Ejercicio 2. Filtros
- Conteo sin bucles utilizando `len(df_filtrado)`:
  - Solo Grupo A: **144 filas**.
  - Unidades con calificación menor a 70: **108 filas**.
  - Materia *Bases de datos*, Grupo B con calificación $\ge 80$: **18 filas**.

### Ejercicio 3. Columna calculada
- Vectorización con `import numpy as np` y `np.where(df['calificacion'] >= 70, 'Aprobado', 'Reprobado')`, garantizando alto rendimiento y código idiomático de Pandas.

### Ejercicio 4. Resúmenes y Exportación
- Agrupaciones con `.groupby()` para cálculo de promedios por materia, grupo/materia, alumno y unidad.
- Exportación segura a `promedios_alumnos.csv` encadenando `.reset_index()` y pasando `index=False`.

### Ejercicio 5. Gráficas con Matplotlib
- Estética mejorada con rejilla `plt.grid(True, linestyle='--', alpha=0.6)`, paleta cromática diferenciada y etiquetas descriptivas.
- **Prevención de error crítico:** Invocación de `plt.savefig()` **estrictamente antes** de `plt.show()` para garantizar imágenes no vacías y con resolución de 300 DPI.

### Ejercicio 6. Lectura de resultados y Análisis Argumentado
1. **Materia con promedio más bajo:** *Matemáticas discretas* (promedio: **65.01 puntos**).
2. **Tendencia de la Unidad 3:** **Sí**, el promedio general de la Unidad 3 (**67.83**) es inferior al de la Unidad 1 (**75.30**) y Unidad 2 (**73.56**).
3. **Alumnos bajo 70:** **6 de los 24 alumnos (25.0%)** quedaron por debajo del promedio aprobatorio.

> **Párrafo de interpretación técnica:**  
> *A partir del análisis cuantitativo y visual de los registros académicos, se observa que la asignatura con el rendimiento más bajo corresponde a Matemáticas discretas, registrando un promedio de 65.01 puntos, situándose como la disciplina con mayor índice de dificultad conceptual para la generación. Con respecto a la progresión del curso, el promedio general experimentó un claro descenso hacia el cierre del periodo: mientras que las unidades 1 y 2 alcanzaron promedios de 75.30 y 73.56 puntos respectivamente, la unidad 3 descendió a 67.83 puntos. Esta caída sistemática se corrobora de manera directa en el gráfico de líneas `tendencia_unidades.png`, donde las trayectorias de las cuatro asignaturas muestran una pendiente negativa marcada hacia la tercera unidad debido al incremento acumulativo en la complejidad de los temas finales y la saturación por entregas de proyectos. Finalmente, al consolidar las calificaciones por estudiante, un total de 6 de los 24 alumnos (25.0%) concluyeron con un promedio general inferior al mínimo aprobatorio de 70, indicando una necesidad prioritaria de implementar asesorías académicas preventivas e intervenciones remediales previo a las evaluaciones finales.*

---

## 🚀 Instrucciones para Sincronizar con GitHub

1. Crear un nuevo repositorio en GitHub llamado `practica-pandas-tap` (o el nombre preferido).
2. Vincular el repositorio local y subir los archivos:
```bash
git remote add origin https://github.com/Emilianomontes/practica-pandas-tap.git
git branch -M main
git push -u origin main
```
