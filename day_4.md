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