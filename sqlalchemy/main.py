# import SQL Alchemy libraries
# create_ engine to name a db file
# Foreing Key to make relations between tables
# columns to name column in the table
# String for setting data type to text, number, character
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
# declarative base make the Classes connected
from sqlalchemy.ext.declarative import declarative_base
# session maker adds data to the db and commits to push the data in db
from sqlalchemy.orm import sessionmaker

# Base class to connect Classes the alchemy way
Base = declarative_base()

# make classes for each table put in table name and column properties
class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    # class init method to make above  objects 
    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    # represent function to format the data when called in query
    # important to make correct spelling otherwise you will find this out at 0300hrs at night
    def __repr__(self):
        return f'({self.ssn})({self.firstname}) ({self.lastname}),({self.gender}),({self.age})'

class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid", Integer, primary_key = True)
    description = Column ("descripiton", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner
    
    def __repr__(self):
        return f'({self.tid}) ({self.description}) owned by ({self.owner})'

# making sqlite conneciton and making engine variable name the db   
engine = create_engine("sqlite:///mydb2.db", echo = True)
# create all the connected classes through Base means make all tables mentioned above
Base.metadata.create_all(bind=engine)
# session class is actually making CURD queries in db
Session = sessionmaker(bind=engine)
# set it to sessions
session = Session()
# add data to persons table
##query setup
p1 = Person(1231,'awesss','aakhtar','m',34)
p2 = Person(1232,'awessss','aaakhtar','m',33)
p3 = Person(1233,'awesssss','aaaakhtar','m',39)
p4 = Person(1234,'awessssss','akhaaatar','m',3)
 ## Qeury into db
session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

# push query in db
session.commit()

t1 = Thing(1, "car", p1.ssn)
t2 = Thing(2, "bike", p4.ssn)
t3 = Thing(3, "laptop", p1.ssn)
t4 = Thing(4, "watch", p4.ssn)
t5 = Thing(5, "money", p3.ssn)
t6 = Thing(6, "racket", p2.ssn)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.add(t6)
session.commit()

# check output
results = session.query(Thing).all()
print(results)

results2 = session.query(Person).all()
print(results2)