create table students(id int,name varchar(20),class int,marks int);
insert into students values(1,'rahul',8,45),
(2,'sai',8,65),(3,'ganesh',10,75),(4,'ram',8,85),(5,'shankar',6,55);

create table grades(id int,grade varchar(20));

insert into grades values(1,'D'),(2,'C'),(3,'B'),(4,'A'),(5,'C'),(6,'A');

select * from students;
select * from grades;



select students.id,students.name,students.class,students.marks,grades.grade
from students inner join grades on students.id=grades.id;


select students.id,students.name,students.class,students.marks,grades.grade
from students right join grades on students.id=grades.id;

select students.id,students.name,students.class,students.marks,grades.grade
from students left join grades on students.id=grades.id;

select students.id,students.name,students.class,students.marks,grades.grade
from students full join grades on students.id=grades.id;

select students.id,students.name,students.class,students.marks,grades.grade
from students inner join grades on students.id=grades.id
where marks>65;

select students.id,students.name,students.class,students.marks,grades.grade
from students inner join grades on students.id=grades.id
where name like 's%';

select name,class,marks from students where exists(select id from grades where students.id=grades.id and grade between 'A' and 'C');

select name,class,marks from students
where id= any(select id from grades where students.id=grades.id);

select name,class,marks from students
where id in(select id from grades
							where grade between 'B' and 'C');

delete from students 
where id in (select id from grades
				where grade='C');

select * from students;

update students set name='Ravindra'
where id in (select id from grades where marks='45');

select * from students;

/**Question-2**/
create table employees(id int,name varchar(20),department varchar(20),location varchar(20),salary int);
insert into employees values(1,'john','salesforce','chennai',30000),
(2,'alex','testing','chennai',27000),	
(3,'robert','development','chennai',45000),	
(4,'shyam','testing','chennai',25000),	
(5,'peter','devops','chennai',50000),	
(6,'ben','datascience','chennai',40000),	
(7,'stella','salesforce','chennai',30000);

select * from employees;

alter table employees
add bonus int;

update employees
set bonus='25000'
where department='testing';

select * from employees;


update employees 
set location='banglore'
where id between '1' and '4';

select * from employees;

delete from employees
where bonus is null;

insert into employees values(1,'john','salesforce','mumbai',30000,2000),
(3,'john','hr','mumbai',43000,10000),
(5,'john','testing','chennai',30000,5000),
(6,'john','data analyst','pune',50000,4000);

select * from employees;

update employees
set id ='1' where department='testing';

update employees
set name='stella' where department='hr';

select * from employees;

update employees
set name='lexi' where bonus='5000';

update employees
set name='Rob' where salary='50000';

select name,max(salary) as max_salary
from employees
group by name;

select name,min(salary) as min_salary
from employees
where id between '1' and '4'
group by name,id;


select id,name,avg(salary) as avg_salary
from employees
group by name,id
having count(id)=1;



select id,name,avg(salary) as avg_salary
from employees
group by name,id
having count(id)=1
order by name asc;













