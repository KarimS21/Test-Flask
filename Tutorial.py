from flask import Flask,redirect,url_for,render_template,request
import conexion
app = Flask(__name__)

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
        cursor.close()
        conn.close()
    
        print("Datos insertados correctamente.")

        return redirect(url_for("user",usr=nombre))
    else:
        return render_template("index.html")

    

#@app.route("/login",methods=["POST","GET"])
#def login():
#    return render_template()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run()