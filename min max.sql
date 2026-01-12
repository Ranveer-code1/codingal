create table if not exists products(
num int primary key,
pro_name text,
price int);
insert into products(num,pro_name,price)VALUES
(1,"Patak phlippe grandmaster chime ",32000000),
(2,"Ferrari 250 GTO",75000000),
(3,"Rolex Submariner hulk",30000),
(4,"Buggati Chiron ",1200000),
(5,"Richard Mille Emerald ",6000000);
select pro_name,price from products where price=(select min(price)from products);
select pro_name,price from products where price=(select max(price)from products);
drop table products;
select * from products;
