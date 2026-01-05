create table salesman1(
sid int primary KEY,
sname text,
samount text,
ssales int);
Insert into salesman1(sid,sname,samount,ssales) values
(1,"Raj","$2000",20),
(2,"Ranveer","$1100",11),
(3,"Mason","$990",10),
(4,"Ram","$9900",99),
(5,"Phoenex","$2300",23),
(6,"Aurelia","$2600",26),
(7,"Maggie","$3500",35);
select sname from salesman1;
select * from salesman1 where sname="Ranveer";
