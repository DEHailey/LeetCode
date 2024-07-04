# Write your MySQL query statement below
select transaction_id
from 
(
    select * , dense_rank() over(partition by date(day) order by amount desc) as dt
    from Transactions
    order by day asc
) temp
where dt = 1
order by transaction_id asc

