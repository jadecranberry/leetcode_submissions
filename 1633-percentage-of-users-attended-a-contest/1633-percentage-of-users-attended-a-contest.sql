# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(DISTINCT user_id)*100/(SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY 2 DESC, 1 ASC


