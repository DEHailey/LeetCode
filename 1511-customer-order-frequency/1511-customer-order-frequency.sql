# Write your MySQL query statement below
select customer_id, name
from Customers
     join Orders using(customer_id)
     join Product using(product_id)
where year(order_date) = 2020
group by customer_id
having sum(if(month(order_date)=6, quantity,0) *price) >= 100 and
       sum(if(month(order_date)=7, quantity,0) *price) >= 100