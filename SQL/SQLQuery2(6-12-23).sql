create database Customers;
use Customers;
create table customers(Cid int,Customer_name varchar(20),contact_name varchar(20),address varchar(20));
insert into customers(Cid,Customer_name,contact_name,address)values('1','Alfred','Maria Anders','Obere str.57');
insert into customers(Cid,Customer_name,contact_name,address)values('2','Trujilo','Ana Trujillo','Avda Constitution');
insert into customers(Cid,Customer_name,contact_name,address)values('3','Antonio','Antonio Moreno','Mataderos 2312');
insert into customers(Cid,Customer_name,contact_name,address)values('4','Around the horn','Thomas Hardy','120 Hanover Sq.');
insert into customers(Cid,Customer_name,contact_name,address)values('5','Berglunds','Christina Berglund','Berguvsvagen 8');

select * from sys.tables;

select * from Customers;

--drop table Customers;

Alter table Customers 
add Salary int;
Update Customers set Salary= '25000' where Cid='1';
Update Customers set Salary= '30000' where Cid='2';
Update Customers set Salary= '50000' where Cid='3';
Update Customers set Salary= '35000' where Cid='4';
Update Customers set Salary= '45000' where Cid='5';

--delete from Customers where Customer_name='NULL';
SELECT DISTINCT salary FROM Customers;

select count(Customer_name) as Total_customers
from Customers
Group by Customer_name;

select count(salary) as Total_salary,salary
from customers
group by salary
HAVING count(salary)>1;

select avg(salary) as Avg_sal,Customer_name
from customers
group by salary,Customer_name
order by salary asc;

select max(salary) as max_sal,Customer_name
from customers
where Cid between '1' and '4'
group by salary,Customer_name
order by salary desc;

select min(salary) from Customers;

Select count(Cid) as total_id
from customers
group by Cid
having count(Cid)>1;

CREATE TABLE Employees (
   ID INT NOT NULL,
   NAME VARCHAR (20) NOT NULL,
   AGE INT NOT NULL,
   ADDRESS CHAR (25),
   SALARY int);

INSERT INTO Employees VALUES 
(1, 'Ramesh', 32, 'Ahmedabad', 2000),
(2, 'Khilan', 25, 'Delhi', 1500),
(3, 'Kaushik', 23, 'Kota', 2000),
(4, 'Chaitali', 25, 'Mumbai', 6500),
(5, 'Hardik', 27, 'Bhopal', 8500),
(6, 'Komal', 22, 'Hyderabad', 4500),
(7, 'Muffy', 24, 'Indore', 10000);

select * from Employees;

delete from Employees where AGE='25';
commit;

begin tran;
delete from Employees where AGE='27';
rollback;

begin tran;
save tran s1;
delete from Employees where ADDRESS='Mumbai';
save tran s2;
delete from Employees where SALARY> '5000';
rollback tran s2;

create table t_employees(id int,name varchar(20),department varchar(20),salary int,experience_yrs int); 
insert into t_employees values
(1,'akash','development',72000,2),
(2,'abishek','production',45000,1),
(3,'pranav','hr',59000,3),
(4,'shubham','accounts',57000,2);

create table t2_employees(id int,name varchar(20),department varchar(20),salary int,experience_yrs int); 
insert into t2_employees values
(1,'prasanth','r&D',72000,1),
(2,'abishek','production',45000,1),
(3,'gautam','development',59000,4),
(4,'rahul','marketing',26000,1);
insert into t2_employees values(5,'john','hr',30000,1);
delete from t2_employees where name ='john';

select * from t_employees;
select * from t2_employees;


SELECT *FROM t_employees UNION SELECT *FROM t2_employees; /*union*/

SELECT name FROM t_employees UNION SELECT name FROM t2_employees;

SELECT *FROM t_employees UNION ALL SELECT *FROM t2_employees;

select *FROM t_employees intersect SELECT *FROM t2_employees;

select *FROM t_employees except SELECT *FROM t2_employees;



/**arthimetic operators**/
select id,name,department,experience_yrs, salary+2000 as updated_salary from t_employees where id between '1' and '3';

select id,name,department,experience_yrs,salary-1000 as deducted_salary from t2_employees
where experience_yrs>1;

select id,name,department,experience_yrs,salary*2 as new_salary from t_employees
where experience_yrs>2;

select id ,name,salary,salary%3 as new_salary from t_employees
where experience_yrs between '1' and '4';

/*data integrity*/
/*default*/
create table Demo(id int,name varchar(50),salary int default 15000);
insert into Demo values(1,'vamsi',10000),
(2,'charan',5000),
(3,'suraj',9000),
(4,'john',default);
select * from Demo;

create table demo1(id int unique,name varchar(50),price int unique);
insert into demo1 values(1,'potato',30),(1,'brinjal',40);

create table demo2(id int not null,age int);
insert into demo2 values(1,25),(null,26);
insert into demo2 values(1,23),(4,27),(5,28);

select * from demo2;

create table demo3(id int primary key,salary int);
insert into demo3 values(4,20000),(4,50000); /** error - primary key doesnt contain duplicates**/
insert into demo3 values(1,3000),(2,4000),(3,4000);
select * from demo3;

create table demo4(id int,name varchar(50),primary key(id,name));

Create table employee(id int primary key,name varchar(50),age int);

Create table company(email varchar(50),address varchar(50),id int primary key foreign key references employee(id));


/**group **/
select max(salary),name
from t2_employees
where department='production'
group by salary,name
order by avg(salary);

select * from t2_employees;



use Customers;

select t_employees.name,t_employees.department,t_employees.salary,t2_employees.experience_yrs 
from t_employees inner join t2_employees on t_employees.id=t2_employees.id;

select t_employees.name,t_employees.department,t_employees.salary,t2_employees.experience_yrs 
from t_employees full outer join t2_employees on t_employees.id=t2_employees.id;



