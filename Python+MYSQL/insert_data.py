import mysql.connector

def insert_data():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='Demo_Data'
    )
    cursor = conn.cursor()

    # Insert data into the company table
    insert_company_data = """
        INSERT INTO company (companyId, companyName)
        VALUES (%s, %s)
    """
    company_data = [
        (1, 'Company A'),
        (2, 'Company B'),
        (3, 'Company C')
    ]
    cursor.executemany(insert_company_data, company_data)

    # Insert data into the user table
    insert_user_data = """
        INSERT INTO user (userId, userName, email, mobile, password, companyId)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    user_data = [
        (1, 'User 1', 'user1@example.com', '1234567890', 'password1', 1),
        (2, 'User 2', 'user2@example.com', '9876543210', 'password2', 1),
        (3, 'User 3', 'user3@example.com', '5678901234', 'password3', 2),
        (4, 'User 4', 'user4@example.com', '4321098765', 'password4', 3)
    ]
    cursor.executemany(insert_user_data, user_data)

    # Commit the changes and close the cursor and database connection
    conn.commit()
    cursor.close()
    conn.close()
