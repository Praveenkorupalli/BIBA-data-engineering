CREATE database  sub_queries;
use sub_queries;

create table Products(PID int,Pname varchar(20),supplierID int,CategoryID int,price int);

insert into  Products values(1,'chais',1,1,10),
(2,'chang',1,1,20),(3,'aniseed syrup',1,2,40),(4,' Antons Cajun',2,2,50),(1,'ChefGumbo Mix',2,2,30);


create table suppliers(supplierID int,name varchar(30),contact_name varchar(30),address varchar(50));

insert into suppliers values(1,'Exotic Liquid','Charlotte Cooper','49 Gilbert St'),
(2,'New Orleans Cajun Delight','Shelley Burke','P.O. Box 78934'),
(3,'Grandma Kellys Homestead','Regina Murphy','707 Oxford Rd'),
(4,'Tokyo Traders','Yoshi Nagase','9-8 Sekimai Musashino-sh');
select * from Products;
select * from suppliers;

/**Exists**/

select name from suppliers
where exists(select Pname from Products where products.supplierID=suppliers.supplierID and price<20);

select name from suppliers 
where exists (select Pname from Products where products.supplierID =suppliers.supplierID and price=40);

select name from suppliers
where exists (select Pname from Products where products.supplierID =suppliers.supplierID and price<40);

select Pname from products
where exists (select name from suppliers where products.supplierID=suppliers.supplierID or price>=30);

select Pname from products
where exists (select name from suppliers where products.supplierID=suppliers.supplierID and price>=30);

/**ANY**/

select * from Products;
select * from suppliers;


select * from products
where supplierID <=any(select supplierID from suppliers 
				        where supplierID>'2' );

select * from products
where supplierID =any(select supplierID from suppliers 
				       where supplierID='1' );

select * from products
where supplierID =any(select supplierID from suppliers 
				       where supplierID!='1' );

/** ALL **/

select * from products
where supplierID =all(select supplierID from suppliers 
				where supplierID='2' );

select * from products
where supplierID < all(select supplierID from suppliers 
				where supplierID='2' );

select * from products
where supplierID >all(select supplierID from suppliers /**it doesnt produce any output**/
				where supplierID='3' );


/** correlated subquery**/

select p.PID,p.Pname,p.supplierID,p.price
from products p
where p.supplierID=(select b.supplierID from suppliers b 
			          where supplierID='2');


select p.PID,p.Pname,p.supplierID,p.price
from products p
where p.supplierID =(select b.supplierID from suppliers b 
			          where name='New Orleans Cajun Delight');


/**  exists **/
select Pname from products
where exists(select supplierID from suppliers  where suppliers.supplierID=Products.CategoryID);

/** not exists **/
select Pname from products
where not exists(select supplierID from suppliers  where suppliers.supplierID=Products.CategoryID);

/**  stored procedure**/

CREATE PROCEDURE usproduct
as
SELECT * from Products WHERE price >'20';

exec us_product;

create procedure inproduct
as
select PID,Pname,price from Products where supplierID='2' and CategoryID='2';

exec inproduct;


