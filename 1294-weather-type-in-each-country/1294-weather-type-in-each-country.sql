# Write your MySQL query statement below


SELECT c.country_name, CASE when AVG(weather_state*1.0)<=15.0 then 'Cold'
                                           when AVG(weather_state*1.0)>=25.0 then 'Hot'
                                           ELSE 'Warm'
                                      END AS weather_type  
FROM Countries c join Weather w
ON c.country_id = w.country_id
WHERE LEFT(W.day, 7)='2019-11'
GROUP BY country_name
