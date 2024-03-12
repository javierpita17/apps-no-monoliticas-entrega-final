import propiedadesalpes.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorReservaDTOJson
from propiedadesalpes.modulos.security.aplicacion.comandos.login import Login
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando
from flask import Response
from propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio
import json

bp = api.crear_blueprint('login', '/login')

@bp.route('/login', methods=('POST',))
def reservar_usando_comando():
    try:
        session['uow_metodo'] = 'pulsar'

        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        comando = Login(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
                
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
