from flask import Flask, render_template
from datetime import datetime
import os
ruta_actual = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(ruta_actual, 'templates'))

@app.route('/')
def inicio():
    ahora = datetime.now()
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_semana = dias[ahora.weekday()]
    
    mensaje_prueba = "MI PRIMERA PAGINA WEB"
    
    return render_template('index.html', info=dia_semana, informacion=mensaje_prueba)
if __name__ == '__main__':
    app.run(debug=True, port=5001)