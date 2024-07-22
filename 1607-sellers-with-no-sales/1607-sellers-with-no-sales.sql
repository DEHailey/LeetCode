# Write your MySQL query statement below
select seller_name
from Seller s
left join Orders o
on o.seller_id = s.seller_id
group by s.seller_id 
having sum(ifnull(year(sale_date)=2020,0))=0
order by 1 asc