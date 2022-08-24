# Write your MySQL query statement below


SELECT DISTINCT a.account_id
FROM LogInfo a JOIN LogInfo b
WHERE a.login between (b.login) and (b.logout)
and a.account_id = b.account_id
and a.ip_address != b.ip_address