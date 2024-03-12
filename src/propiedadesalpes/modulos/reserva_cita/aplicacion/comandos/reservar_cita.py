class ReservarCitaCommand:
    def __init__(self, cliente_id, agente_id, propiedad_id, fecha_hora):
        self.cliente_id = cliente_id
        self.agente_id = agente_id
        self.propiedad_id = propiedad_id
        self.fecha_hora = fecha_hora
