# Write your MySQL query statement below

WITH CTE as(
    SELECT id,login_date, datediff(lead(login_date, 4) over (partition by id order by login_date asc ) , login_date) date_diff
    FROM logins
    GROUP BY 1,2
    )

SELECT distinct cte.id, name
FROM CTE join accounts a
on cte.id = a.id
where date_diff=4
order by 1