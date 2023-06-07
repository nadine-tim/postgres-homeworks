"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def connection_to_db():
    """
    Подключение и запись в БД
    """

    path = ["north_data/customers_data.csv", "north_data/employees_data.csv", "north_data/orders_data.csv"]
    query = ["insert into customers values (%s, %s, %s)",
             "insert into employees values (%s, %s, %s, %s, %s, %s)",
             "insert into orders values (%s, %s, %s, %s, %s)"]

    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='pgadmin')
    cur = conn.cursor()

    try:
        for i in range(len(path)):
            with open(path[i], 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute(query[i], row)
            conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    connection_to_db()
