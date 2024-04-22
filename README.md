Overview
This Python script connects to a MySQL database named Galactic_empire and creates tables to store data related to the Galactic Empire universe. It includes tables for planets, characters, foods, and ships, along with sample data insertion for each table.

Requirements
Python 3.x
mysql-connector-python library (install using pip install mysql-connector-python)
Usage
Ensure that you have a MySQL server running and accessible.
Update the connection parameters in the script (host, user, password, port, database) to match your MySQL server configuration.
Execute the script. It will create the necessary tables if they don't already exist and insert sample data into each table.
Verify that the tables and data have been successfully created and inserted into the database.
Structure
The script uses the mysql.connector module to connect to the MySQL database.
It creates four tables: Planets, Characters, Foods, and Ships, each with appropriate columns to store relevant data.
Sample data is provided for each table to demonstrate usage.
Tables
Planets

Columns: PlanetID, Name, Terrain, Population
Characters

Columns: CharacterID, Name, Gender, Age
Foods

Columns: FoodID, Name, Type, EatableByHumans
Ships

Columns: EngineNumber, Name, CrewSize
Sample Data
Sample data is provided for each table to demonstrate functionality.
Planets, characters, foods, and ships are represented with relevant attributes.
Ensure to adjust or expand the sample data according to your requirements.
License
This project is licensed under the MIT License.


v1.1

Here's the updated summary:

Table Names: The table names were changed from singular to plural for consistency. For example, planet was changed to Planets.
Foreign Key Constraints: Foreign key constraints were added to the character_info table to establish relationships with other tables (planet, food, and ship).
Data Insertion: Sample data was inserted into the character_info table, which now includes foreign key references to planet, food, and ship.
Additional Tables: character_info was added to represent characters with additional attributes like FoodID and ShipEngineNumber.
Data Insertion for New Tables: Sample data was inserted into the food and ship tables.
