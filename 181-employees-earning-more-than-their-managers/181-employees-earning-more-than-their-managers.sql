# Write your MySQL query statement below
SELECT a.name as Employee
FROM Employee a, Employee b
WHERE a.salary > b.salary and a.managerId = b.id