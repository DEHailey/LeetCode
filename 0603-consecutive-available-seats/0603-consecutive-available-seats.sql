# Write your MySQL query statement below
select distinct a.seat_id 
from Cinema a
join Cinema b
on abs(a.seat_id - b.seat_id) = 1
and a.free = 1
and b.free = 1
order by seat_id