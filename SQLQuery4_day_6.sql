Create Database setoperations;
use setoperations
 
 
CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
 
INSERT INTO Employees (EmployeeID, Name, Department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'Engineering'),
(4, 'Dana', 'HR');
 
 
CREATE TABLE Applicants (
    ApplicantID INT,
    Name VARCHAR(50),
    AppliedFor VARCHAR(50)
);
 
INSERT INTO Applicants (ApplicantID, Name, AppliedFor) VALUES
(5, 'George', 'Engineering'),
(6, 'Helen', 'Marketing'),
(7, 'Ian', 'Marketing'),
(3, 'Charlie', 'Sales');
 
Select * from Employees;
Select * from Applicants;

--set theory
-- union
-- intercept - common
-- except -un - common

Select Department from Employees
intersect
Select AppliedFor from Applicants;

Select Department from Employees
union
Select AppliedFor from Applicants;

Select Department from Employees
except
Select AppliedFor from Applicants;
--Result is always unique
--in set all elements are unique
-- order matters for except

CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    InStock CHAR(3)
);
 
INSERT INTO Products (ProductID, ProductName, Category, InStock) VALUES
(1, 'Laptop', 'Electronics', 'Yes'),
(2, 'Smartphone', 'Electronics', 'No'),
(3, 'Coffee Maker', 'Appliances', 'Yes'),
(4, 'Blender', 'Appliances', 'Yes'),
(5, 'T-shirt', 'Apparel', 'No');

CREATE TABLE Orders (
    OrderID INT,
    ProductID INT,
    CustomerName VARCHAR(50),
    Quantity INT
);
 
INSERT INTO Orders (OrderID, ProductID, CustomerName, Quantity) VALUES
(100, 1, 'Alice', 1),
(101, 3, 'Bob', 2),
(102, 2, 'Charlie', 1),
(103, 4, 'Dana', 1),
(104, 3, 'Alice', 1);

select * from Orders
select * from Products

-- List all distinct products thqat are either in stock or have been ordered
select productID from Products where InStock='Yes'
union
select productID from orders ;

select * from products where ProductID in (select productID from Products where InStock='Yes'
union
select productID from orders );

-- Task 2
-- Identify products that are both in stock and have been ordered.
 select * from products where ProductID in (select productID from Products where InStock='Yes'
intersect
select productID from orders );
-- Task 3
-- Find products that are in stock but have never been ordered.
 select * from products where ProductID in (select productID from Products where InStock='Yes'
except
select productID from orders );

CREATE TABLE EmployeeSales (
    EmployeeID INT,
    Region VARCHAR(50),
    Category VARCHAR(50),
    Quarter VARCHAR(10),
    SalesAmount DECIMAL(10,2)
);
 
INSERT INTO EmployeeSales (EmployeeID, Region, Category, Quarter, SalesAmount)
VALUES
    (101, 'North', 'Electronics', 'Q1', 1200.00),
    (101, 'North', 'Electronics', 'Q2', 1500.00),
    (102, 'North', 'Clothing', 'Q1', 800.00),
    (102, 'North', 'Clothing', 'Q2', 950.00),
    (103, 'South', 'Electronics', 'Q1', 1000.00),
    (103, 'South', 'Clothing', 'Q1', 1200.00),
    (104, 'East', 'Electronics', 'Q2', 1150.00),
    (104, 'East', 'Clothing', 'Q2', 500.00),
    (105, 'West', 'Electronics', 'Q1', 1900.00),
    (105, 'West', 'Clothing', 'Q1', 1100.00),
    (105, 'West', 'Electronics', 'Q2', 2100.00),
    (105, 'West', 'Clothing', 'Q2', 1300.00);

-- compound sort
select * from EmployeeSales order by region,salesamount desc

select region,category,sum(SalesAmount)  from EmployeeSales group  by region,category 

-- Grouping Sets -R-C,R-Q,R,Q
SELECT REGION, CATEGORY , [QUARTER] ,SUM(SALESAMOUNT) 
FROM EmployeeSales
GROUP BY GROUPING SETS(
	(REGION , CATEGORY),
	(REGION , [QUARTER]),(Region),([Quarter])
)
ORDER BY GROUPING(Region),GROUPING(Category),GROUPING([Quarter])

CREATE DATABASE projects; -- Creating
 
USE projects; -- Switching
 
 
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);
 
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    employee_id INT,
    start_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
 
 
INSERT INTO employees (employee_id, name, department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Engineering'),
(3, 'Charlie', 'HR'),
(4, 'David', 'Marketing');
 
INSERT INTO projects (project_id, project_name, employee_id, start_date) VALUES
(101, 'Alpha', 1, '2021-01-10'),
(102, 'Beta', 2, '2021-03-15'),
(103, 'Gamma', 1, '2021-02-20');

