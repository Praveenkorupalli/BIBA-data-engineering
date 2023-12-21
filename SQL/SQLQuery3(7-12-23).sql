create database joins;
use joins;

create table students(id int,name varchar(20),class int,marks int);
insert into students values(1,'abhi',8,90),(2,'ram',9,80),(3,'rahul',10,75),(4,'sai',7,85),(5,'varma',5,95);

create table student_grades(id int,grade varchar(5));
insert into student_grades values(1,'A'),(2,'B'),(3,'c'),(4,'A'),(5,'A+'),(6,'D');

select students.name,students.class,students.marks,student_grades.grade 
from students inner join student_grades on students.id=student_grades.id;


select * from students;


select * from student_grades;


insert into students values(7,'murali',9,'69');
select students.id,students.name,students.class,students.marks,student_grades.grade 
from students left join student_grades on students.id=student_grades.id;

select students.name,students.class,students.marks,student_grades.grade 
from students right join student_grades on students.id=student_grades.id;

select students.name,students.class,students.marks,student_grades.grade 
from students full join student_grades on students.id=student_grades.id;

select students.name,students.class,students.marks ,student_grades.grade
from students cross join student_grades ;
 

/** Equi join**/
select students.id,students.name,students.class,students.marks,student_grades.grade 
from students,student_grades where students.id=student_grades.id;
                             /*or*/
select students.name,students.class,students.marks,student_grades.grade 
from students  join student_grades on students.id=student_grades.id;

/**NON EQUI JOIN**/

select students.id,students.name,students.class,students.marks,student_grades.grade 
from students,student_grades where students.id<student_grades.id;


select students.id,students.name,students.class,students.marks,student_grades.grade 
from students  join student_grades on students.id>=student_grades.id;



//**string functions**//
SELECT ascii ( 'name');
SELECT char (75);
SELECT len ( 'training');
SELECT lower ( 'JOHN' );
SELECT REPLACE ( 'country', 'y', 'ies' );
SELECT reverse ( 'what');
SELECT str (134.56,2,1);
SELECT upper ( 'Praveen');

select str(185.5,4,-2);

//**date functions**//

select getdate();

SELECT dateadd (mm, 2, '2010-02-03');

SELECT datediff ( month, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));
SELECT datediff (day, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));
SELECT datediff ( year, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));

SELECT datepart (mm, '2008-05-01');
SELECT datepart (dd, '2008-05-01');
SELECT datepart (yy, '2008-05-01');

SELECT day ( '2010-03-21');
SELECT month ('2007-04-03');
SELECT year ( '2011-04-17');

//*Mathematical functions**//

select abs(-77); /**retruns absolute value**/
select sin(1.5);
select ceiling(14.6);
select exp(5);
select floor(16.857);
select log(10.5);

//*Rank Functions*//

select id,name, row_number() over (order by name) from students;

select id,name,rank() over (order by marks desc) as rank from students;

select id,name,dense_rank() over (order by marks asc) as rank from students;

select id,name,class,NTILE(3) over(order by marks desc) as rank
from students where marks>=80;
/**system functions**/

select HOST_ID() as 'hostid';
select HOST_NAME();

select SUSER_ID() as sid;

select user_id() as USERID;

select db_name(5) as databasename;

/** use of aggregate functions**/
use Customers;
select 'Average_marks'=avg(marks) from students;
select 'unique mark'=count(distinct marks) from students;

select 'min mark'=min(marks) from students;
select 'max mark'=max(marks) from students;
select 'sum of marks'=sum(marks) from students;

/** group by **/
use joins;
select name,count(marks),marks
from students
where id between '1' and '4'
group by name,marks;

SELECT * FROM students limit 3; //** limit keyword not working**//

