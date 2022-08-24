# Write your MySQL query statement below
SELECT S1.student_id, S1.student_name, S2.subject_name, count(E.subject_name) as attended_exams
FROM Students S1 join Subjects S2 LEFT join Examinations E
ON S1.student_id = E.student_id AND S2.subject_name = E.subject_name
GROUP BY S1.student_id, S2.subject_name
ORDER BY 1, 3

