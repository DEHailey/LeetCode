# Write your MySQL query statement below
select transaction_id
from (
    select *, dense_rank() over(partition by date(day) order by amount desc) as d
    from Transactions
    order by day 
) temp
where d = 1
order by transaction_id asc
