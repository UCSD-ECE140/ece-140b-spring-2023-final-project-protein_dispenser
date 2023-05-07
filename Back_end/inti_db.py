import mysql.connector

# Connect to MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

# Create database
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS HealthHive")
cursor.close()

# Connect to HealthHive database
cnx.database = "HealthHive"

# Create users table
cursor = cnx.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
)
""")
cursor.close()

# Create user_info table
cursor = cnx.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_info (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  info VARCHAR(255) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
cursor.close()

# Create user_strings table
cursor = cnx.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  string VARCHAR(255) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

cursor.execute("CREATE TABLE session (id INT)")

cursor.close()


# cursor = cnx.cursor()
# cursor.execute("""
# INSERT INTO users (username, password)
# VALUES
# ('user1', 'password1'),
# ('user2', 'password2'),
# ('user3', 'password3')
# """)
# cnx.commit()
# cursor.close()

# Close MySQL connection
cnx.close()

print("Database created successfully.")
