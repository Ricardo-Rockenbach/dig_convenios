import pandas as pd
from auxiliar import selecionar_PLANILHA_ACORDO

# PROCESSAMENTO DOS DADOS ACORDO 

def pos_processamentoACORDO():
    print("Iniciando pós-processamento da planilha ACORDO...")
    
    # Leitura da Planilha ACORDO, ACORDO JUDICIAL e CMI
    caminho_arquivo_acordo = selecionar_PLANILHA_ACORDO()
    
    primeira_linha = 2
    ultima_linha = 13
    
    df_acordo = pd.read_excel(
        caminho_arquivo_acordo,
        skiprows=primeira_linha - 1,
        nrows=ultima_linha - primeira_linha + 1,
        usecols=[0, 1, 2, 3],
        header=None,
    )
    df_acordo.columns = ["MES_NOME", "VALOR_ACORDO", "VALOR_ACORDO_JUDICIAL", "VALOR_CMI"]
    df_acordo["MES_NOME"] = df_acordo["MES_NOME"].astype(str).str.strip().str.upper()
    df_acordo = df_acordo.set_index("MES_NOME")
    

    print(df_acordo)
    print("Pós-processamento da planilha ACORDO finalizado.")

    return df_acordo


