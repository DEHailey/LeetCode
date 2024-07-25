# Write your MySQL query statement below
select w.name as warehouse_name, 
       sum((p.Width * p.Length * p.Height) * w.units) as volume
from Warehouse w
left join Products p
on p.product_id = w.product_id
group by warehouse_name