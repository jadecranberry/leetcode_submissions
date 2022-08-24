# Write your MySQL query statement below




SELECT order_id
FROM (SELECT order_id, max(avg(quantity)) over() as max_avg_quantity, max(quantity) as max_quantity
FROM OrdersDetails
GROUP BY order_id) AS new
WHERE new.max_quantity>new.max_avg_quantity