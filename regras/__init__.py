# regras/__init__.py

from .base import RegraBase
from .acordo import RegraAcordo
from .sus import RegraSUS


def obter_regra(convenio):

    if convenio in ["ACORDO", "ACORDO JUDICIAL", "CMI", "SAUDE MAIOR"]:
        return RegraAcordo()
    
    if convenio in ["SUS"]:
        return RegraSUS()

    return RegraBase()