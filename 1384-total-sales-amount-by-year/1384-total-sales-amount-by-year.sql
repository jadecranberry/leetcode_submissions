# Write your MySQL query statement below

#use recursive CTE to find all possible dates
WITH recursive CTE AS(
     SELECT MIN(period_start) as date
     FROM Sales
     UNION ALL
     SELECT DATE_ADD(date, INTERVAL 1 day)
     FROM CTE
     WHERE date<=ALL(SELECT MAX(period_end) FROM Sales)
)

SELECT s.product_id, p.product_name, LEFT(e.date, 4) as report_year, SUM(s.average_daily_sales) as total_amount
FROM Sales s JOIN Product p ON p.product_id = s.product_id JOIN CTE e ON e.date>=s.period_start AND e.date<=s.period_end
GROUP BY 1,2,3
ORDER BY 1,3