# Write your MySQL query statement below
SELECT E1.name
FROM Employee e1 join Employee e2
ON E1.ID = E2.managerId
GROUP BY E2.managerId
HAVING count(*)>=5
