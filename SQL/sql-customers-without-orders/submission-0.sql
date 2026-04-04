-- Write your query below
SELECT name
From customers
where id NOT IN (SELECT customer_id From orders)