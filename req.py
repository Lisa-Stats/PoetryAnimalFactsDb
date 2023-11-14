import requests
from .poetryanimalfactsdb import app

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
    return cat_data[0]

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
    return dog_data[0]
