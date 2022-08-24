# Write your MySQL query statement below


WITH t as(
    SELECT *, ROW_NUMBER() over(partition by continent order by name) as row_id
    FROM Student
)

SELECT 
      MAX(CASE WHEN continent='America' THEN name END)AS America,
      MAX(CASE WHEN continent='Asia' THEN name END)AS Asia,
      MAX(CASE WHEN continent='Europe' THEN name END)AS Europe 
FROM t
GROUP BY row_id