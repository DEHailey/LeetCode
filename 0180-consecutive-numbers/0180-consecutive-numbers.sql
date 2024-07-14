# Write your MySQL query statement below

with cte as (
    select 
        id,
        num,
        lead(id, 1) over(order by id) as next_id1,
        lead(id, 2) over(order by id) as next_id2,
        lead(num, 1) over(order by id) as num1,
        lead(num, 2) over(order by id) as num2
    from Logs
)
select distinct num as ConsecutiveNums
from cte
where 
    num = num1 and 
    num = num2 and
    next_id1 = id + 1 and
    next_id2 = id + 2
