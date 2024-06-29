# Write your MySQL query statement below
select c1.name as country
from Person p
join Country c1
on substring(phone_number,1,3) = country_code
join Calls c2
on p.id in (c2.caller_id, callee_id)
group by c1.name
having avg(duration) > (select avg(duration) from calls)
