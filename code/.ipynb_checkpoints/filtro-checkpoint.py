import pandas as pd

class FiltroCandidatos:
    def __init__(self, data_path="data.csv"):
        self.df = pd.read_csv(data_path)

    def filtrar(self, edad_min=None, edad_max=None,
                frecuencia_min=None, frecuencia_max=None,
                monto_min=None, monto_max=None,
                categorias=None,
                estaciones=None):
        df_filtrado = self.df.copy()

        if edad_min is not None:
            df_filtrado = df_filtrado[df_filtrado["edad"] >= edad_min]
        if edad_max is not None:
            df_filtrado = df_filtrado[df_filtrado["edad"] <= edad_max]

        if frecuencia_min is not None:
            df_filtrado = df_filtrado[df_filtrado["frecuencia"] >= frecuencia_min]
        if frecuencia_max is not None:
            df_filtrado = df_filtrado[df_filtrado["frecuencia"] <= frecuencia_max]

        if monto_min is not None:
            df_filtrado = df_filtrado[df_filtrado["monto_prom"] >= monto_min]
        if monto_max is not None:
            df_filtrado = df_filtrado[df_filtrado["monto_prom"] <= monto_max]

        if categorias is not None and len(categorias) > 0:
            df_filtrado = df_filtrado[df_filtrado["categoria_fav"].isin(categorias)]

        if estaciones is not None and len(estaciones) > 0:
            df_filtrado = df_filtrado[df_filtrado["estacion_pref"].isin(estaciones)]

        return df_filtrado.reset_index(drop=True)

if __name__ == "__main__":
    filtro = FiltroCandidatos()
    candidatos = filtro.filtrar(frecuencia_min=3, monto_min=100)
    print(candidatos.head())
