create database sub_totals;
use sub_totals;

CREATE TABLE
SalesList
(SalesMonth NVARCHAR(20), SalesQuartes  VARCHAR(5), SalesYear  SMALLINT, SalesTotal int);

INSERT INTO  SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2019,60);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,50);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'May','Q2',2019,30);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2020,10);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'October','Q4',2019,150);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,180);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2020,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2019,160);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,170);

select * from SalesList;

create Procedure q1_sales
as 
select SalesMonth,SalesTotal from SalesList
where SalesQuartes ='Q1';

exec q1_sales;

create Procedure q2_sales
as 
select SalesMonth,SalesTotal from SalesList
where SalesQuartes ='Q1' and SalesYear='2020';

exec q2_sales;

/**subtotal**/

SELECT  SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
    GROUP BY ROLLUP(SalesYear);

/** passing 2 different columns to the rollup so it adds extra 'subtotals' and a 'grand total' row **/

SELECT  SalesYear,SalesQuartes, SUM(SalesTotal) AS SalesTotal
FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes);

/** pass 3 different columns to the roolup so it generates subtotal rows for all heirachies**/

select SalesYear,SalesQuartes,SalesMonth ,SUM(SalesTotal) AS SalesTotal
FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes, SalesMonth);


/** grouping function**/

SELECT SalesYear,SalesQuartes,SUM(SalesTotal) AS SalesTotal,
GROUPING(SalesQuartes) AS SalesQuarterGrp,
GROUPING(SalesYear) AS SYearGrp
FROM SalesList
GROUP BY ROLLUP(SalesYear, SalesQuartes);

SELECT CASE 
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0 THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1 THEN 'Grand Total'
ELSE
CAST(SalesYear AS varchar(10))
END 
AS SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal 
FROM SalesList
GROUP BY ROLLUP(SalesYear,SalesQuartes);

