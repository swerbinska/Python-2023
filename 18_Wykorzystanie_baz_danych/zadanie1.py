# Załadować do bazy danych postgres pythonem zawartość pliku `foods.csv`

import csv
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)
engine.echo = True #to nam daje informacje co sie dzieje jakie relacje miedzy baza a sql

Base.prepare(engine, reflect=True) #dzieki temu mamy juz tabele bo jest reflect
FoodItem = Base.classes.fooditem
session = Session(engine)

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        food_item = FoodItem(name=row["name"], price=row["price"])
        session.add(food_item)
    session.commit()
