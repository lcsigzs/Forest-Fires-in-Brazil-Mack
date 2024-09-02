"""
Primeiras impressoes e tratamento de dados com o dataset do Kaggle sobre Queimadas no Brasil 
"""

import pandas as pd

df = pd.read_csv('../amazon.csv', encoding='iso-8859-1', parse_dates=['date'])
print(df)

print(df.head())

print(len(df))

print(df.dtypes)

print(df.tail())

print(f"Tem {df.shape[0]} linhas e {df.shape[1]} colunas nesse dataset")

print(df.duplicated().any())

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df.duplicated().any(), df.duplicated().sum())

print(df.isna().sum())