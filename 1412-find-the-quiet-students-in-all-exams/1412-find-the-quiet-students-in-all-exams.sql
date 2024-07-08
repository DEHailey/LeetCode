# Write your MySQL query statement below

with cte as(
    select exam_id, Student.student_id, Student.student_name, score, rank() over(partition by exam_id order by score) rk1, rank() over(partition by exam_id order by score desc) rk2
    from Exam
    left join Student
    on Exam.student_id = Student.student_id
)
select distinct student_id, student_name
from cte
where student_id not in (select student_id from cte where rk1 = 1 or rk2 = 1)
order by student_id

