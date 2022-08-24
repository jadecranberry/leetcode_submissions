# Write your MySQL query statement below
   
WITH recursive cte as(
     SELECT num, 1 as occurance, frequency FROM numbers
     UNION ALL
     SELECT num, occurance+1, frequency FROM cte 
     WHERE occurance<frequency
),
t2 as (
   SELECT num, row_number() over(order by num) as num_index
   FROM cte
)

SELECT avg(num) as median
FROM t2
WHERE num_index BETWEEN (SELECT max(num_index)/2 from t2) AND (SELECT (max(num_index)/2)+1 from t2)







