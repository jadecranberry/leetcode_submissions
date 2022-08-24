# Write your MySQL query statement below
SELECT a.name as warehouse_name, SUM(a.units*b.Width*b.Length*b.Height) AS volume
FROM Warehouse as a JOIN Products as b
ON a.product_id = b.product_id
GROUP BY a.name