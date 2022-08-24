# Write your MySQL query statement below

SELECT e1.reports_to as employee_id, e2.name, count(distinct e1.employee_id) as reports_count, round(avg(e1.age), 0) as average_age
FROM Employees e1 LEFT JOIN Employees e2
ON e1.reports_to = e2.employee_id
where e1.reports_to is not null
GROUP BY e1.reports_to, e2.name
order by 1
