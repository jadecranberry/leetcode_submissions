# Write your MySQL query statement below
SELECT department, employee, salary
FROM (SELECT d.name as department, e.name as employee, e.salary, dense_rank() over(partition by e.departmentid order by salary desc) as rnk
     FROM employee e join department d
     on e.departmentId = d.id) as t
where t.rnk<4     