# Write your MySQL query statement below
SELECT distinct a.seat_id
FROM cinema a join cinema b
ON ABS(a.seat_id-b.seat_id)=1 AND a.free=1 and b.free=1
ORDER BY a.seat_id