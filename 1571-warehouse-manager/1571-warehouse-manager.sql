# Write your MySQL query statement below
select w.name as warehouse_name, sum(sub.cubic_ft * w.units) as volume
from Warehouse w
left join (
    select p.product_id,
           p.Width * p.Length * p.Height as cubic_ft
    from Products p
) as sub
on w.product_id = sub.product_id
group by warehouse_name
