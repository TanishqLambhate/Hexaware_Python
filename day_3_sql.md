### Database
- Special software to store data
- what is cloud = Renting PC
- why cant we put twitter database in our laptop
- Cloud Providers

- Good Server Hard Disk-vibration resistent ,lifespan ,costlier

- Renting PC 
##### What OS in cloud
- Linux
    1. Free
    2. Opensource
    3. Secure
    4. Small footprint
    5. Automation(DX-Developer Experience)
    - Alpine Linux is used mostly in cloud
    - Alpine only takes 256 mb wheras win takes 30 gb

- **Scaling**
    1. Vertical-increasing the same pc storage,ram and more processing power. Upto 256 gb
    2. Horizontal - Adding PCs

- AutoScaling:ON
    - they will intentionally increase traffic
    1. Distributed denial of service(**DDOS**)
        - Attacking bots , Malicious bots
        - captcha will protect

- **Database why?**
    - Database-Frequently asked it will have it in ram
    - Querying becomes easier
    - CRUD easy
    - Backups are inbuilt
    - Undo -easily(time limit)
    - Performance

- Normalization
    - For saftey of data

[SQL](https://sqlbolt.com/)

# EXC 1
## SQL Lesson 1: SELECT queries 101
Find the title of each film
```sql
SELECT title FROM movies;
```
Find the director of each film
```sql
SELECT Director FROM movies;
```
Find the title and director of each film
```sql
SELECT Title,Director FROM movies;
```
Find the title and year of each film 
```sql
SELECT Title,Year FROM movies;
```
Find all the information about each film
```sql
SELECT * FROM movies;
```
## EX2
#### SQL Lesson 2: Queries with constraints (Pt. 1)
Find the movie with a row id of 6
```sql
SELECT * FROM movies where id=6;
```
Find the movies released in the years between 2000 and 2010
```sql
SELECT * FROM movies where year between 2000 and 2010;
```
Find the movies not released in the years between 2000 and 2010
```sql
SELECT * FROM movies where year not between 2000 and 2010;
```
Find the first 5 Pixar movies and their release year
```sql
SELECT * FROM movies where id between 1 and 5;
```
## EX 3
### SQL Lesson 3: Queries with constraints (Pt. 2)
Find all the Toy Story movies 
```sql
SELECT * FROM movies where title like "Toy Story%";
```
Find all the movies (and director) not directed by John Lasseter
```sql
SELECT * FROM movies where not director="John Lasseter";
```
Find all the WALL-* movies 
```SQL
SELECT * FROM movies where title like "WALL-%";
```
### Ex 4
#### SQL Lesson 4: Filtering and sorting Query results
List all directors of Pixar movies (alphabetically), without duplicates 
```sql
SELECT distinct(director) FROM movies order by director ASC;
```
List the last four Pixar movies released (ordered from most recent to least)
```sql
SELECT * FROM movies order by year DESC limit 4;
```
List the first five Pixar movies sorted alphabetically
```sql
SELECT * FROM movies order by title limit 5;
```
List the next five Pixar movies sorted alphabetically
```sql
SELECT * FROM movies order by title limit 5 offset 5;
```
### EX
List all the Canadian cities and their populations ✓
```sql
SELECT * FROM north_american_cities where country="Canada";
```
Order all the cities in the United States by their latitude from north to south 
```sql
    SELECT * FROM north_american_cities where country="United States" order by Latitude desc;
    ```
List the two largest cities in Mexico (by population)
```
```sql
SELECT * FROM north_american_cities  where country ="Mexico" order by population desc limit 2;
```
List the third and fourth largest cities (by population) in the United States and their population ✓
```sql
SELECT * FROM north_american_cities  where country ="United States" order by population desc limit 2 offset 2;
```
## Ex 6
### SQL Lesson 6: Multi-table queries with JOINs

Find the domestic and international sales for each movie 
```sql
SELECT * FROM movies INNER JOIN Boxoffice ON Movies.id=Boxoffice.Movie_id;
```
Show the sales numbers for each movie that did better internationally rather than domestically
```sql
    SELECT * FROM movies INNER JOIN Boxoffice ON Movies.id=Boxoffice.Movie_id
where International_sales>Domestic_sales;
```
List all the movies by their ratings in descending order 
```sql
    SELECT * FROM movies INNER JOIN Boxoffice ON Movies.id=Boxoffice.Movie_id
    order by rating desc;
```
## Ex 7
### SQL Lesson 7: OUTER JOINs
Find the list of all buildings that have employees 
```sql
SELECT distinct building FROM employees ;
```
Find the list of all buildings and their capacity
```sql
SELECT * FROM Buildings ;
```
## Ex 8
Find the name and role of all employees who have not been assigned to a building 
```sql
    SELECT * FROM employees where building is null;
```
Find the names of the buildings that hold no employees
```sql
SELECT * FROM Buildings left join employees on Building_name=building
where building is null;
```

## EX 9
List all movies and their combined sales in millions of dollars 
```sql
SELECT title,(domestic_sales+international_sales)/1000000 as combined_sales FROM movies inner join Boxoffice on id=movie_id;
```
List all movies and their ratings in percent 
```sql
SELECT title,rating*10 FROM movies inner join Boxoffice on id=movie_id;
```
List all movies that were released on even number years
```sql
SELECT * FROM movies where Year%2==0 ;
```
EX 10
Find the longest time that an employee has been at the studio
```sql
    SELECT max(years_employed) FROM employees;
```
For each role, find the average number of years employed by employees in that role
```sql
    SELECT avg(years_employed),role FROM employees group by role;
```
    
EX 11
Find the number of Artists in the studio (without a HAVING clause) 
```sql
SELECT role,count(role) FROM employees where role="Artist";
```
Find the number of Employees of each role in the studio
```sql
SELECT count(role),role FROM employees group by role;
```
Find the total number of years employed by all Engineers 
```sql
SELECT sum(years_employed) FROM employees where role="Engineer";
```
EX 12

Find the number of movies each director has directed
```SQL
SELECT director,count(director) FROM movies group by director;
```
Find the total domestic and international sales that can be attributed to each director 
```sql
SELECT sum(domestic_sales)+sum(international_sales) as total,director 
FROM movies 
left join boxoffice on id=movie_id 
group by director ;
```
EX 13
Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
```SQL
insert into movies values(15,'Toy Story 4','Tanishq',2024,120);
```
Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
```sql
insert into BOXOFFICE values(15,8.7,340000000,270000000);
```