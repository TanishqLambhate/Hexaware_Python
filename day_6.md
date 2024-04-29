### Natural Join
- not supported in mysql
1. No condition
2. same column name for pk and fk
```sql
    select * from employee natural join department
```
- result will be same as inner join

### Equi Join
- special type of inner join
1. Mention the condition
2. condition should always about equal to "="
3. Trying to find equal values on pk to fk
``` sql
    select * from emp inner join dep on emp.dep_id=dep.dep_id
```
- inner join with equal to becomes equi join
- inner join with different symbol such as <,> to becomes inner join
```sql
CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Salary DECIMAL(10,2),
    DepartmentID INT
);
 
CREATE TABLE Departments (
    DepartmentID INT,
    DepartmentName VARCHAR(50),
    MinSalary DECIMAL(10,2)
);
 
INSERT INTO Employees VALUES (1, 'John Doe', 50000, 101), (2, 'Jane Smith', 40000, 102);
INSERT INTO Departments VALUES (101, 'HR', 45000), (102, 'Marketing', 35000);
 
Select * from Employees
 
Select * from Departments
 
 
Select Name, Salary, DepartmentName,  MinSalary
From Employees
Inner Join Departments 
on Salary > MinSalary
```

Database
```sql
    create database fun; --creating
```
```sql
use fun;--switching
```
```sql
Exec sp_renamedb 'fun' , 'cool';
```
```sql
drop database cool;
```
#### declaration
```sql
-- Declare @variableName <>
-- Declare @variableName <Date Type> =<Value>
declare @d Date =GETDATE();
SELECT FORMAT(@d,'dd/mm/yyyy','en-us') from orders
```