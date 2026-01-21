import pandas as pd

for c in range(1):

    df = pd.read_excel(rf"F:\Beckap\GERAM NORD UM MILHAO\PARTES DA GERAL10.xlsx")

    mask = ~df['Razão Social ou Nome Empresarial'].str.contains('LTDA')
    df = df[mask]

    df.to_excel(rf"F:\Beckap\GERAM NORD UM MILHAO\sem ltda\PARTES DA GERAL10.xlsx", index=False)
    print(c)


