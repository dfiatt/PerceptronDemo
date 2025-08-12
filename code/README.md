# Proyecto Perceptrón para Predicción de Clientes Receptivos

---

## Descripción General

Este proyecto implementa un sistema básico de predicción para identificar clientes receptivos a campañas promocionales basándose en datos históricos. Usa un **Perceptrón**, un algoritmo simple de aprendizaje supervisado, para clasificar clientes según su perfil de compra.

El sistema consta de:

- **Generación de datos sintéticos** para simular un conjunto de clientes con características relevantes.
- **Filtro previo** para seleccionar candidatos según parámetros definidos por el usuario.
- **Entrenamiento y uso del perceptrón** para predecir receptividad de los clientes.

---

## Archivos y Componentes

### 1. `data_factory.ipynb`

- Genera un archivo `data.csv` con datos sintéticos de clientes.
- Las columnas del CSV incluyen:
  - `edad`: edad del cliente (18-70 años)
  - `frecuencia`: número de compras en un periodo (distribución Poisson)
  - `monto_prom`: monto promedio gastado (distribución Normal)

### 2. `filtro.py`

- Contiene la clase `FiltroCandidatos` que carga el archivo `data.csv`.
- Permite filtrar clientes según:
  - Rango de edad
  - Rango de frecuencia de compras
  - Rango de monto promedio

### 3. `perceptron.py`

- Implementa la clase `Perceptron` con métodos para:
  - Entrenamiento (`fit`)
  - Predicción (`predict`)
  - Guardar el modelo entrenado (`save`)
  - Cargar un modelo entrenado (`load`)
- Incluye historial de errores durante el entrenamiento

---

## Cómo usar el sistema

### Paso 1: Generar los datos sintéticos

Ejecuta el notebook `data_factory.ipynb` para crear el archivo `data.csv` con 1000 registros de clientes simulados.

### Paso 2: Filtrar candidatos

Usa la clase `FiltroCandidatos` para preseleccionar clientes según tus criterios:

```python
filtro = FiltroCandidatos()
candidatos = filtro.filtrar(
    edad_min=25,
    frecuencia_min=3,
    monto_min=100
)
```

### Paso 3: Entrenar el perceptrón

```python
perceptron = Perceptron(input_size=3)
perceptron.fit(X_train, y_train)
```

## Requisitos

- Python 3.7+
- Paquetes Python:
  - numpy
  - pandas
  - joblib

Se pueden instalar las dependencias con:

```bash
pip install numpy pandas joblib
```
---------------------------------------------------------------------------------

## Requisitos

- Python 3.7+
- Paquetes Python:
  - numpy
  - pandas
  - matplotlib

Se pueden instalar las dependencias con:

pip install numpy pandas matplotlib
