CREATE TABLE DXC_Customers(
    num INT PRIMARY KEY,
    Company_name TEXT,
    City TEXT,
    Grade INT,
    Value TEXT);
INSERT INTO DXC_Customers(num, Company_name, City, Value, Grade) VALUES
(1, "Cartier", "Paris", "10.5 Billion", 105),
(2, "Rolex", "Geneve", "9.1 Billion", 104),
(3, "Omega", "La Chaux-de-Fonds", "6.735 Billion", 103),
(4, "Patek Philippe", "Geneve", "4.9 Billion", 102),
(5, "Audermars Piguet", "Le Brassus", "4.8 Billion", 99),
(6, "Breitling", "Saint-Imier", "4.5 Billion", 98),
(7, "JPMorgan", "New York City", "842.48 Billion", 200);
SELECT * FROM DXC_Customers;
SELECT * FROM DXC_Customers WHERE Grade >= 100;
SELECT * FROM DXC_Customers WHERE Grade >= 100 AND City = "New York City";
