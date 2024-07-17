# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016
from (
    select 
        *, 
        count(*) over(partition by tiv_2015) as t2015_c,
        count(*) over(partition by lat, lon) as latlon_c
    from
        Insurance
) temp
where t2015_c > 1 and latlon_c = 1