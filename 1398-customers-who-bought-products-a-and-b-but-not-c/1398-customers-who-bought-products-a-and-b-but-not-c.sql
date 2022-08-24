# Write your MySQL query statement below
SELECT C.customer_id, C.customer_name
FROM Orders O, Customers C
where C.customer_id = O.customer_id
GROUP BY C.customer_id
Having sum(O.product_name="A")>0 AND SUM(O.product_name="B")>0 AND SUM(O.product_name="C")=0
