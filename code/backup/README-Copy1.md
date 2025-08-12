# Explicación del Código: Perceptrón para Clasificación de Clientes

Este código implementa un modelo de perceptrón para clasificar clientes como receptivos o no receptivos a una campaña promocional, basado en sus características: edad, frecuencia de compra y monto promedio gastado.

---

## Clase Perceptrón

- **Inicialización:**  
  Crea un vector de pesos `w` y un sesgo `b`, ambos inicializados en cero.  
  Parámetros: tamaño de entrada (`input_size`), tasa de aprendizaje (`learning_rate`) y número de épocas (`epochs`).

- **Función de activación:**  
  Es una función escalón que devuelve `1` si la suma ponderada es mayor a cero, y `0` en caso contrario.

- **Método `predict`:**  
  Calcula el producto punto entre los pesos y las características de entrada, suma el sesgo y aplica la función de activación para obtener la predicción.

- **Método `fit`:**  
  Entrena el perceptrón ajustando los pesos y sesgo iterativamente para minimizar el error entre las predicciones y las etiquetas reales.  
  Para cada dato de entrenamiento:  
  1. Calcula la salida actual.  
  2. Determina el error (diferencia entre etiqueta real y predicción).  
  3. Actualiza los pesos y el sesgo usando la regla del perceptrón.

---

## Carga y Preparación de Datos

- Se lee el archivo `data.csv` con columnas: `age`, `freq`, `spent`, `label`.  
- Las características (`age`, `freq`, `spent`) se almacenan en una matriz `X`.  
- Las etiquetas (`label`) se almacenan en un vector `y`.

---

## Entrenamiento y Guardado del Modelo

- Se crea una instancia del perceptrón con los parámetros deseados.  
- Se entrena el modelo con los datos cargados mediante el método `fit`.  
- Finalmente, el modelo entrenado se guarda en un archivo binario `perceptron_model.pkl` usando `pickle`.

---

## Visualización y Predicción

- Se recargan los datos y el modelo entrenado.  
- Para cada cliente, se predice si es receptivo o no.  
- Se grafica un scatter plot con la edad en el eje X y el monto promedio en el eje Y.  
- Los puntos verdes representan clasificaciones correctas, los rojos indican errores.  
- Esta visualización ayuda a interpretar cómo el modelo separa los clientes según sus características.

---

Este enfoque básico permite identificar patrones lineales en los datos y segmentar clientes para campañas promocionales de manera efectiva usando álgebra lineal y aprendizaje supervisado.
