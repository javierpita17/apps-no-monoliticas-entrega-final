from propiedadesalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

class Reserva(db.Model):
    __tablename__ = "reservas"
    id = db.Column(db.String(40), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)

class EventosReserva(db.Model):
    __tablename__ = "eventos_reserva"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

class PropiedadDTO(db.Model):
    __tablename__ = "propiedades"    
    id = db.Column(db.String(40), primary_key=True)
    ubicacion = db.Column(db.Integer)
    valorMercado = db.Column(db.String(200))
    estadoActual = db.Column(db.String(200))
    tipo= db.Column(db.String(200))

