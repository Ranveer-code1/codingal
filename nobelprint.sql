create table if not exists nobelwin(
id int primary KEY,
name text,
age int,
subject text,
catagory text,
year int);

insert into nobelwin(id,name,age,subject,catagory,year) VALUES
(1,"Ranveer",12,"Coding","SQL",2026),
(2,"Quinlan",11,"Maths","Algebra",2026),
(3,"Ankit",12,"Science","Fusion",2026),
(4,"Arjun",12,"English","Essay",2026),
(5,"Paras",11,"Applied technology","Woodworks",2026);

select * from nobelwin where name like "A%";
