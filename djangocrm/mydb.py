# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/ or from CLI >> 
# 'brew install mysql'
# 'brew services restart mysql'
# 'mysql.server start' 
# 'mysql_secure_installation'
# If 'Access Denied' issue: Check here > https://stackoverflow.com/questions/41645309/mysql-error-access-denied-for-user-rootlocalhost
# 'sudo mysql -u root -p" >> 
# Set password for root user
# 'pip install mysql-connector-python'

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '****'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create Database itself
cursorObject.execute("CREATE DATABASE crm_project")

print("ALL DONE")