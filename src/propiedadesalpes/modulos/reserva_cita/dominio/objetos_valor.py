from datetime import datetime

class FechaHora:
    def __init__(self, value):
        self.value = self.validar_fecha_hora(value)
    
    @staticmethod
    def validar_fecha_hora(value):
        formato_fecha_hora = "%Y-%m-%d %H:%M"
        try:
            fecha_hora_validada = datetime.strptime(value, formato_fecha_hora)
        except ValueError:
            raise ValueError(f"La fecha y hora proporcionadas '{value}' no están en el formato correcto '{formato_fecha_hora}'.")

        if fecha_hora_validada < datetime.now():
            raise ValueError("La fecha y hora proporcionadas no pueden estar en el pasado.")

        return fecha_hora_validada

try:
    fecha_hora = FechaHora("2024-03-04 15:00")
    print(fecha_hora.value)
except ValueError as e:
    print(e)
