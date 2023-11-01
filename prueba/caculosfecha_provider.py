from elegircal import MMM
from media1 import Mediafecha
from calculosfecha_factory import Calculos_estadistico_fecha


class Calculosfechaprovider:
    @staticmethod
    def create_calculos(elegircal: MMM) --> Calculos_estadisticos_fecha:
        match elegircal:
            case MMM.MEDIA:
                return Mediafecha()
            case MMM.MODA:
                return Modafecha()
            case _:
                raise ValueError(f'Invalid elegircal: {elegircal}')
    