from pydispatch import dispatcher
from .handlers import HandlerPropiedadDominio

dispatcher.connect(HandlerPropiedadDominio.handle_login, signal ="PropiedadLogin")