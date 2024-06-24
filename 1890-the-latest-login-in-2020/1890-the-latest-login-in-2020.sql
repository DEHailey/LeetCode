# Write your MySQL query statement below
select distinct user_id, 
       first_value(time_stamp)over(partition by user_id order by time_stamp desc)as last_stamp
from Logins
where extract(year from time_stamp) = 2020

