# Write your MySQL query statement below
 

SELECT a.seller_name 
FROM Seller a LEFT JOIN Orders b
ON a.seller_id = b.seller_id and LEFT(b.sale_date, 4)='2020' 
WHERE b.order_cost IS NULL
ORDER BY seller_name

