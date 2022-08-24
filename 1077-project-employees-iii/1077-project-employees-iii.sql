# Write your MySQL query statement below
SELECT t.project_id, t.employee_id
FROM (SELECT P.project_id, p.employee_id, rank() over(partition by p.project_id order by e.experience_years desc) as exp_rank
FROM employee as e inner join project as p
ON e.employee_id = p.employee_id) AS t
where t.exp_rank = 1