import pandas as pd
import os

# =========================
# CONFIGURAÇÕES
# =========================

# Mapa dos Meses
meses = {
    1: "JANEIRO",
    2: "FEVEREIRO",
    3: "MARÇO",
    4: "ABRIL",
    5: "MAIO",
    6: "JUNHO",
    7: "JULHO",
    8: "AGOSTO",
    9: "SETEMBRO",
    10: "OUTUBRO",
    11: "NOVEMBRO",
    12: "DEZEMBRO"
}

# Mapa das linhas dos meses na planilha a ser preenchida
posicao_meses = {
    "JANEIRO": 3,
    "FEVEREIRO": 34,
    "MARÇO": 65,
    "ABRIL": 96,
    "MAIO": 127,
    "JUNHO": 158,
    "JULHO": 189,
    "AGOSTO": 220,
    "SETEMBRO": 251,
    "OUTUBRO": 282,
    "NOVEMBRO": 313,
    "DEZEMBRO": 344
}



# =========================
# LEITURA DOS DADOS
# =========================

# Ler o arquivo xlsx
df = pd.read_excel(
    r"data\dados_brutos.xlsx",
    usecols=[
        "CONVENIO",
        "VALOR_CUSTO_M",
        "VALOR_VENDA_M",
        "VALOR_CUSTO_D",
        "VALOR_VENDA_D",
        "VALOR_CUSTO_T",
        "VALOR_VENDA_T", 
        "INDATA_INICIAL"
   ],
)

# Tratar a coluna "INDATA_INICIAL" para extrair o mês e o nome do mês
df["INDATA_INICIAL"] = pd.to_datetime(df["INDATA_INICIAL"], errors="coerce", dayfirst=True)
df["MES"] = df["INDATA_INICIAL"].dt.month
df["MES_NOME"] = df["MES"].map(meses)

# =========================
# LIMPEZA DOS DADOS
# =========================

# remover linhas com valores nulos
df = df.dropna(subset=["CONVENIO"])
# definir index como a coluna "CONVENIO"
df = df.set_index("CONVENIO")
# Remover os covenios com nome "CONVENIO"
df = df[~df.index.str.contains("CONVENIO", case=False)]
# dropar a coluna "INDATA_INICIAL"
df = df.drop(columns=["INDATA_INICIAL"])




# =========================
# CRIAR PLANILHAS POR CONVÊNIO
# =========================

# criar a pasta "data/extracao" se ela não existir
os.makedirs("data/extracao", exist_ok=True)

# criar uma nova planilha para cada convenio
for convenio, df_convenio in df.groupby(level=0):
    print(f"Processando convênio: {convenio}")
    # ordenar o dataframe por mes
    df_convenio = df_convenio.sort_values("MES")
    df_convenio.to_excel(f"data\extracao\{convenio}.xlsx")

print(df)

