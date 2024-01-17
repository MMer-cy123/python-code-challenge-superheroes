# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

class Hero(db.Model,SerializerMixin):

    __tablename__ = 'hero'
    serialize_rules = ("-hero_power.hero")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    hero_powers = db.relationship('HeroPower', backref='hero')

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'super_name': self.super_name,
    #         'created_at': self.created_at,
    #         'updated_at': self.updated_at,
    #         'hero_powers': [hero_power.to_dict() for hero_power in self.hero_powers]
    #     }


class Power(db.Model,SerializerMixin):
    __tablename__ = 'power'
    serialize_rules = ("-hero_power.power")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    hero_powers = db.relationship('HeroPower', backref='power')


class HeroPower(db.Model,SerializerMixin):
    __tablename__ = 'hero_power'
    serialize_rules = ("-hero.hero_power","-power.hero_power")

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), primary_key=True)
    strength = db.Column(db.String(255))

    # hero = db.relationship('Hero', backref=db.backref('hero_powers', cascade='all, delete-orphan'))
    # power = db.relationship('Power', backref=db.backref('power_heroes', cascade='all, delete-orphan'))

    # def to_dict(self):
    #     return {
    #         'hero_id': self.hero_id,
    #         'power_id': self.power_id,
    #         'strength': self.strength
    #     }
