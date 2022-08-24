# Write your MySQL query statement below
SELECT
(Select DISTINCT salary
FROM Employee
ORDER BY 1 DESC
LIMIT 1 OFFSET 1)
AS SecondHighestSalary