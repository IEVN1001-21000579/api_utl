from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    titulo='IEVN-1001'
    lista=['Cesar', 'Juan', 'Pedro', 'Maria']
    return render_template('uno.html', titulo=titulo, list=list)

@app.route('/user/<string:user>')
def user(user):
    return 'User: {}'.format(user)

@app.route('/numero/<int:n1>')
def numero(n1):
    return 'Number: {}'.format(n1)

@app.route('/user/<string:nom>/<int:id>')
def nom(nom, id):
    return '<h1>ID: {} Nombre: {}'.format(id, nom)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return 'Suma: {}'.format(n1+n2)

@app.route('/default')
@app.route('/default/<string:nom>')
def nom2(nom='Cesar'):
    return '<h1>Nombre: {}'.format(nom)

if __name__ == '__main__':
    app.run(debug=True)

# Este es un comentario