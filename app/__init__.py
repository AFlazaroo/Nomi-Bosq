from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1074129082@localhost/Nomina_ProyectoFinalBD'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # 🔥 Importar modelos para que SQLAlchemy los registre
    from app.model.Empleado import Empleado
    from app.model.Seguridad__social import SeguridadSocial
    from app.model.Cesantias import Cesantias
    from app.model.Incapacidad import Incapacidad
    from app.model.Contrato import Contrato
    from app.model.Vacaciones import Vacaciones
    from app.model.Horas_Extra import HorasExtra
    from app.model.Liquidacion import Liquidacion
    

    # Importamos las rutas desde controllers/routes.py
    from app.controller import routes
    app.register_blueprint(routes.app_bp)

    return app

# 🔥 Función para obtener conexión directa a MySQL (si la necesitas en otro punto)
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1074129082",
        database="Nomina_ProyectoFinalBD"
    )
