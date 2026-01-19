create table if not exists products(
product_id int primary KEY,
product_name text,
product_quantity int,
supplier_id int,
product_price real);
insert into products(product_id,product_name,product_quantity,supplier_id,product_price)Values
(1,"Rolex Daytona",5,1,70000),
(2,"Richard Mille Ferrari",4,3,5000000),
(3,"Patek Philippe grand master chime",1,2,6000000),
(4,"Rolex Submariner",6,4,30000),
(5,"Omega Speedmaster",10,5,5000),
(6,"Omega Seamaster",20,6,4500);
select * from products;
select count(product_id) from products;
select sum(product_price) from products;
select avg(product_quantity) from products;
