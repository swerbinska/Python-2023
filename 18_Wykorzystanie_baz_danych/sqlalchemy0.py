from sqlalchemy.ext.automap import automap_base #biblioteka dostepna w pythonie; ma ujednolicony poziom stringa
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#powinnismy tez tu uzyc funkcji with
Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url) #teraz tworzymy engine = to co connection - tożsame z with psycopg2.connect(connect_string) as connection: z postgres.py linia 111

# reflect the tables
Base.prepare(engine, reflect=True) #kazemy sie mechanizmom pythona przejrzec z baza danych i sprawdzic co jest; pojawiaja sie klasy jakie sa w bazie danych

# mapped classes are now created with names by default
# matching that of the table name.
FoodItem = Base.classes.fooditem #i tu wyciagamy klase

session = Session(engine) #teraz musimy zrobic session - tworzymy sesje ktora chodzi po enginie

result = session.query(FoodItem).limit(5) #podaj mi pięć fooditemow - i jak to odpalimy to mamy wyprintowaną liste: return f'FoodItem({self.id}, "{self.name}", {self.price})
for row in result:
    print(row.__dict__)

for row in result:
    print('\t|\t'.join( (str(row.id),  str(row.name) , str(row.price))))

    