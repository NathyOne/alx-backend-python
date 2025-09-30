import mysql.connector


def stream_users(query, host='localhost', user='root', password='', database=''):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        buffered=False,
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)

    while True:
        rows = cursor.fetchmany(6)
        if not rows:
            break
        for row in rows:
            yield row

    cursor.close()
    connection.close()


for row in stream_rows(
    query="SELECT * FROM user_data LIMIT 6",
    host="localhost",
    user="root",
    password="root",
    database="ALX_prodev"
):
    print(f"Name: {row['name']}, Email: {row['email']}")
