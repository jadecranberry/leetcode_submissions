# Write your MySQL query statement below
SELECT employee_id, count(*) over(partition by team_id) as team_size
FROM Employee

