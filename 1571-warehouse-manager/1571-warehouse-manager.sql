# Write your MySQL query statement below
select w.name as warehouse_name, 
       sum(w.units * sub.cubic_ft) as volume
from Warehouse w
left join (
    select
        p.product_id, 
        p.width * p.length * p.height as cubic_ft
    from Products p
) as sub
on w.product_id = sub.product_id
group by warehouse_name
order by warehouse_name asc

