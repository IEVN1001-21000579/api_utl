from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from config import config

app=Flask(__name__)

con=MySQL(app)

@app.route('/alumnos', methods=['GET'])
def lista_alumnos():
    try:
        cursor=con.connection.cursor()
        sql='SELECT * FROM alumnos'
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for fila in datos:
            alumno={'matricula': fila[0], 'nombre': fila[1], 'apaterno': fila[2], 'amaterno': fila[3], 'correo': fila[4]}
            alumnos.append(alumno)
        return jsonify({'alumnos': alumnos, 'mensaje': 'lista de alumnos', 'exito': True})
    
    except Exception as ex:
        return jsonify({'message': 'error {}'.format(ex), 'exito': False})

    return ''

@app.route('/alumnos/<mat>', methods=['GET'])
def lista_alumnos(mat):
    try:
        alumno=leer_alumno_bd(mat)
        if alumno!=None:
            return jsonify({'alumno': alumno, 'mensaje': 'alumno encontrado', 'exito': True}),
        else:
            return jsonify({'mensaje': 'alumno no encontrado', 'exito': False}),
    
    except Exception as ex:
        return jsonify({'message': 'error {}'.format(ex), 'exito': False})

    return ''

def pagina_no_encontrada(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000, debug=True)