CREATE TABLE departments(
id int primary key,
name text, 
did int,
salary int,
country text);

insert into departments(id,name,did,salary,country)VALUES
(1,"Ranveer",123,1000000,"Aus"),
(2,"John",124,500000,"US"),
(3,"Paras",123,500000,"Ind"),
(4,"Ron",123,250000,"UK"),
(5,"Quinlan",124,100000,"Aus");

select did, count(*) from departments group by did;
select did,sum(salary) from departments GROUP by did;
select did, count(*),sum(salary) from departments group by did;
select did, count(*),sum(salary),avg(salary) from departments group by did;
select did, sum(salary) from departments where country="Aus" group by did;
select * from departments order by salary desc;
