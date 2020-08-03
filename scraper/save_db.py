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
    connection = create_connection("postgres", "postgres", "postgres", "127.0.0.1", "5432")

    # Внутри дефолтной БД postgres создаем базу данных db
    # create_database_query = "CREATE DATABASE db"
    # create_database(connection, create_database_query)

    # Создадим внутри базы данных db таблицу content
    create_content_table = "CREATE TABLE IF NOT EXISTS content (id SERIAL PRIMARY KEY,title TEXT NOT NULL,post TEXT NOT NULL)"
    execute_query(connection, create_content_table)


    # Достаем данные для записи из спарсенных файлов
    file = "results_scraper_post/94_Элемент выбора меню застрял на экране после закрытия контекстного или командного меню.xlsx"
    title = parser_content_of_file(file)['title']
    body_post=parser_content_of_file(file)['body_post']


    # Вставим запись в таблицу content
    content = [
        (title, body_post)
    ]
    content_records = ", ".join(["%s"] * len(content))
    insert_query = (
        f"INSERT INTO content (title, post) VALUES {content_records}"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, content)

    # Выбор записей из таблицы
    select_users = "SELECT * FROM content"
    content = execute_read_query(connection, select_users)

    for post in content:
        print(post)

    # Удаление записей таблицы
    # delete_post = "DELETE FROM content WHERE id = 3"
    # execute_query(connection, delete_post)


