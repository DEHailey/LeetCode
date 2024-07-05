# Write your MySQL query statement below
select distinct p.product_name, p.product_id, o.order_id, o.order_date
from Products p
join (
    select
        order_id,
        order_date,
        product_id,
        rank() over(partition by product_id order by order_date desc) as rnk
    from Orders
) o
on p.product_id = o.product_id
and rnk = 1
order by p.product_name, p.product_id, o.order_id