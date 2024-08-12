# Write your MySQL query statement below
select c.name as customer_name, c.customer_id, t.order_id, t.order_date
from Customers c
join (
    select order_id, order_date, customer_id,
           rank() over(partition by customer_id order by order_date desc) as rnk
    from Orders
)t
on c.customer_id = t.customer_id and rnk <= 3
order by customer_name, customer_id, order_date desc