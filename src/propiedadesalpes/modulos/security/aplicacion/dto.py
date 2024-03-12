from dataclasses import dataclass, field
from propertiesalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class UserDTO(DTO):    
    id: str = field(default_factory=str)
    username: str
    password: str
    estadoActual: str
