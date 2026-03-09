# regras/sus.py

from .base import RegraBase


class RegraSUS(RegraBase):

    def aplicar(self, dados):

        dados["VALOR_CUSTO_M"] = None
        dados["VALOR_VENDA_M"] = None
        dados["VALOR_VENDA_D"] = None
        dados["VALOR_CUSTO_T"] = None
        dados["VALOR_VENDA_T"] = None

        return dados