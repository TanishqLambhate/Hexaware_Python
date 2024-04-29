-- write a query to find all orders attributed to a salesman in paris
select * from orders;
select * from salesman;

select salesman_id from salesman where city='Paris' ;
select * from orders where salesman_id in (select salesman_id from salesman where city='Paris');

-- Task 7					
-- Write a query to find all orders attributed to a salesman in Paris
-- Clue: In operator
 -- method 1
SELECT a.*  
FROM orders as a INNER JOIN salesman AS b
ON a.salesman_id = b.salesman_id
WHERE b.city = 'Paris'
-- Task 8 

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);

-- Write a query to find the name and id of all salesmen who had more than one customer
select * from customer ;
select salesman_id from customer group by salesman_id having count(salesman_id)>1;
select name,salesman_id from salesman where salesman_id in (select salesman_id from customer group by salesman_id having count(salesman_id)>1);

-- All & Any
-- all=max
-- any=min
-- want all the orders which are greater than the Poojitha's Orders
select * from orders where purch_amt > All(
				select purch_amt
				from orders
				where customer_id=3005);
-- ANOTHER WAY
select * from orders where purch_amt >(select max(purch_amt) from orders 
where customer_id=3005);
-- ANY
select * from orders where purch_amt > Any(
				select purch_amt
				from orders
				where customer_id=3005);



-- Task 9
-- Write a query to display only those customers whose grade are, in fact, higher than every customer in New York.
--- All or Any
select * from customer ;
select grade  from customer where city='New York';
select * from customer where grade> All(select grade  from customer where city='New York');


-- Task 10
-- Write a query to find all orders with an amount smaller than any amount for a customer in London.
select customer_id  from customer where city='London';
select purch_amt from orders where customer_id In (select customer_id  from customer where city='London');
select * from orders where purch_amt< Any(select purch_amt from orders where customer_id In (select customer_id  from customer where city='London'));