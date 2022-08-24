# Write your MySQL query statement below
#LEAD ( expression [, offset [, default] ] )

#expression
#An expression that can contain other built-in functions, but can not contain any analytic functions.

#offset
#Optional. It is the physical offset from the current row in the table. If this parameter is omitted, the default is 1.

#default
#Optional. It is the value that is returned if the offset goes out of the bounds of the table. If this parameter is omitted, the default is null.

SELECT user_id, max(diff) as biggest_window
FROM (SELECT user_id, DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (partition by user_id ORDER BY visit_date), visit_date) as diff
     FROM UserVisits) as t
GROUP BY user_id
ORDER BY user_id

