# Write your MySQL query statement below


SELECT D.name AS Department, E.name as Employee, E.salary
FROM Employee E JOIN Department D
WHERE E.departmentId = D.id AND E.Salary = (SELECT MAX(Salary) from Employee e2 where e2.DepartmentId=D.Id)