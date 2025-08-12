# Proyecto Perceptrón para Predicción de Clientes Receptivos

---

## Descripción General

Este proyecto implementa un sistema básico de predicción para identificar clientes receptivos a campañas promocionales basándose en datos históricos. Usa un **Perceptrón**, un algoritmo simple de aprendizaje supervisado, para clasificar clientes según su perfil de compra.

El sistema consta de:

- **Generación de datos sintéticos** para simular un conjunto de clientes con características relevantes.
- **Filtro previo** para seleccionar candidatos según parámetros definidos por el usuario.
- **Entrenamiento y uso del perceptrón** para predecir receptividad de los clientes.
- **Interfaz de consola básica** para interacción con el usuario.
- **Visualización gráfica** de los resultados (clientes receptivos vs no receptivos).

---

## Archivos y Componentes

### 1. `data_factory.ipynb`

- Genera un archivo `data.csv` con datos sintéticos de clientes.
- Las columnas del CSV incluyen:
  - `edad`: edad del cliente.
  - `frecuencia`: número de compras en un periodo.
  - `monto_prom`: monto promedio gastado.
  - `categoria_fav`: categoría favorita de productos.
  - `estacion_pref`: estación del año preferida para comprar.

### 2. `filtro.py`

- Contiene la clase `FiltroCandidatos` que carga el archivo `data.csv` y permite filtrar clientes según rangos o listas de valores para cada columna.
- Se usa para preseleccionar candidatos que cumplen criterios específicos antes de la clasificación con el perceptrón.

### 3. `perceptron.py`

- Implementa la clase `Perceptron` con métodos para:
  - Entrenamiento (`fit`).
  - Predicción (`predict`).
  - Guardar el modelo entrenado en disco (`save`).
  - Cargar un modelo entrenado (`load`).
- Usa álgebra lineal para ajustar pesos y clasificar los datos.

### 4. `vista.py` (o `vista.ipynb`)

- Script controlador principal para la aplicación.
- Solicita al usuario ingresar:
  - Tipo de producto a promocionar.
  - Monto del producto.
- Usa el filtro para seleccionar candidatos basados en esos parámetros.
- Entrena el perceptrón con los datos filtrados.
- Muestra la lista de clientes receptivos y no receptivos según la predicción.
- Imprime el porcentaje promedio de receptividad y aciertos del modelo.
- Grafica la cantidad de clientes receptivos y no receptivos.

---

## Cómo usar el perceptron

### Paso 1: Generar los datos sintéticos

Ejecutando el notebook `data_factory.ipynb` para crear el archivo `data.csv` con datos de clientes simulados, o importa un archivo data.csv que contenga data de clientes que contenga las columnas: edad, frecuencia, monto_prom, categoria_fav, estacion_pref

### Paso 2: Filtrar candidatos y entrenar el modelo

Ejecuta `vista.py` o el notebook `vista.ipynb`:

1. Ingresa la categoría del producto que deseas promocionar (por ejemplo: "Herramientas", "Electrónica").
2. Ingresa el monto mínimo de compra para filtrar clientes.
3. El programa filtrará los candidatos en base a estos criterios.
4. Entrenará el perceptrón con los datos filtrados y etiquetados según la lógica definida (clientes con frecuencia > 5 y monto promedio > 100 se consideran receptivos).
5. Mostrará clientes receptivos y no receptivos.
6. Mostrará estadísticas de desempeño y una gráfica resumen.
7. Interpretación de lecturas:
---------------------------------------------------------------------------------
| Columna             | Significado                                             |
| ------------------- | ------------------------------------------------------- |
| **Edad**            | Edad del cliente (entrada 1 del modelo).                |
| **Frecuencia**      | Frecuencia de compras (entrada 2).                      |
| **Monto\_Promedio** | Promedio de gasto en colones (entrada 3).               |
| **Real**            | Clase **real** (objetivo): 0 = no compra, 1 = compra.   |
| **Predicción**      | Lo que el **modelo predijo** para ese cliente.          |
| **Acierto**         | Si la predicción fue igual a la real, Si falló.         |
---------------------------------------------------------------------------------

## Requisitos

- Python 3.7+
- Paquetes Python:
  - numpy
  - pandas
  - matplotlib

Se pueden instalar las dependencias con:

pip install numpy pandas matplotlib
