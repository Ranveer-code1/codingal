CREATE TABLE salesman(
    seller_id INT PRIMARY KEY,
    seller_name TEXT,
    seller_city TEXT,
    seller_country TEXT
);

CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name TEXT,
    customer_city TEXT,
    seller_id INT
);

CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    order_name TEXT,
    seller_id INT,
    customer_id INT
);

INSERT INTO salesman(seller_id, seller_name, seller_city, seller_country) VALUES 
(123,"Ranveer","Newcastle","Australia"),
(124,"Quinlan","New York City","United States of America"),
(125,"James","Surat","India"),
(126,"Robert","Rome","Italy"),
(127,"Charlie","Paris","France"),
(128,"Jennifer","London","United Kingdom");

INSERT INTO customers (customer_id, customer_name, customer_city, seller_id) VALUES
(112,"Ranveer","Newcastle",123),
(12,"John","New York City",124),
(113,"Mia","Paris",128),
(114,"Shubam","Rome",126),
(115,"James","New Mexico",110),
(116,"Charles","Berlin",110);

INSERT INTO orders(order_id, order_name, seller_id, customer_id) VALUES
(1,"Patek Philippe Calatrava",123,112),
(2,"Jaeger-LeCoultre Reverso",124,12),
(3,"Omega Speedmaster",125,113),
(4,"Cartier Santos",126,114),
(5,"Audemars Piguet Royal Oak",128,113),
(6,"Rolex Daytona",128,113);

SELECT customers.customer_name, customers.customer_city, salesman.seller_name FROM customers JOIN salesman ON customers.customer_city = salesman.seller_city;

SELECT customers.customer_name, customers.customer_city, salesman.seller_name FROM customers JOIN salesman ON salesman.seller_id = customers.seller_id;

SELECT orders.order_id, customers.customer_name FROM orders JOIN customers ON orders.customer_id = customers.customer_id;

SELECT * FROM customers JOIN orders ON orders.customer_id = customers.customer_id WHERE orders.order_name = "Audemars Piguet Royal Oak";
