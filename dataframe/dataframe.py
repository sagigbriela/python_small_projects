import numpy as np
import pandas as pd
import datetime as dt
from pandas import Series,DataFrame

data = {
	"contrato_a" :  {
		"fecha_de_inicio" : dt.datetime(2024,1,1),
		"fecha_fin" : dt.datetime(2024,1,7)
	},
	"contrato_b" : {
		"fecha_de_inicio" : dt.datetime(2024,1,3),
		"fecha_fin" : dt.datetime(2024,12,31)
	}
}

df = pd.DataFrame(data)

df_transposed = df.T

fecha_de_inicio_row = df_transposed.loc[:, "fecha_de_inicio"]
fecha_fin_row = df_transposed.loc[:, "fecha_fin"]

fecha_inicio = dt.datetime.min 
fecha_fin = dt.datetime.max


for fecha in fecha_de_inicio_row:
    if fecha >= fecha_inicio:
        fecha_inicio = fecha

for fechafin in fecha_fin_row:
    if fechafin <= fecha_fin:
        fecha_fin = fechafin

print(f'Fecha de inicio superposición:{fecha_inicio}')
print(f'Fecha de fin superposicion:{fecha_fin}')