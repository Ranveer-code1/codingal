CREATE TABLE DXC_company2 (
    id INT PRIMARY KEY,
    name TEXT,
    salary INT,
    role TEXT,
    status TEXT
);

INSERT INTO DXC_company2 (id, name, salary, role, status) VALUES
(1,"Ranveer",1000000,"CEO","approved"),
(2,"Raj",750000,"CFO","suspect"),
(3,"Quinlan",500000,"COO","approved"),
(4,"Phoenix",500000,"CFO","approved"),
(5,"Aurelia",500000,"CMO","approved"),
(6,"Jacob",500000,"CTO","approved"),
(7,"Michael",500000,"CIO","approved"),
(9,"Zoe",500000,"HR Manager","approved"),
(10,"Rosie",250000,"Sales Manager","approved"),
(11,"Rosette",100000,"Tech Officer","approved"),
(12,"Madison",100000,"Tech Officer","suspect"),
(13,"Emma",100000,"Tech Officer","suspect"),
(14,"Hannah",100000,"Tech Officer","approved"),
(15,"Olivia",100000,"Tech Officer","approved"),
(16,"Issabelle",100000,"Tech Officer","suspect"),
(17,"Izzy",100000,"Tech Officer","approved"),
(18,"Sam",100000,"Tech Officer","approved"),
(19,"Abigail",80000,"HR","approved"),
(20,"Avery",80000,"HR","approved"),
(21,"Will",80000,"HR","suspect"),
(22,"Andrew",80000,"HR","approved"),
(23,"Chris",80000,"HR","suspect"),
(24,"Daniel",80000,"HR","approved"),
(25,"Mathew",50000,"Sales","suspect"),
(26,"Ethan",50000,"Sales","approved"),
(27,"Ashley",50000,"Sales","approved"),
(28,"Ron",50000,"Sales","suspect"),
(29,"Indiana",50000,"Sales","approved"),
(30,"William",50000,"Sales","approved");
select * from DXC_company2;
select name,salary from DXC_company2 where salary=(select min(salary)from DXC_company2);
select name,salary from DXC_company2 where salary=(select max(salary)from DXC_company2);
select count(id) from DXC_company2;
select sum(salary) from DXC_company2;
select avg(salary) from DXC_company2;
