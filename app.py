from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <h1 style="color:darkblue;">¡Bienvenido a la App de Transformación Digital!</h1>
    
    <p style="font-size:18px;">
        Esta aplicación fue creada como parte de un proyecto académico que demuestra cómo una app puede ser
        desplegada en la nube utilizando tecnologías modernas como <strong>Flask</strong> y <strong>Render</strong>.
    </p>
    
    <h2 style="color:green;">👥 Integrantes del equipo:</h2>
    <ul style="font-size:18px;">
        <li>Ernesto Sevilla</li>
        <li>Kevin Eslava</li>
        <li>Juan Tapia</li>
        <li>Paul Vargas</li>
    </ul>

    <p style="font-size:18px;">
        ¡Gracias por visitar nuestra app y ser parte del cambio hacia la Transformación Digital! 🚀
    </p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

