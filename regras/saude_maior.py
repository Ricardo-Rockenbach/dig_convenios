# Regras Saude Maior

# regra para que o convenio Saude maior preencha em cada mes um valor fixo na coluna 13 da planilha principal
from .base import RegraBase

class RegraSaudeMaior(RegraBase):
    
    def aplicar(self, dados):

        dados["VALOR_VENDA_M"] = None
        dados["VALOR_VENDA_D"] = None
        dados["VALOR_VENDA_T"] = None
        dados["TOTAL_VENDA"] = 400000

        return dados    
        