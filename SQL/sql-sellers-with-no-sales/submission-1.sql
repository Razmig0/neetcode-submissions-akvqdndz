-- Write your query below
SELECT s.seller_name
From seller s
WHERE seller_id NOT IN(SELECT o.seller_id FROM orders o WHERE sale_date >= '2020-01-01' AND sale_date <= '2020-12-31')
ORDER BY s.seller_name