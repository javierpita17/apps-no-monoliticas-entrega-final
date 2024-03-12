
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio
from propiedadesalpes.seedwork.infraestructura.vistas import Vista
from propiedadesalpes.modulos.propiedades.infraestructura.vistas import Vista
from propiedadesalpes.modulos.propiedades.dominio.entidades import Reserva
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioReservas, RepositorioEventosReservas
from .repositorios import RepositorioReservasSQLAlchemy, RepositorioEventosReservas
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas:
            return RepositorioReservasSQLAlchemy()
        elif obj == RepositorioReservas:
            return RepositorioReservasSQLAlchemy()
        elif obj == RepositorioEventosReservas:
            return RepositorioReservasSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Reserva:
            return VistaReserva()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')


