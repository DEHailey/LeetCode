# Write your MySQL query statement below
select seller_name
from Seller s
left join Orders o
on s.seller_id = o.seller_id
group by s.seller_id 
having sum(ifnull(year(sale_date)=2020,0))=0
order by 1 asc