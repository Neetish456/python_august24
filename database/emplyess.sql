--create database employees;
--select database();
--use employees;
--select database();
create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);


insert employees(name, designation,technology,phone_num,commission,salary,years_of_exp) values("Neetish" , "C to The E to the O" , "Brains" , 90080069000 , 75000 , 700000 , 20);
insert employees(name, designation,technology,phone_num,commission,salary,years_of_exp) values("Ishwar" , "HR" , "techlead" , 90080069001 , 45000 , 350000 , 10);
insert employees(name, designation,technology,phone_num,commission,salary,years_of_exp) values("Anirudh" , "Lead" , "Design" , 90080069002 , 30000 , 400000, 11);
insert employees(name, designation,technology,phone_num,commission,salary,years_of_exp) values("Ganavi" , "Treasury" , "Finance" , 90080069003 , 50000 , 375000 , 1);
insert employees(name, designation,technology,phone_num,years_of_exp) values("Vinay" , "Intern" , "Front desk" , 90080069004, 69);
insert employees(name, designation,technology,phone_num,commission,salary,years_of_exp) values("Prajnya" , "Project Lead" , "Innovation " , 90080069005 , 25000 , 350000 , 6);

select name, designation from employees;

select distinct name from employees;
select * from employees where salary < 500000 ;
select * from employees where salary < 400000 ;
select * from employees where salary < 300000 ;
select * from employees where salary < 500000 ;
select * from employees where salary > 400000 ;
select * from employees where designation = 'HR';

select * from employees;

UPDATE `neetish_db`.`employees` SET `designation` = 'CEO' WHERE (`id` = '1');
