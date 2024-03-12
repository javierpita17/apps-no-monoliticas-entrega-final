class ReservaCitaQueryHandler:
    def handle(self, query):
        if query.tipo == 'buscar_por_cliente':                    
            return self.repository.obtener_reservas_por_cliente_id(query.cliente_id)
        elif query.tipo == 'buscar_por_fecha':
            return self.repository.obtener_reservas_por_fecha(query.fecha)
        elif query.tipo == 'buscar_por_propiedad':
            return self.repository.obtener_reservas_por_propiedad_id(query.propiedad_id)
        else:
            raise ValueError(f"Tipo de consulta no soportado: {query.tipo}")
