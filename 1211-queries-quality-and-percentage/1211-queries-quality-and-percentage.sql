# Write your MySQL query statement below
select query_name, 
round(sum(rating / position) / count(*),2) as quality, 
round(100 * sum(CASE WHEN rating < 3 then 1 else 0 end) / count(*),2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name 
order by quality desc