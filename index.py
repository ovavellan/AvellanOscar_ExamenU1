# importar la libreria flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
# llamar a index.html en la ruta principal
def principal():
    return render_template('/principal.html')


# ejecutar
if __name__ == '__main__':
    app.run(debug=True)
