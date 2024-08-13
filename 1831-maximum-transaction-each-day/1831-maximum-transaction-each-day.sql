# Write your MySQL query statement below
select transaction_id
from (
    select transaction_id, day, amount,
           rank() over(partition by day order by amount desc) as rnk
    from Transactions
)t
where rnk = 1
order by transaction_id
