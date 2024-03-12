from propiedadesalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioReservas
from propiedadesalpes.modulos.propiedades.dominio.entidades import Reserva
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorReserva
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Reserva)
        reserva =  self._fabrica_propiedades.crear_objeto(vista.obtener_por(id=query.id)[0], MapeadorReserva())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)