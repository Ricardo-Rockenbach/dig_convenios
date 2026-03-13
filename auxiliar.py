import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selecionar_DADOS_BRUTOS():
    Tk().withdraw()

    caminho = askopenfilename(
        title="Selecione a planilha de DADOS BRUTOS",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    return caminho


def selecionar_PLANILHA_CONVENIOS_20XX():
    Tk().withdraw()

    caminho = askopenfilename(
        title="Selecione a planilha a ser atualizada (planilha de convênios 20XX)",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    return caminho
    
def selecionar_PLANILHA_SUS():
    Tk().withdraw()

    caminho = askopenfilename(
        title="Selecione a planilha SUS",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    return caminho

def selecionar_PLANILHA_ACORDO():
    Tk().withdraw()

    caminho = askopenfilename(
        title="Selecione a planilha ACORDO",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )

    return caminho