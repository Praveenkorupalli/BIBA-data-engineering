create database datacleaning;
use datacleaning;

create table companies( id int,name varchar(50),industry varchar(30),year_founded int,city varchar(30));

insert into companies values(1,'overhex','software',2006,'Franklin'),
(2,'unimattax','itservices',2009,'newtonsquare'),
(3,'lexila','realestate',2032,'tinleypark'),
(4,'yearflex','null',2013,'madison');
(5,'Toghtam','logistics',2011,'Bimingham'),
insert into companies values(1,'overhex','software',2006,'Franklin');
insert into companies values(1,'overhex',,2006,'Franklin');

select * from companies;
select distinct(industry) from companies;
update companies
set industry='marketing' where id='4';

insert into companies values(6,'Quotelane',null,null,'Greenville');
insert into companies values(6,'Quotelane',null,null,'Greenville');


select id,count(name) as count
from companies
group by id
having(id)>1;


WITH cte AS (SELECT name,ROW_NUMBER() OVER (PARTITION BY name ORDER BY name ASC) AS rn
FROM companies)
DELETE FROM cte
WHERE rn > 1;

select * from companies;
select * from companies
where industry is NULL;

delete from companies
where year_founded is null;

update companies
set industry='other'
where industry is null;

select * from companies;

update companies
set name =upper(name);

select * from companies;

select * from companies
where year_founded > '2023';

update companies
set year_founded=2012
from companies
where id='6';

select * from companies;

/** partition by**/
create table car_prices(company varchar(50),model varchar(50),car_type varchar(50),price int);

insert into car_prices values('ford','mondeo','premium',18200),
('renault','fuego','sport',16500),
('Citroen','Cactus','premium',8990),
('ford','mondeo','standard',12400),
('Renault','Megane','standard',14300);

select * from car_prices;

select company,model,price,
avg(price) over() as 'overall avg price',
avg(price) over(partition by car_type) as 'car type avg price' 
from car_prices;






