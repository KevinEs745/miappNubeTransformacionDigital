from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <html>
    <head>
        <title>Mi App Nube - Transformación Digital</title>
        <style>
            body {
                background: linear-gradient(to right, #eef2f3, #8e9eab);
                font-family: Arial, sans-serif;
                padding: 40px;
                color: #333;
            }
            h1 {
                color: #2c3e50;
                font-size: 36px;
            }
            h2 {
                color: #27ae60;
            }
            ul {
                font-size: 18px;
                line-height: 1.6;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                max-width: 700px;
                margin: auto;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Proyecto de Transformación Digital</h1>
            <p>Esta aplicación es parte de un proyecto académico en el que aprendimos a desplegar apps web
            en la nube usando <strong>Python (Flask)</strong> y la plataforma <strong>Render</strong>.</p>
            
            <p>El objetivo es demostrar cómo una app sencilla puede estar disponible globalmente en minutos,
            como parte del enfoque de Transformación Digital en las organizaciones.</p>

            <h2>👨‍💻 Equipo de desarrollo:</h2>
            <ul>
                <li>Ernesto Sevilla</li>
                <li>Kevin Eslava</li>
                <li>Juan Tapia</li>
                <li>Paul Vargas</li>
            </ul>

            <p>✅ ¡Gracias por visitar nuestra aplicación y ser parte del cambio digital! 🌍</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

