import mysql.connector
from create_tables import create_tables
from insert_data import insert_data
from retrieve_data import get_users_by_company

# Call the create_tables function to create the tables
create_tables()

# Call the insert_data function to insert data into the tables
insert_data()

# Call the get_users_by_company function to retrieve users by company
company_id = 1 
users = get_users_by_company(company_id)

# Print the list of users
for user in users:
    print(user)
