# Write your MySQL query statement below
select contest_id, round(count(user_id)*100/(select count(*) from users),
2 ) as percentage from register group by 1 order by percentage DESC, contest_id
