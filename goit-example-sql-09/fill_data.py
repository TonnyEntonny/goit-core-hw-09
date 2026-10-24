from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 5
NUMBER_TASKS = 10


def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_users = []
    fake_tasks = []

    fake_data = faker.Faker('uk_UA')

    for _ in range(number_users):
        fullname = fake_data.name()
        email = fake_data.unique.email()
        fake_users.append((fullname, email))


    fake_status = [
    ('new',),
    ('in progress',),
    ('completed',)
    ]

    for _ in range(number_tasks):
        title = fake_data.sentence(nb_words=3)
        description = fake_data.text(max_nb_chars=80)
        status_id = randint(1, 3)
        user_id = randint(1, number_users)
        fake_tasks.append((title, description, status_id, user_id))
    return fake_users, fake_status, fake_tasks


def insert_data_to_db(users, status, tasks) -> None:
    # Подключаемся к файлу базы salary (тому самому, который открыт в DBeaver)
    with sqlite3.connect(r"D:\python\Новая папка\sqldz") as con:
        cur = con.cursor()

        cur.execute("PRAGMA foreign_keys = ON;")

        sql_to_users = """INSERT OR IGNORE INTO users(fullname, email) VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        sql_to_status = """INSERT OR IGNORE INTO status(name) VALUES (?)"""
        cur.executemany(sql_to_status, status)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()
        print("База успешно заполнена тестовыми данными!")


if __name__ == '__main__':
    users, statuses, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    insert_data_to_db(users, statuses, tasks)