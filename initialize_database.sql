DROP DATABASE cars_api;
CREATE DATABASE cars_api;
\c cars_api;

CREATE TABLE cars(
    id  SERIAL PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL UNIQUE
);

-- INSERT INTO cars(brand, model) VALUES('audi', 'A4')
-- INSERT INTO cars(brand, model) VALUES('mercedes', 'S-class')
-- INSERT INTO cars(brand, model) VALUES('mercedes', 'E-class')
-- INSERT INTO cars(brand, model) VALUES('mercedes', 'A-class')
-- INSERT INTO cars(brand, model) VALUES('bmw', 'x-5')
-- INSERT INTO cars(brand, model) VALUES('bmw', 'x-7')

INSERT INTO cars(brand, model) VALUES('audi', 'A4'),
('mercedes', 'S-class'),
('mercedes', 'E-class'),
('mercedes', 'A-class'),
('bmw', 'x-5'),
('bmw', 'x-7')