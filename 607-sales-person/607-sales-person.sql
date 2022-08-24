# Write your MySQL query statement below
SELECT name 
FROM SalesPerson
WHERE sales_id NOT in (SELECT sales_id FROM Orders WHERE com_id = (select com_id from Company WHERE NAME = 'RED'))
