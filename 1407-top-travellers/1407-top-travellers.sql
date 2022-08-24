# Write your MySQL query statement below
SELECT Users.name, SUM(IFNULL(DISTANCE, 0)) AS travelled_distance
FROM Users LEFT JOIN Rides
ON Users.id = Rides.user_id
GROUP BY Rides.user_id
ORDER BY 2 DESC, 1 ASC



