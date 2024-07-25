# Write your MySQL query statement below
select sale_date, 
       sum(case when fruit = 'oranges' then sold_num * -1 else sold_num * 1 end) as diff
from Sales
group by sale_date
order by sale_date