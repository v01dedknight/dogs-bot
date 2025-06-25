USE dogs_db;

-- Тестовые данные
INSERT INTO dogs (name, birthday, gender, color, weight, free, delivery, picture1) VALUES
('Бобик', '2020-05-15', 'male', 'коричневый', 15.50, 1, 0, 'https://example.com/dogs/bobik1.jpg'),
('Мурка', '2019-08-10', 'female', 'чёрный', 12.30, 0, 1, 'https://example.com/dogs/murka1.jpg'),
('Шарик', '2021-01-20', 'male', 'белый', 10.00, 1, 1, 'https://example.com/dogs/sharik1.jpg');