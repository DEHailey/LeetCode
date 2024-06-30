# Write your MySQL query statement below
select min(abs(a.x - b.x)) as shortest
from Point a
join Point b
on a.x != b.x