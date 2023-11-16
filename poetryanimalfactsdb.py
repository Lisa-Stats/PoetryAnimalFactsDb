import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@postgresql:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(10))
    fact = db.Column(db.Text())

def cat_request():
    cat = requests.get("https://meowfacts.herokuapp.com")
    cat_json = cat.json()
    cat_data = cat_json["data"]
    [single_fact] = cat_data
    with app.app_context():
        fact = Fact(
            animal="cat",
            fact=single_fact
        )
        db.session.add(fact)
        db.session.commit()
    return single_fact

def cat_list():
    with app.app_context():
        cat_facts = Fact.query.order_by(Fact.id.desc()).filter_by(animal="cat").limit(3)
    return cat_facts

def dog_request():
    dog = requests.get("https://dog-api.kinduff.com/api/facts")
    dog_json = dog.json()
    dog_data = dog_json["facts"]
    [single_fact] = dog_data
    with app.app_context():
        fact = Fact(
            animal="dog",
            fact=single_fact
        )
        db.session.add(fact)
        db.session.commit()
    return single_fact

def dog_list():
    with app.app_context():
        dog_facts = Fact.query.order_by(Fact.id.desc()).filter_by(animal="dog").limit(3)
    return dog_facts

@app.route("/")
def main():
    if request.args.get("dog", False) == "Get Dog Fact":
        return render_template("index.html",
                               dog_data=dog_request(), dog_facts=dog_list())
    elif request.args.get("cat", False) == "Get Cat Fact":
        return render_template("index.html",
                               cat_data=cat_request(), cat_facts=cat_list())
    else:
        return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
      db.create_all()
    app.run(debug=True, host="0.0.0.0")
