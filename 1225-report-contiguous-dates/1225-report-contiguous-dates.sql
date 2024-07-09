# Write your MySQL query statement below
select stats as period_state, min(day) as start_date, max(day) as end_date
from (
    select
        day,
        rank() over (order by day) as overall_ranking,
        stats,
        rk,
        (rank() over(order by day) - rk) as inv
    from (
        select fail_date as day, 'failed' as stats, rank() over(order by fail_date) as rk
        from Failed
        where fail_date between '2019-01-01' and '2019-12-31'
        union
        select success_date as day, 'succeeded' as stats, rank() over(order by success_date) as rk
        from Succeeded
        where success_date between '2019-01-01' and '2019-12-31'
    )t
)c
group by inv, stats
order by start_date
