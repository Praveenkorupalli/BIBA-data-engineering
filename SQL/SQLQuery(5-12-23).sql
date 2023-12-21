create table employee_details(id int,name varchar(20),age varchar(30),city varchar(20), salary varchar(20));
insert into employee_details(id,name,age,city,salary) VALUES('101','john','26','chennai','25000');
insert into employee_details(id,name,age,city,salary) VALUES('102','ram','26','chennai','30000');
insert into employee_details(id,name,age,city,salary) VALUES('103','sri','26','chennai','50000');
insert into employee_details(id,name,age,city,salary) VALUES('104','snow','26','chennai','30000');
insert into employee_details(id,name,age,city,salary) VALUES('105','sam','26','chennai','25000');

Select * FROM sys.tables;  /*show tables*/

select * from employee_details; 
USE Employee;
alter table employee_details 
add branch varchar;

alter table employee_details
drop column branche,branches;
select * from employee_details;

truncate table employee_details;

select * from employee_details;

update employee_details set age='25' where id='105';

delete from employee_details where id ='104';

select name from employee_details order by age desc;
use Employee;

create table employee_status(id int,working_status varchar(10),experience varchar(20));
insert into employee_status(id,working_status,experience)values('101','working','5yrs');
insert into employee_status(id,working_status,experience)values('102','notworking','4yrs');
insert into employee_status(id,working_status,experience)values('103','working','3yrs');
insert into employee_status(id,working_status,experience)values('104','notworking','7yrs');
insert into employee_status(id,working_status,experience)values('105','working','4yrs');
insert into employee_status(id,working_status,experience)values('106','notworking','2yrs');
select * from employee_status;


select distinct id,experience from employee_status; /*individual values*/

update employee_status set working_status = 'working' where experience > '2yrs'; /*updation*/
select * from employee_status;

select id from employee_status order by experience asc;

select * from employee_details join employee_status on employee_details.id=employee_status.id;

select employee_details.id,employee_details.name,employee_details.age,employee_status.working_status,employee_status.experience
from employee_details inner join employee_status on employee_details.id = employee_status.id;

select employee_details.id,employee_details.name,employee_details.age,employee_details.salary,employee_status.working_status,employee_status.experience
from employee_details right join employee_status on employee_details.id = employee_status.id;

select employee_details.id,employee_details.name,employee_details.salary,employee_status.working_status,employee_status.experience
from employee_details left join employee_status on employee_details.id = employee_status.id;

select employee_details.id,employee_details.name,employee_details.salary,employee_status.working_status,employee_status.experience
from employee_details right join employee_status on employee_details.id = employee_status.id
union
select employee_details.id,employee_details.name,employee_details.salary,employee_status.working_status,employee_status.experience
from employee_details left join employee_status on employee_details.id = employee_status.id

select count(salary) as total_count from employee_details
group by salary;

select * from employee_details where salary>'30000';

select * from employee_details where city='chennai' and age='25';


SELECT * FROM employee_details WHERE name NOT LIKE 's%';

select * from employee_details where salary>'30000' or age='25';

select * from employee_status where experience between '4yrs' and '7yrs';