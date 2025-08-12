import matplotlib.pyplot as plt
from perceptron import Perceptron
from filtro import FiltroCandidatos
import pandas as pd
import numpy as np

def main():

    print("Vista.py is running...")  # add this as first line in file

    filtro = FiltroCandidatos()

    monto_producto = float(input("Ingrese monto mínimo del producto: "))

    candidatos = filtro.filtrar(
        monto_min=monto_producto
    )

    print(f"\nSe seleccionaron {len(candidatos)} candidatos con gasto mínimo de {monto_producto}")

    if len(candidatos) == 0:
        print("No hay candidatos para analizar. Finalizando programa.")
        return

    # Variables de entrada y etiquetas
    X = candidatos[["edad", "frecuencia", "monto_prom"]].values
    y = np.where((candidatos["frecuencia"] > 5) & (candidatos["monto_prom"] > 100), 1, 0)

    # Entrenar perceptrón
    perceptron = Perceptron(input_size=3, learning_rate=0.01, epochs=10)
    perceptron.fit(X, y)
    perceptron.save()

    # Evaluar modelo
    resultados = []
    for i, x in enumerate(X):
        pred = perceptron.predict(x)
        resultados.append({
            "edad": x[0],
            "frecuencia": x[1],
            "monto_prom": x[2],
            "prediccion": pred,
            "real": y[i],
            "acierto": pred == y[i]
        })

    df_resultados = pd.DataFrame(resultados)

    print("\nClientes receptivos:")
    print(df_resultados[df_resultados["prediccion"] == 1])

    print("\nClientes no receptivos:")
    print(df_resultados[df_resultados["prediccion"] == 0])

    receptividad_promedio = df_resultados["prediccion"].mean() * 100
    acierto_promedio = df_resultados["acierto"].mean() * 100

    print(f"\nPorcentaje promedio de clientes receptivos: {receptividad_promedio:.2f}%")
    print(f"Porcentaje promedio de aciertos del perceptrón: {acierto_promedio:.2f}%")

    # Graficar resultados
    etiquetas = ['Receptivos', 'No Receptivos']
    cantidades = [df_resultados["prediccion"].sum(), len(df_resultados) - df_resultados["prediccion"].sum()]

    plt.bar(etiquetas, cantidades, color=['purple', 'black'])
    plt.title('Cantidad de Clientes Receptivos y No Receptivos')
    plt.ylabel('Número de Clientes')
    plt.show()

if __name__ == "__main__":
    main()
