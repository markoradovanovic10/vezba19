
from faker import Faker
from db import connect
from datetime import datetime

fake = Faker()

genres = ["Mystery", "Fantasy", "Sci-Fi", "Romance", "Horror"]
adjectives = ["Dark", "Fantastic", "Epic", "Legendary", "Hidden", "Enternal"]
nouns = ["Secret", "Kingdom", "Journey", "Realm", "Legacy", "Shadow"]

def generate_book_title():
    genre = fake.random_element(genres)
    adjective = fake.random_element(adjectives)
    noun = fake.random_element(nouns)
    name = fake.name()
    book_name = adjective + " " + noun
    date = fake.date_between(start_date=datetime(1950,1,1), end_date=datetime(2020,1,1))
    return book_name, genre, name, date

def insert_user(connect, name, date):
    cursor = connect.cursor()
    query_users = "INSERT INTO users (name, dob) VALUES (%s, %s)"
    cursor.execute(query_users, (name, date))
    connect.commit()
    cursor.close()

def check_user(connect, name, dob):
    cursor = connect.cursor()
    query_users = "SELECT * FROM users WHERE name = %s and dob = %s"
    cursor.execute(query_users, (name, dob,))
    user = cursor.fetchone()
    return user

def insert_book(connect, name, category, author):
    cursor = connect.cursor()
    query = "INSERT INTO books (name, category, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, category, author))
    connect.commit()
    cursor.close()


book_name, genre, name, date = generate_book_title()
if not check_user(connect, name, date):
    insert_user(connect, name, date)
insert_book(connect, book_name, genre, name)








