# Write your MySQL query statement below
select
    p.product_name,
    sum(o.unit) as unit
from Orders o
join Products p
on o.product_id = p.product_id
where year(o.order_date) = 2020 and month(o.order_date) = 2
group by product_name
having unit >= 100

    
