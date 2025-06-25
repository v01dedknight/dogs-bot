-- Создание базы данных
CREATE DATABASE IF NOT EXISTS dogs_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE dogs_db;

-- Создание таблицы dogs
CREATE TABLE IF NOT EXISTS dogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    birthday DATE,
    gender ENUM('male', 'female'),
    color VARCHAR(100),
    weight DECIMAL(5,2),
    free TINYINT(1),
    delivery TINYINT(1),
    picture1 TEXT,
    picture2 TEXT,
    picture3 TEXT,
    picture4 TEXT,
    picture5 TEXT,
    picture6 TEXT,
    picture7 TEXT,
    picture8 TEXT,
    picture9 TEXT,
    picture10 TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
