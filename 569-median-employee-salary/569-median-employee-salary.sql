# Write your MySQL query statement below
WITH CTE as(
     SELECT *, row_number() over(partition by company order by salary) as roww, count(id) over(partition by company) as cnt
     FROM Employee
)


SELECT id, company, salary
FROM CTE
WHERE roww between cnt/2.0 and cnt/2.0+1

