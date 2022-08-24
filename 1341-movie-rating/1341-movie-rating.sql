# Write your MySQL query statement below

(SELECT u.name as results
FROM MovieRating r LEFT JOIN Users u
ON U.user_id = r.user_id
GROUP BY r.user_id
ORDER BY COUNT(r.movie_id) DESC, u.name
LIMIT 1)
UNION
(SELECT m.title as results
 FROM MovieRating r LEFT JOIN Movies m
 ON r.movie_id = m.movie_id
 WHERE LEFT(CREATED_AT,7)='2020-02'
 GROUP BY r.movie_id
 ORDER BY AVG(rating) DESC,m.title
 LIMIT 1
)
