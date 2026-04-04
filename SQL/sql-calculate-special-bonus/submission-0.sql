-- Write your query below
SELECT employee_id,
CASE WHEN employee_id % 2 = 1 AND name Not Like 'M%' 
THEN salary ELSE 0
END AS bonus
From employees
ORDER BY employee_id;