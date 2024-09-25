# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus 
FROM Employee
LEFT JOIN Bonus 
USING (empId)
where bonus is null or bonus<1000