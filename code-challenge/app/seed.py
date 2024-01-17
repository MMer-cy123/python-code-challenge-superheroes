# from faker import Faker
# from models import db, Hero, Power

# fake = Faker()

# # Seed powers
# print("🦸‍♀️ Seeding powers...")
# powers = [
#     {"name": "super strength", "description": "gives the wielder super-human strengths"},
#     {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
#     {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
#     {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
# ]
# for power_data in powers:
#     power = Power(name=power_data["name"], description=power_data["description"])
#     db.session.add(power)

# db.session.commit()

# # Seed heroes
# print("🦸‍♀️ Seeding heroes...")
# heroes = [
#     {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
#     {"name": "Doreen Green", "super_name": "Squirrel Girl"},
#     {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
#     {"name": "Janet Van Dyne", "super_name": "The Wasp"},
#     {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
#     {"name": "Carol Danvers", "super_name": "Captain Marvel"},
#     {"name": "Jean Grey", "super_name": "Dark Phoenix"},
#     {"name": "Ororo Munroe", "super_name": "Storm"},
#     {"name": "Kitty Pryde", "super_name": "Shadowcat"},
#     {"name": "Elektra Natchios", "super_name": "Elektra"}
# ]
# for hero_data in heroes:
#     hero = Hero(name=hero_data["name"], super_name=hero_data["super_name"])
#     db.session.add(hero)

# db.session.commit()

# # Add powers to heroes
# print("🦸‍♀️ Adding powers to heroes...")
# strengths = ["Strong", "Weak", "Average"]
# all_powers = Power.query.all()

# for hero in Hero.query.all():
#     for _ in range(fake.random_int(min=1, max=3)):
#         power = fake.random_element(all_powers)
#         hero_power = HeroPower(hero=hero, power=power, strength=fake.random_element(strengths))
#         db.session.add(hero_power)

# db.session.commit()

# print("🦸‍♀️ Done seeding!")
from faker import Faker
from app import app
from models import db, Hero, Power, HeroPower
import random

fake = Faker()

with app.app_context():
    # def seed_database():
    powers = [
        {
            "name": "super strength",
            "description": "gives the wielder super-human strengths",
        },
        {
            "name": "flight",
            "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        },
        {
            "name": "super human senses",
            "description": "allows the wielder to use her senses at a super-human level",
        },
        {
            "name": "elasticity",
            "description": "can stretch the human body to extreme lengths",
        },
    ]
    for power_data in powers:
        power = Power(name=power_data["name"], description=power_data["description"])
        db.session.add(power)

    db.session.commit()

    heroes = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"},
    ]
    for hero_data in heroes:
        hero = Hero(name=hero_data["name"], super_name=hero_data["super_name"])
        db.session.add(hero)

    db.session.commit()

    strengths = ["Strong", "Weak", "Average"]
    hero_ids = [hero.id for hero in Hero.query.all()]
    power_ids = [power.id for power in Power.query.all()]
    # all_powers = Power.query.all()

    # for hero in Hero.query.all():
    #   for  i in range(fake.random_int(min=1, max=8)):
    #       power = fake.random_element(all_powers)
    #        hero_power = HeroPower(hero=hero, power=power, strength=fake.random_element(strengths))
    #        db.session.add(hero_power)

    for item in range(5):
        hero_power = HeroPower(
            hero_id=random.choice(hero_ids),
            power_id=random.choice(power_ids),
            strength=random.choice(strengths),
        )
        db.session.add(hero_power)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")
