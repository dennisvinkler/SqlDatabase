CREATE SCHEMA `galactic_empire`;

CREATE TABLE galactic_empire.Planets (
    PlanetID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Terrain VARCHAR(100),
    Population BIGINT
);

CREATE TABLE galactic_empire.Characters (
    CharacterID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Age INT
);

CREATE TABLE galactic_empire.Foods (
    FoodID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    EatableByHumans BOOLEAN
);

CREATE TABLE galactic_empire.Ships (
    EngineNumber VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    CrewSize INT
);


INSERT INTO galactic_empire.Planets (Name, Terrain, Population) VALUES
('Tatooine', 'Desert', 200000),
('Coruscant', 'Urban', NULL),
('Hoth', 'Frozen', 0),
('Naboo', 'Grasslands', 450000000),
('Dagobah', NULL, 0);

INSERT INTO galactic_empire.Characters (Name, Gender, Age) VALUES
('Luke Skywalker', 'Male', 23),
('Leia Organa', 'Female', 21),
('Han Solo', 'Male', 30),
('Darth Vader', 'Male', 45),
('Yoda', 'Male', 900),
('Obi-Wan Kenobi', 'Male', 57);

INSERT INTO galactic_empire.Foods (Name, Type, EatableByHumans) VALUES
('Blue Milk', 'Drink', TRUE),
('Bantha Steak', 'Meat', TRUE),
('Yogurt', 'Dairy', NULL),
('Ration Pack', NULL, NULL),
('Spice', 'Seasoning', FALSE);

INSERT INTO galactic_empire.Ships (EngineNumber, Name, CrewSize) VALUES
('Falcon123', 'Millennium Falcon', 4),
('Xwing789', 'X-wing Starfighter', 1),
('TIE456', 'TIE Fighter', 1),
('Slave007', 'Slave I', 1);