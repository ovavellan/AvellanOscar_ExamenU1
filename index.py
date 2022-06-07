# importar la libreria flask
from flask import Flask, redirect, request,render_template, url_for

app = Flask(__name__, template_folder='templates')


#Declaración de arreglo
datos_vehiculares = []

# evento = HolidayBase

#Definición de la ruta
@app.route('/')
# llamar a index.html en la ruta principal
def principal():
    return render_template('/principal.html', datos = datos_vehiculares )


#segundo controlador el cuál almacenara los elementos que ingresemos por el formulario HTML
@app.route('/enviar',  methods=['GET','POST'])
#Función enviar la cuál podrá almacenar los datos ingresados por medio del formulario dentro de nuestro arreglo
def enviar():
    if(request.method == "POST"):
        llamadas = len(datos_vehiculares) + 1
        # numero_llamadas = llamadas
        placas = request.form['placa']
        fechas = request.form['fecha']
        horas = request.form['hora']
        datos_vehiculares.append({llamadas: 'llamadas' ,'placa': placas, 'fecha': fechas, 'hora': horas })
        return redirect(url_for('principal'))


# Main del programa
if __name__ == '__main__':
    app.run(debug=True)
