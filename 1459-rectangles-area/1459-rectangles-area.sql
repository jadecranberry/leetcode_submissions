# Write your MySQL query statement below


SELECT P1.id as p1, P2.id as p2, ABS(P1.x_value-P2.x_value)*abs(p1.y_value-p2.y_value) as area
FROM Points P1 JOIN Points P2
ON P1.id<p2.id AND P1.x_value!=p2.x_value AND p1.y_value!=p2.y_value
ORDER BY 3 DESC, 1, 2
