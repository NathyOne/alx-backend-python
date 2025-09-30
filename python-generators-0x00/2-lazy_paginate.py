import mysql.connector


def paginate_users(page_size, offset):
    """
    Fetches a specific page of users from the database
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s",
                   (page_size, offset))

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users


def lazy_paginate(page_size):
    """
    Generator that lazily loads each page of users when needed
    Starts at offset 0 and increments by page_size
    """
    offset = 0

    while True:
        # Fetch the next page only when needed
        page = paginate_users(page_size, offset)

        # If no users returned, we've reached the end
        if not page:
            
            break

        # Yield the current page
        yield page

        # Move to next page
        offset += page_size

# Usage with only ONE loop


def main():
    """
    Main function demonstrating lazy pagination with one loop
    """
    # Only ONE loop in the entire code
    for page in lazy_paginate(page_size=6):
        print(f"Page with {len(page)} users:")
        for user in page:
            print(f"  - {user['name']}, Age: {user['age']}")
        print("--- End of Page ---\n")


if __name__ == "__main__":
    main()
