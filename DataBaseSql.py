# This line imports the mysql.connector module, which is a Python driver for MySQL databases.
import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anna1995',
    port='3306',
   database="Galactic_empire"
)

cursor = database.cursor()

#Initiate this command incase you did not create the new database, after command completed the command can be removed or commented for future use.
#cursor.execute("CREATE DATABASE Galactic_empire")

# SQL statement to create Planets, Characters, Foods, and Ships tables
create_tables_statements = [
    """
    CREATE TABLE IF NOT EXISTS Planets (
        PlanetID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Terrain VARCHAR(100),
        Population BIGINT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Characters (
        CharacterID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Gender VARCHAR(10),
        Age INT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Foods (
        FoodID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Type VARCHAR(50),
        EatableByHumans BOOLEAN
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Ships (
        EngineNumber VARCHAR(20) PRIMARY KEY,
        Name VARCHAR(100),
        CrewSize INT
    )
    """
]


# Here is an example if you want to create table one by one.
# mycursor.execute("CREATE TABLE IF NOT EXISTS Planets (PlanetID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100), Terrain VARCHAR(100), Population BIGINT)")

# Execute each CREATE TABLE statement
for statement in create_tables_statements:
    cursor.execute(statement)


# Sample data for Planets table
planets_data = [
    ('Tatooine', 'Desert', 200000),
    ('Coruscant', 'Urban', None),
    ('Hoth', 'Frozen', 0),
    ('Naboo', 'Grasslands', 450000000),
    ('Dagobah', None, 0)
]

# Sample data for Characters table
characters_data = [
    ('Luke Skywalker', 'Male', 23),
    ('Leia Organa', 'Female', 21),
    ('Han Solo', 'Male', 30),
    ('Darth Vader', 'Male', 45),
    ('Yoda', 'Male', 900),
    ('Obi-Wan Kenobi', 'Male', 57)
]

# Sample data for Foods table
foods_data = [
    ('Blue Milk', 'Drink', True),
    ('Bantha Steak', 'Meat', True),
    ('Yogurt', 'Dairy', None),
    ('Ration Pack', None, None),
    ('Spice', 'Seasoning', False)
]

# Sample data for Ships table
ships_data = [
    ('Falcon123', 'Millennium Falcon', 4),
    ('Xwing789', 'X-wing Starfighter', 1),
    ('TIE456', 'TIE Fighter', 1),
    ('Slave007', 'Slave I', 1)
]

# Execute INSERT INTO statements to insert sample data into each table
cursor.executemany("INSERT INTO Planets (Name, Terrain, Population) VALUES (%s, %s, %s)", planets_data)
cursor.executemany("INSERT INTO Characters (Name, Gender, Age) VALUES (%s, %s, %s)", characters_data)
cursor.executemany("INSERT INTO Foods (Name, Type, EatableByHumans) VALUES (%s, %s, %s)", foods_data)
cursor.executemany("INSERT INTO Ships (EngineNumber, Name, CrewSize) VALUES (%s, %s, %s)", ships_data)


database.commit()