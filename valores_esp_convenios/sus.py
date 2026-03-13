import pandas as pd
from auxiliar import selecionar_PLANILHA_SUS



# PROCESSAMENTO DOS DADOS SUS 

def pos_processamentoSUS():
    print("Iniciando pós-processamento da planilha...")
    
    # Leitura da Planilha SUS
    caminho_arquivo_sus = selecionar_PLANILHA_SUS()
    
    primeira_linha = 4
    ultima_linha = 15
    
    df_sus = pd.read_excel(
        caminho_arquivo_sus,
        skiprows=primeira_linha - 1,
        nrows=ultima_linha - primeira_linha + 1,
        usecols=[0, 9],
        header=None,
    )
    df_sus.columns = ["MES_NOME", "VALOR_SUS"]
    df_sus["MES_NOME"] = df_sus["MES_NOME"].astype(str).str.strip().str.upper()
    df_sus = df_sus.set_index("MES_NOME")
    

    print(df_sus)
    print("Pós-processamento da planilha SUS finalizado.")

    return df_sus


