select r.contest_id , 
       ROUND(COUNT(r.user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
from Register r 
group by r.contest_id
Order by percentage  DESC , r.contest_id  ASC;

