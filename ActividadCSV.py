import pandas as pd

#file = open("C:/Users/nalva/OneDrive/Escritorio/Python/Datos/CSV/Darknet.csv","r")
file = "C:/Users/nalva/OneDrive/Escritorio/Python/Datos/CSV/Darknet.csv"
#df = pd.DataFrame(file)
df = pd.read_csv(file)
#print(df.info())

#Mostrar las columnas con valores nulos
null_columns = df.columns[df.isnull().any()]
print("Columns with null values:", null_columns)

#Definir dataframes con valores nulos eliminados y rellenados
df1 = df.dropna()
df2 = df.fillna(0)

#Mostrar la cantidad de filas de cada dataframe
print(f"{'Dataframe:':<20}{'Cantidad de filas':<10}")
print(f"{'Original:':<20}{len(df):<10}")
print(f"{'Limpio:':<20}{len(df1):<10}")
print(f"{'Relleno:':<20}{len(df):<10}")
#Diferencia entre dataframe original y dataframe limpio
print(f"\nDiferencia df y df1: {len(df)-len(df1)}\n")

#Convertir los tipos de todas las columnas a numeros y string
for column in df2.columns:
    try:
        df2[column] = pd.to_numeric(df2[column])
    except (ValueError, TypeError):
        df2[column] = df2[column].astype(str)

#Definir las columnas que tengan datos de tipo fecha
df2["Timestamp"] = pd.to_datetime(df2["Timestamp"])

#Mostrar la informacion del dataframe limpio
print(df2.info())

#Guardar dataframe limpio en un archivo csv
df2.to_csv("C:/Users/nalva/OneDrive/Escritorio/Python/Datos/CSV/Darknet2.csv", index=False)