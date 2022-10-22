###Ejercicio 1
import pandas as pd
df = pd.read_csv("weatherHistory.csv")
print(df)

###Ejercicio 2
print(df.columns)


###Ejercicio 3
print(df["Precip Type"].unique())


###Ejercicio 4
print(df["Pressure (millibars)"].mean())


###Ejercicio 5
df_subset = df[df.Summary=="Partly Cloudy"]
df_subset["Pressure (millibars)"].mean()


###Ejercicio 6
df_subset = df[df["Daily Summary"]=="Foggy until afternoon."]


###Ejercicio 7
len(df["Daily Summary"].unique())
len(df["Summary"].unique())

