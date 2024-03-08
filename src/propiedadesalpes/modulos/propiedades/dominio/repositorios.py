""" Interfaces para los repositorios del dominio de propiedades

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de propiedades

"""

from abc import ABC
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioReservas(Repositorio, ABC):
    ...

class RepositorioEventosReservas(Repositorio, ABC):
    ...
