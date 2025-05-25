# app/controller/contratocontroller.py

from flask import Blueprint, render_template, request, redirect, url_for
from app import get_connection

contrato_bp = Blueprint('contrato_bp', __name__, url_prefix='/inicio/gestion_contratos')


@contrato_bp.route('/')
def pt_gestion_contratos():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.callproc('obtener_contratos')
        contratos = []

        for result in cursor.stored_results():
            column_names = [desc[0] for desc in result.description]
            contratos = [dict(zip(column_names, row)) for row in result.fetchall()]

        print(f'Contratos obtenidos: {contratos}')
    except Exception as e:
        print(f'Error al obtener contratos: {str(e)}')
        contratos = []
    finally:
        cursor.close()
        conn.close()

    return render_template('contratos/GestionContrato.html', contratos=contratos)
