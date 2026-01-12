create table student(
rno int primary key,
name text,
subject text,
city text);
insert into student(rno,name,subject,city) values
(1,"Ranveer","Coding","Newcastle"),
(2,"Rajveer","Maths","London"),
(3,"Quinlan","Science","Washington"),
(4,"Mason","English","Sydney"),
(5,"Lachlan","STEM","Berlin");
select * from student;
select * from student where name="Ranveer" and subject="Coding";
select * from student where subject="STEM" or rno=1546;
select * from student where name="Quinlan" and (subject="Science" or subject="English");
