# Write your MySQL query statement below
SELECT t.customer_id, t.product_id, t.product_name
FROM (SELECT o.customer_id, o.product_id, p.product_name, RANK() OVER (partition by o.customer_id ORDER BY count(o.product_id) DESC) as rnk
     FROM Orders o JOIN products p
     ON o.product_id = p.product_id
     GROUP BY 1, 2) as t
WHERE rnk =1     