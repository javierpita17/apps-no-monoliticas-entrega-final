from propertiesalpes.seedwork.aplicacion.comandos import Comando, ComandoHandler


class Login(Comando):
    username: str
    password: float

class LoginHandler(ComandoHandler):
    ...
    