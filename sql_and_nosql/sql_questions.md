Here are a list of SQL question answers

# Window Function:
1.  What are window functions in SQL, and how do they differ from aggregate functions?
- Scope:
Aggregate Functions: Collapse multiple rows into a single summary row (e.g., SUM(), AVG(), COUNT()).
Window Functions: Perform calculations across a "window" of rows without collapsing the result set (e.g., ROW_NUMBER(), RANK(), LEAD(), LAG()).

- Usage:
Aggregate Functions: Often used with GROUP BY to summarize data.
Window Functions: Used with the OVER() clause to define the window.


2. Write a query to calculate the running (rolling) total of rental amounts for each customer.
~~~sql
select customer_id, amount, 
    sum(amount) over (partition by customer_id order by payment_date) as runnint_total
from payment;
~~~

# Having:

3. What are differences between Where and Having 
- WHERE Clause:
Purpose: Filters rows before any grouping or aggregation takes place.
Usage: Used with SELECT, UPDATE, DELETE statements
Conditions: Can include conditions on individual columns or expressions.
~~~sql
SELECT customer_id, amount
FROM payment
WHERE amount > 50
~~~
- HAVING Clause:
Purpose: Filters groups of rows after grouping and aggregation.
Usage: Used with GROUP BY to filter groups based on aggregate functions.
Conditions: Can include conditions on aggregate expressions like SUM(), COUNT(), AVG(), etc.
~~~sql
SELECT customer_id, SUM(amount) AS total_amount
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 500;
~~~


# CTE :

4. Explain the difference between a CTE and a subquery.
- Scope and Readability:CTEs are defined at the beginning of the query, making the query easier to read and understand.
- Reusability:CTEs can be referenced multiple times in the same query, whereas subqueries cannot.
- Recursion: CTEs can be recursive, allowing for more complex operations like hierarchical queries. Subqueries do not support recursion.
Write a recursive CTE to find all the films rented by a specific customer, including the rental dates.



# Joins:

5. What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN?
![joins](..\media\inner-joins-and-outer-joins-in-sql-1.jpg)

6. Given the following tables

- Table 1: Signups (user_id: int, time_stamp: datetime)
- Table 2: Confirmations (user_id: int, time_stamp: datetime, action: enum [confirmed, timeout] )

Write a solution to find the confirmation rate of each user.

~~~sql
select s.user_id, coalesce (round(d.confirmation_rate,2), 0.0) as confirmation_rate 
from Signups s
left join(
        select user_id, avg(case when action='confirmed' then 1 else 0 end) as confirmation_rate
        from Confirmations
        group by(user_id)) d 
    on d.user_id = s.user_id
~~~

7. Write a query to find customers who have rented films from both the "Action" and "Comedy" categories.

Subqueries:

What is a correlated subquery, and how does it differ from a regular subquery?

Write a query to find the top 5 customers with the highest total rental amounts using a subquery.

Indexes:

What are the different types of indexes in SQL, and when should you use them?

How would you optimize a query that retrieves the most frequently rented films?

Performance Tuning:

What are some common techniques for optimizing SQL queries?

Write a query to identify and remove duplicate rows from the rental table.

Advanced Aggregations:

Explain the GROUP BY clause and the HAVING clause. How do they differ?

Write a query to calculate the average rental duration for each film category.

Data Manipulation:

How do you handle NULL values in SQL? Provide examples.

Write a query to update the rental rate of all films in the "Drama" category by increasing it by 10%.

Transactions and Concurrency:

What are transactions in SQL, and why are they important?

Explain the different isolation levels in SQL and their impact on data consistency.

Advanced Query Techniques:

Write a query to find the second highest rental amount for each customer.

How would you implement pagination in SQL to retrieve a specific range of rows?