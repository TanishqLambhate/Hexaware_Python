- Dorid Cam
- ctrl+~  =>terminal
- update
    - before update select the condition then apply update.
## EX 14
The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
```sql
update movies
set director="John Lasseter"
where id=2;
```
The year that Toy Story 2 was released is incorrect, it was actually released in 1999
```sql
update movies
set year="1999"

where title="Toy Story 2";
```
Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
```sql
    update movies
    set title="Toy Story 3",    director="Lee Unkrich"
    where id="11";

```
## EX 
This database is getting too big, lets remove all movies that were released before 2005
```SQL
Delete FROM movies
where year<2005;
```
Andrew Stanton has also left the studio, so please remove all movies directed by him
```sql
Delete FROM movies
where DIRECTOR="Andrew Stanton";
```

### AWS 
- s3 bucket is used to store images in database

### Decimal / float /
### EX (SQL Lesson 16: Creating tables)
Create a new table named Database with the following columns:
– Name A string (text) describing the name of the database
– Version A number (floating point) of the latest version of this database
– Download_count An integer count of the number of times this database was downloaded
```sql
create table if not exists Database(
Name text ,
Version float ,
Download_count int 
);
```
### EX
Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
```sql
ALTER TABLE Movies
ADD Language   TEXT 
default english
```
And drop the BoxOffice table as well 
```sql
drop table boxoffice
```
