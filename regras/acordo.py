# regras/acordo.py

from .base import RegraBase


class RegraAcordo(RegraBase):

    def aplicar(self, dados):

        dados["VALOR_VENDA_M"] = None
        dados["VALOR_VENDA_D"] = None
        dados["VALOR_VENDA_T"] = None

        return dados