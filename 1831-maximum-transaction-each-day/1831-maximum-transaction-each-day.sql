# Write your MySQL query statement below

SELECT transaction_id 
FROM (SELECT *, dense_rank() over(partition by DATE(day) order by amount desc) as rnk
     FROM Transactions) as t
WHERE rnk=1
order by transaction_id