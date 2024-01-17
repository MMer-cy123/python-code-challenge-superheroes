#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS


from models import db, Hero, Power, HeroPower


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome</h1>'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = []
    for hero in Hero.query.all():
        hero = {
            "id" : hero.id,
            "name": hero.name, 
            "super_name": hero.super_name
            }
        result.append(hero)
    return jsonify(result)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.filter_by(id=id).first()
    if hero:
        return jsonify(hero.to_dict()),200
    else:
        return jsonify({'message': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    result = []
    for power in powers:
        power={
            "id": power.id,
        "name": power.name,
        "description": power.description,
        "created_at": power.created_at,
        "updated_at" : power.updated_at
        }
        result.append(power)
    return jsonify(result)

@app.route('/powers/<id>/', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({'message': 'Power not found'}), 404

@app.route('/powers/<id>/', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        name = request.json.get('name')
        description = request.json.get('description')

        if name is not None:
            power.name = name
        if description is not None:
            power.description = description

        db.session.commit()
        return jsonify(power.to_dict())
    else:
        return jsonify({'message': 'Power not found'}), 404

@app.route('/hero_powers', methods=['POST'])
def add_hero():
    data = request.form
    

    # if id is not None and hero_powers is not None:
    hero = HeroPower(
        strength = data.get('strength'),
        power_id = data.get('power_id'),
        hero_id = data.get('hero_id')
        
        
        )
    db.session.add(hero)
    db.session.commit()
    return jsonify(hero.to_dict())
    # else:
    #     return jsonify({'message': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(port=5500)
    # seed_database()
