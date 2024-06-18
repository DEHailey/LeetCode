# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP '^[a-z][a-z0-9_.-]*@leetcode[.]com$'
