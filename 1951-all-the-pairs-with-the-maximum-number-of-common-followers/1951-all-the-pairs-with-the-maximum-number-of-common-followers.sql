# Write your MySQL query statement below    
SELECT u1 as user1_id, u2 as user2_id 
FROM (SELECT r1.user_id as u1, r2.user_id as u2, dense_rank() over (order by count(*) DESC) as rnk
     FROM Relations r1 join relations r2
     on r1.user_id < r2.user_id AND r1.follower_id = r2.follower_id
     group by 1,2) as t
WHERE rnk=1     
    
    