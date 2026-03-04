import pandas as pd

# Ler o arquivo xlsx
df = pd.read_excel(
    r"data\dados_brutos.xlsx",
    usecols=["CONVENIO","VALOR_CUSTO_M","VALOR_VENDA_M","VALOR_CUSTO_D","VALOR_VENDA_D","VALOR_CUSTO_T","VALOR_VENDA_T", "INDATA_INICIAL"],
    )
# extrair o mes da coluna "INDATA_INICIAL"
df["INDATA_INICIAL"] = pd.to_datetime(df["INDATA_INICIAL"], errors="coerce", dayfirst=True)
df["MES"] = df["INDATA_INICIAL"].dt.month

# remover linhas com valores nulos
df = df.dropna()
# definir index como a coluna "CONVENIO"
df = df.set_index("CONVENIO")
# Remover os covenios com nome "CONVENIO"
df = df[~df.index.str.contains("CONVENIO", case=False)]

# criar uma nova planilha para cada convenio
for convenio in df.index.unique():
    df_convenio = df[df.index == convenio]
    df_convenio.to_excel(f"data\extracao\{convenio}.xlsx")

print(df)





# # Le uma nova planilha
# df2 = pd.read_excel(
#     r"data\Custo Receita 2025 Int.xlsx",
#     sheet_name="Total",
#     skiprows=3,
#     usecols=[0,5,6,7,8,9,10]
#     )
# df2 = df2.dropna()
# df2 = df2.set_index("CONVENIO")
# df2 = df2[~df2.index.str.contains("CONVENIO", case=False)]
# df2 = df2[~df2.index.str.contains("TOTAL", case=False)]


# #print(df)
# print(df2)