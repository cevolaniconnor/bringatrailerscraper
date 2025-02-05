import pandas as pd

file = 'soldGT2.xlsx'

df = pd.read_excel(file)

df[['City', 'State', 'Zip']] = df.iloc[:, 7].str.extract(r'([A-Za-z\s]+),\s*([A-Za-z\s]+)\s*(\d+)', expand=True)


df.to_excel(file, index=False)

print(df.head())