# Write your MySQL query statement below
select 
    a.visited_on as visited_on, sum(b.day_sum) as amount, round(avg(b.day_sum), 2) as average_amount
from 
    (select visited_on, sum(amount) as day_sum from Customer group by visited_on) a, 
    (select visited_on, sum(amount) as day_sum from Customer group by visited_on) b
where 
    DATEDIFF(a.visited_on, b.visited_on) between 0 and 6
group by 
    a.visited_on
having 
    count(b.visited_on) = 7



