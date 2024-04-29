CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4, 2)
);

INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);

select * from salesman


-- Task 1

-- Find the average commision of a saleman from Paris

select avg(commission) from salesman where city='Paris' ;
-- Task 2
-- Find out if there are cities with only one salesman and list them | No nulls

select count("city") as counts from salesman group by city having count(city) <2 and count(city) >0;
select city,count("city") as counts from salesman where city is not null group by city having count(city)=1;

-- Task 3
-- Determine the maximum commission in each city, and list the salesmen who earn this commission
-- Clue: Join
select max(commission),city,salesman_id from salesman where city is not null group by city,salesman_id;

--list the salesmen who earn this commission
--use  hexaware

select * from salesman where salesman_id in()
select max(commission),city,salesman_id from salesman  join salesman on salesman.salesman_id=salesman.salesman_id where city is not null group by city,salesman_id;

select name,city,commission from salesman o
where commission=(
		select max(commission)
		from salesman i
		where o.city=i.city
);

select name ,city , comission
from salesman o
inner join(
	select max(commission),i.city from salesman where i.city is not null group by i.city;
)i
on o.commission


SELECT a.name, a.commission

FROM salesman AS a INNER JOIN (

	SELECT city, MAX(commission) AS maxCom

	FROM salesman

	WHERE city IS NOT NULL

	GROUP BY city

) AS b

ON a.commission = b.maxCom AND a.city =  b.city

CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
 
 
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5003),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5001),
(70008, 5760, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.4, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.6, '2012-04-25', 3002, 5001);

-- Task 4 - Sub-Query
-- Write a query to display all the orders from the orders table issued by the salesman 'Paul Adam'.
select * from orders inner join salesman on orders.salesman_id=salesman.salesman_id where name='Paul Adam';

select * from orders  where salesman_id=(select salesman_id from salesman where name='Paul Adam');

-- Task 5 
-- Write a query to display all the orders which values are greater than the average order value for 10th October 2012
select AVG(purch_amt),ord_date from orders where ord_date='2012-10-10' group by ord_date;

select AVG(purch_amt) from orders where ord_date='2012-10-10' ;

select * from orders where purch_amt>(select AVG(purch_amt) from orders where ord_date='2012-10-10' );

-- Task 6
-- Write a query to find all orders with order amounts which are above-average amounts for their customers.
select * from orders;
select AVG(purch_amt),salesman_id from orders group by salesman_id ;

select * from orders where purch_amt In (select AVG(purch_amt) from orders group by salesman_id);

Select * 
from orders o
where purch_amt > (Select  AVG(purch_amt) 
					from orders i
					where o.customer_id = i.customer_id
					)
-- top 3 purch amount
select * from orders order by purch_amt desc
offset 0 rows fetch next 3 rows only;
 
-- format date - 25 apr 2012

select format(ord_date,'D','en-gb') from orders

-- Settings Page
declare @d int=3
select * from orders order by purch_amt desc
offset 0 rows fetch next @d rows only;

--set theory
-- union
-- intercept - common
-- except -un - common

create Database setoperations;
use setoperations