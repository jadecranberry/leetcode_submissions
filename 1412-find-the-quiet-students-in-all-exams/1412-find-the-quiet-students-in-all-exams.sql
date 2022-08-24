# Write your MySQL query statement below
with cte as(
SELECT S.student_id, S.student_name, e.exam_id, e.score, max(e.score) over (partition by exam_id ORDER BY score desc) as max_score, min(e.score) over (partition by exam_id ORDER BY score asc) as min_score
      FROM student s inner join exam e
      on s.student_id=e.student_id
)

SELECT DISTINCT student_id, student_name
FROM cte
WHERE student_id not in (SELECT student_id FROM cte where cte.score=max_score or cte.score=min_score) 
ORDER BY student_id
