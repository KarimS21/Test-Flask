from flask import Flask, redirect, url_for, render_template, request, session, Response
import conexion

app = Flask(__name__)
app.secret_key = "hello"

def validar_datos(nombre, apellido, ubicacion, email, numero, password):
    # Verifica que ningún campo esté vacío
    if not all([nombre, apellido, ubicacion, email, numero, password]):
        return False
    # Puedes agregar más condiciones de validación aquí si es necesario
    return True

@app.route("/", methods=["POST", "GET"])
def home():
    mensaje_error = None  # Inicializa la variable para el mensaje de error
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        ubicacion = request.form["ubicacion"]
        email = request.form["email"]
        numero = request.form["numero"]
        password = request.form["password"]
        
        # Validar los datos
        if validar_datos(nombre, apellido, ubicacion, email, numero, password):
            conn = conexion.connect()
            cursor = conn.cursor()
            sql_insert = "INSERT INTO usuario (nombre, apellido, ubicacion, email, numero, password) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_insert, (nombre, apellido, ubicacion, email, numero, password))
            conn.commit()
            session["nombre"] = nombre.lower()
            cursor.close()
            conn.close()
            return render_template("index.html")
        else:
            mensaje_error = "Todos los campos son obligatorios. Por favor, completa toda la información."

    return render_template("index.html", error=mensaje_error)

if __name__ == "__main__":
    app.run(debug=True)
