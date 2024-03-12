from propertiesalpes.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerUsuario(Query):
    user_id: uuid.UUID


class ObtenerUsuarioHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...
