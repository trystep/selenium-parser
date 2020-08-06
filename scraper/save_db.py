import os

import psycopg2
from psycopg2 import OperationalError
from scraper.parser_excel import parser_content_of_file


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    # Подключимся к БД
    # sudo -u postgres psql
    # \password postgres
    # вводим пароль: postgres
    # Создадим БД
    # CREATE DATABASE db;
    connection = create_connection("db", "postgres", "postgres", "127.0.0.1", "5432")

    # Создадим внутри базы данных таблицу
    create_content_table = "CREATE TABLE IF NOT EXISTS content (id SERIAL PRIMARY KEY, title TEXT NOT NULL, post TEXT NOT NULL)"
    execute_query(connection, create_content_table)

    # Достаем данные для записи из спарсенных файлов и записываем в БД
    list_files=os.listdir(path="results_scraper_post")
    # for file in list_files:
    #     file = "results_scraper_post/"+file
    #     title = parser_content_of_file(file)['title']
    #     post = parser_content_of_file(file)['body_post']
    #     # Вставим запись в таблицу
    #     connection.autocommit = True
    #     cursor = connection.cursor()
    #     sql = "INSERT INTO content (title, post) VALUES (%s, %s);"
    #     cursor.execute(sql, (title, post))

    # Выбор записей из таблицы
    select_content = "SELECT * FROM content"
    content = execute_read_query(connection, select_content)
    # for post in content:
    #     print(post)
    print("Количество записей в БД - "+str(len(content)))
    # Удаление записей таблицы
    # delete_post = "DELETE FROM contents *"
    # execute_query(connection, delete_post)
