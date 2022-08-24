# Write your MySQL query statement below

SELECT MIN(log_id) as start_id, MAX(log_id) as end_id
FROM (SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) as NUM FROM Logs) as a
GROUP BY log_id-NUM
