# Write your MySQL query statement below
select *
from Users
where mail regexp'^[a-z][a-z0-9_.-]*@leetcode[.]com$'