import mysql.connector


def stream_user_ages():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALX_prodev"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    while True:
        rows = cursor.fetchmany(100)
        if not rows:
            break
        for row in rows:
            yield row[0]
    cursor.close
    connection.close


def calculate_average_age():
    total_age = 0
    count = 0

    # Loop 1: Iterate through ages from generator
    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0  # Avoid division by zero

    return total_age / count


# Main execution
if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
