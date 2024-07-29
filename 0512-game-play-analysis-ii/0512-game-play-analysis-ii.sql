# Write your MySQL query statement below

select distinct player_id, 
       first_value(device_id) over(partition by player_id order by event_date) as device_id
from Activity
