import pandas as pd

pib_trimestral = pd.read_excel('/Users/jguallasamin/Desktop/Tesis/data_1708813067.xlsx', sheet_name='datos', decimal='.', index_col=0, usecols='A:G')
print(pib_trimestral.head())