from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
     if request.method == "POST":
         # print(request.method)
         first_name = request.form["first_name"]
         last_name = request.form["last_name"]
         email = request.form["email"]
         occupation = request.form["occupation"]

     return render_template("index.html")

app.run(port=5000,debug=True)