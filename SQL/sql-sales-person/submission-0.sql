-- Write your query below
SELECT sp.name
FROM sales_person AS sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders AS o
    WHERE com_id = 1
)