# Write your MySQL query statement below


SELECT username, activity, startDate, endDate
FROM (SELECT *,  count(activity) over(partition by username) as cnt, RANK() OVER(PARTITION BY username ORDER BY endDate DESC) AS rnk
      FROM UserActivity) t
WHERE rnk=2 or cnt<2 