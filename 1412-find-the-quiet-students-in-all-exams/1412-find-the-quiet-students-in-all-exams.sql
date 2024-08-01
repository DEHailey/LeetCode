# Write your MySQL query statement below
with qs as(
    select exam_id, s.student_id, s.student_name, score,
           rank() over(partition by exam_id order by score) as rk1,
           rank() over(partition by exam_id order by score desc) as rk2
    from Exam
    left join Student s
    on Exam.student_id = s.student_id
)
select distinct student_id, student_name
from qs
where student_id not in (select student_id from qs where rk1 = 1 or rk2 = 1)
order by student_id

