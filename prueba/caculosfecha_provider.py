from elegircal import MMM
from media1 import Mediafecha
from calculosfecha_factory import Calculos_estadistico_fecha


class Calculosfechaprovider:
    @staticmethod
    def create_calculos(elegircal: MMM) -> Calculos_estadistico_fecha:
        if elegircal == MMM.MEDIA:
            return Calculos_estadistico_fecha()
        elif elegircal == MMM.MODA:
            return Mediafecha()
        else:
            raise ValueError(f'Invalid product {elegircal}')
    