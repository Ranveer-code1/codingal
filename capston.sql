create table salesman(
sid int primary key,
sname text,
scity text,
scountry text);
insert into salesman(sid,sname,scity,scountry) values 
(123,"Ranveer","Newcastle","Australia"),
(124,"Quinlan","New York City","United States of America"),
(125,"Myra","Surat","India"),
(126,"Shubam","Rome","Italy"),
(127,"Charlie","Paris","France");

create table customers(
cid int primary KEY,
cname text,
ccity text,
sid int);
insert into customers (cid,cname,ccity,sid) VALUES
(112,"Ranveer","Newcastle",123),
(12,"Quinlan","New York City",1213),
(113,"Mia","Paris",128),
(114,"Shubam","Rome",126),
(115,"Charles","New Mexico",110);

create table orders(
oid int primary KEY,
oname text,
sid int,
cid int);
insert into orders(oid,oname,sid,cid)VALUES
(1,"Grand master-chime",123,112),
(2,"Nautilous",13,1),
(3,"Submariner",121,142),
(4,"Royal oak" ,126,114),
(5,"Daytona",113,128);

select customers.cname,customers.ccity,salesman.sname from customers join salesman on customers.ccity==salesman.scity;
select customers.cname,customers.ccity,salesman.sname from customers join salesman on salesman.sid==customers.sid;
select orders.oid,customers.cname from orders join customers where orders.cid==customers.cid;
select * from customers join orders on orders.cid==customers.cid where oname="Grand master-chime";
