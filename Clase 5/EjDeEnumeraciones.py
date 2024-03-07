# Enumeraciones, nos permite cerrar la cantidad de posibilidades del valor (por ejemplo 2 opciones)
# Se trata de restringir las posibilidades (por ej la cant de cuotas)
# Key - Entidad FInanciera - 2 opciones son validas (VISA/MASTER)

from enum import Enum

class EntidadFinanciera(Enum):
    VISA = 'VISA'
    MASTERCARD = 'MASTERCARD'