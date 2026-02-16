create table restaurant1 (
id int primary key,
name text,
cuisine text,
price int,
review int);

insert into restaurant1(id,name,cuisine,price,review)values
(1,"Miine","Italian",100,5),
(2,"Rocket","Asian",50,3),
(3,"Dominos","Italian",25,4),
(4,"Miine","Italian",100,5),
(5,"MacDonalds","American",10,4);

select * from restaurant1;
select DISTINCT cuisine from restaurant1;
select DISTINCT name from restaurant1;
select * from restaurant1 where cuisine="Italian";
select * from restaurant1 where review>4
select 