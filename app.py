from flask import Flask, render_template, request,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail,Message

app = Flask(__name__)

# App Configurations
app.config["SECRET_KEY"] = "my application123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Flask Mail Configurations
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "sharmabruno310@gmail.com"
app.config["MAIL_PASSWORD"] = "retb yloj vqgn gpag"


db = SQLAlchemy(app)
mail = Mail(app)

# Defining Form Model (creating table form with below cols)
class Form(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(60))

@app.route('/',methods=["GET","POST"])
def index():
     if request.method == "POST":
         # print(request.method)
         first_name = request.form["first_name"]
         last_name = request.form["last_name"]
         email = request.form["email"]
         date = request.form["date"]
         date_obj = datetime.strptime(date,"%Y-%m-%d")
         occupation = request.form["occupation"]

         # Insert form data into the database
         form = Form(first_name=first_name,last_name=last_name,email=email,date=date_obj,occupation=occupation)
         db.session.add(form)
         db.session.commit()

         # Create email content
         message_body = f"Thank you for your submission!! {first_name} \n " \
                        f"Here are your details : \n" \
                        f"{first_name} {last_name} \n {email} \n {date}\n {occupation}\n" \
                        f"Take Care!!"

         # Sending the email
         msg = Message(subject="New Form submitted!!",
                       sender = app.config["MAIL_USERNAME"],
                       recipients=[email],
                       body=message_body)
         mail.send(msg)
         flash(f"{first_name} , Your details submitted successfully!","success")

     return render_template("index.html")

if __name__ == "__main__":
    # for creating database
    with app.app_context():
        db.create_all()
    # for running  over all app
    app.run(port=5000,debug=True)