
create table Watches (
id int primary key,
name text,
company text,
price int,
review int);

insert into Watches(id,name,company,price,review)values
(1,"Rolex Submariner","Rolex",19500,9),
(2,"Omega Speedmaster","Omega",10000,8),
(3,"Audemars Piguet Royal Oak","Audemars Piguet",75000,9.3),
(4,"Audemars Piguet Royal Oak","Audemars Piguet",75000,9.3),
(5,"Jaeger-LeCoultre Reverso","Jaeger-LeCoultre",5000,8.7);

select * from Watches;
select DISTINCT company from Watches;
select DISTINCT name from Watches;
select * from Watches where company="Jaeger-LeCoultre" and price=5000;
select * from Watches where name like "%Jaeger-LeCoultre%";
select * from Watches order by review desc limit 3;
