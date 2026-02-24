from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# setup database file location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# define the model for the form data
class FormData(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True)

# create the database and tables
with app.app_context():
    db.create_all()

@app.route("/")
def form_sample():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == 'POST':
        name = request.form.get("name")
        user_email = request.form.get("email")

        new_data = FormData(username=name, email=user_email)
        db.session.add(new_data)
        db.session.commit()

    return render_template("submit.html", user_name=name)

if __name__ == "__main__":
    app.run(debug=True)
