from processamento import processar_planilha
from pos_processamento import pos_processamento

def main():
    print("Iniciando processamento da planilha...")
    
    processar_planilha()

    print("Processamento finalizado.")

    pos_processamento()

if __name__ == "__main__":
    main()