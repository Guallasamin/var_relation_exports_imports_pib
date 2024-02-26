import pandas as pd
import matplotlib.pyplot as plt

# 1. Importar datos
# 1.1. Importar datos de PIB trimestral
pib_trimestral = pd.read_excel('/Users/jguallasamin/Desktop/Tesis/data_1708813067.xlsx', sheet_name='datos', decimal='.', index_col=0, usecols='A:G')
print(pib_trimestral.head())

# 1.2 Definir como serie de tiempo y graficar
pib_trimestral.index = pd.to_datetime(pib_trimestral.index)



