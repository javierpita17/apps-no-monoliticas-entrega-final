from propertiesalpes.modulos.property.dominio.eventos import RegistrarPropiedad
from propertiesalpes.seedwork.aplicacion.handlers import Handler

class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_login(evento):
        print('================ LOGIN SUCCESS ===========')
