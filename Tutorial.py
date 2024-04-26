from flask import Flask,redirect,url_for,render_template, request, session
import conexion
app = Flask(__name__)
app.secret_key="hello"

@app.route("/",methods=["POST","GET"])

def home():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        ubicacion = request.form["ubicacion"]
        email = request.form["email"]
        numero = request.form["numero"]
        password = request.form["password"]
        conn = conexion.connect()
        cursor = conn.cursor()
        sql_insert = "INSERT INTO usuario (nombre, apellido, ubicacion, email, numero, password) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nombre,apellido,ubicacion,email,numero,password))
        conn.commit()
        session["nombre"]=nombre.lower()
        cursor.close()
        conn.close()
    
        print("Datos insertados correctamente.")

        return redirect(url_for("nombre"))
    else:
        return render_template("index.html")


@app.route("/nombre")
def nombre():
    if "nombre" in session:
        nombre = session["nombre"]
        return f"<h1>Bienvenido {nombre}</h1>"
    else:
        return redirect("home")
    
#@app.logout("/logout")
#def loguot():
#    session.pop(nombre,None)
#    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)