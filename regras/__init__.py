# regras/__init__.py

from .base import RegraBase
from .acordo import RegraAcordo
from .sus import RegraSUS
from .saude_maior import RegraSaudeMaior

def obter_regra(convenio):

    if convenio in ["ACORDO", "ACORDO JUDICIAL", "C.M.I", "SOCIOS"]:
        return RegraAcordo()
    
    if convenio in ["SUS"]:
        return RegraSUS()
    
    if convenio in ["SAUDE MAIOR"]:
        return RegraSaudeMaior()

    return RegraBase()