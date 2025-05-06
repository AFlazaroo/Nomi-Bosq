from flask import Blueprint, render_template, flash, request
from app.model.Empleado import Empleado
from app import get_connection
app_bp = Blueprint('app_bp', __name__)  # Blueprint para manejar rutas

@app_bp.route('/inicio')
def inicioPaginaNomina():
    return render_template('base.html')

@app_bp.route('/inicio/gestion_empleados')
def pt_gestion_empleado():
    empleados = Empleado.query.all()
    return render_template('GestionEmpleado.html', empleados = empleados)

@app_bp.route('/inicio/gestion_empleados/crear_empleado', methods=['GET', 'POST'])
def pt_crear_empleado():

    #Cargar los cargos de los empleados de la base de datos
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc('obtener_cargos')
    
    cargos = []
    for result in cursor.stored_results():
        cargos = [row[0] for row in result.fetchall()]

    print(f'Cargos: {cargos}')
    
    cursor.close()
    conn.close()

    print(f'Cargos: {cargos}')

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        estado_civil = request.form['estado_civil']
        genero = request.form['genero']
        n_documento = request.form['n_documento']
        cargo = request.form['cargo']
        estado = request.form['estado']
        direccion = request.form['direccion']
        fecha_ingreso = request.form['fecha_ingreso']

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.callproc('insertar_empleado', (nombre, email, fecha_nacimiento, telefono, estado_civil, genero, n_documento, cargo, estado, direccion, fecha_ingreso))
            conn.commit()
            flash('Usuario registrado exitosamente', 'success')
        except Exception as e:
            conn.rollback()
            flash(f'Error al registrar usuario: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('GestionEmpleadoAgregar.html', cargos = cargos)