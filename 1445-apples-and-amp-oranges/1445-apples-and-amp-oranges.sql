# Write your MySQL query statement below
select sale_date, 
       sum(case when fruit in('apples') then sold_num
                when fruit in('oranges') then sold_num*-1 end) as diff
from Sales
group by sale_date
order by sale_date


