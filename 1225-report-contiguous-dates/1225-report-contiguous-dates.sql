# Write your MySQL query statement below
select 'failed' as period_state, min(fail_date) as start_date, max(fail_date) as end_date
from (
    select fail_date, row_number() over() as rnk
    from Failed
    where year(fail_date) = 2019
)t
group by date_sub(fail_date, interval rnk day)

union all

select 'succeeded' as period_state, min(success_date) as start_date, max(success_date) as end_date
from (
    select success_date, row_number() over() as rnk
    from Succeeded
    where year(success_date) = 2019
)t
group by date_sub(success_date, interval rnk day)
order by start_date