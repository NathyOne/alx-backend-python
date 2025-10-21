# Write a function stream_users_in_batches(batch_size) that fetches rows in batches

# Write a function batch_processing() that processes each batch to filter users over the age of25`

# You must use no more than 3 loops in your code. Your script must use the yield generator

# Prototypes:

# def stream_users_in_batches(batch_size)
# def batch_processing(batch_size)


import mysql.connector


def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALX_prodev",
        buffered=False,
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows  # Yield the entire batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over age 25
    """
    for batch in stream_users_in_batches(batch_size):
        users_over_25 = []

        for user in batch:
            if user['age'] > 25:
                users_over_25.append(user)

        yield users_over_25


def main():
    """
    Main function to demonstrate the batch processing
    """
    for filtered_batch in batch_processing(batch_size=6):
        print(f"Batch with {len(filtered_batch)} users over age 25:")
        for user in filtered_batch:
            print(
                f"  - {user['name']}, Age: {user['age']}, Email: {user['email']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
