import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    port='3306',
    database="Galactic_empire"
)
cursor = database.cursor()

# Create planet table
create_planet_table = """
    CREATE TABLE IF NOT EXISTS planet(
        PlanetID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Terrain VARCHAR(100),
        Population BIGINT
    )
"""
cursor.execute(create_planet_table)

# Insert data into planet table
insert_planet_data = """
    INSERT INTO planet (Name, Terrain, Population) VALUES (%s, %s, %s)
"""
planet_data = [
    ('Tatooine', 'Desert', 200000),
    ('Coruscant', 'Urban', None),
    ('Hoth', 'Frozen', 0),
    ('Naboo', 'Grasslands', 450000000),
    ('Dagobah', None, 0)
]
cursor.executemany(insert_planet_data, planet_data)

# Create food table
create_food_table = """
    CREATE TABLE IF NOT EXISTS food(
        FoodID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Type VARCHAR(50),
        EatableByHumans BOOLEAN
    )
"""
cursor.execute(create_food_table)

# Insert data into food table
insert_food_data = """
    INSERT INTO food (Name, Type, EatableByHumans) VALUES (%s, %s, %s)
"""
food_data = [
    ('Blue Milk', 'Drink', True),
    ('Bantha Steak', 'Meat', True),
    ('Yogurt', 'Dairy', None),
    ('Ration Pack', None, None),
    ('Spice', 'Seasoning', False)
]
cursor.executemany(insert_food_data, food_data)

# Create ship table
create_ship_table = """
    CREATE TABLE IF NOT EXISTS ship(
        EngineNumber VARCHAR(20) PRIMARY KEY,
        Name VARCHAR(100),
        CrewSize INT,
        PlanetID INT,
        FOREIGN KEY (PlanetID) REFERENCES planet(PlanetID)
    )
"""
cursor.execute(create_ship_table)

# Insert data into ship table
insert_ship_data = """
    INSERT INTO ship (EngineNumber, Name, CrewSize, PlanetID) VALUES (%s, %s, %s, %s)
"""
ship_data = [
    ('Falcon123', 'Millennium Falcon', 4, 1),
    ('Xwing789', 'X-wing Starfighter', 1, 2),
    ('TIE456', 'TIE Fighter', 1, 3),
    ('Slave007', 'Slave I', 1, 4)
]
cursor.executemany(insert_ship_data, ship_data)

# Create character_info table
create_character_table = """
    CREATE TABLE IF NOT EXISTS character_info(
        CharacterID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Gender VARCHAR(10),
        Age INT,
        PlanetID INT,
        FoodID INT,
        ShipEngineNumber VARCHAR(20),
        FOREIGN KEY (PlanetID) REFERENCES planet(PlanetID),
        FOREIGN KEY (FoodID) REFERENCES food(FoodID),
        FOREIGN KEY (ShipEngineNumber) REFERENCES ship(EngineNumber)
    )
"""
cursor.execute(create_character_table)

# Sample data for character_info table
character_info_data = [
    ('Luke Skywalker', 'Male', 23, 1, 1, 'Falcon123'),  # Name, Gender, Age, PlanetID, FoodID, ShipEngineNumber
    ('Leia Organa', 'Female', 21, 2, 2, 'Xwing789'),
    ('Han Solo', 'Male', 30, 3, 3, 'TIE456'),
    ('Darth Vader', 'Male', 45, 4, 4, 'Slave007'),
    ('Yoda', 'Male', 900, 1, 5, 'Falcon123'),
    ('Obi-Wan Kenobi', 'Male', 57, 5, 1, 'Xwing789'),
    ('Ahsoka', 'Female', 17, 1, 2, 'TIE456'),
    ('Mandalorian', 'Male', 35, 2, 3, 'Slave007'),
    ('Andor', 'Male', 32, 3, 4, 'Falcon123')
]

# Insert sample data into character_info table
insert_character_info_data = """
    INSERT INTO character_info (Name, Gender, Age, PlanetID, FoodID, ShipEngineNumber)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_character_info_data, character_info_data)



database.commit()
