import mysql.connector

def create_tables():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='Demo_Data'
    )
    cursor = conn.cursor()

    # Create the company table
    create_company_table = """
        CREATE TABLE IF NOT EXISTS company (
            companyId INT PRIMARY KEY,
            companyName VARCHAR(255)
        )
    """
    cursor.execute(create_company_table)

    # Create the user table
    create_user_table = """
        CREATE TABLE IF NOT EXISTS user (
            userId INT PRIMARY KEY,
            userName VARCHAR(255),
            email VARCHAR(255),
            mobile VARCHAR(255),
            password VARCHAR(255),
            companyId INT,
            FOREIGN KEY (companyId) REFERENCES company(companyId)
        )
    """
    cursor.execute(create_user_table)

    # Commit the changes and close the cursor and database connection
    conn.commit()
    cursor.close()
    conn.close()
