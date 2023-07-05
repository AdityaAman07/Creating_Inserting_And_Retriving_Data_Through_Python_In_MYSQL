import mysql.connector

def get_users_by_company(company_id):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='Demo_Data'
    )
    cursor = conn.cursor()

    # Execute the SQL query
    query = """
        SELECT userId, userName, email, mobile, password
        FROM user
        WHERE companyId = %s
    """
    cursor.execute(query, (company_id,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Return the list of users
    return rows
