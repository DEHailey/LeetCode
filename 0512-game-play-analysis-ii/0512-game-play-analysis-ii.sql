# Write your MySQL query statement below

select distinct a.player_id, first_value(a.device_id) over(partition by a.player_id order by a.event_date) as device_id
from Activity a
