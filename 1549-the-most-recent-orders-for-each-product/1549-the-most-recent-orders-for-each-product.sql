# Write your MySQL query statement below



SELECT product_name, product_id, order_id, order_date
FROM (
    SELECT p.product_name, p.product_id, O.order_id, o.order_date, RANK() over(partition by product_name Order by Order_date DESC) rnk
     FROM Products p JOIN Orders o
     ON P.product_id=o.product_id
) temp
WHERE rnk = 1
ORDER BY 1, 2, 3
