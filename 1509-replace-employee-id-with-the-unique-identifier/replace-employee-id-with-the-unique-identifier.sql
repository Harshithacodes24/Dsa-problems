select unique_id,name
From Employees as e
left join EmployeeUNI as eu
on e.id=eu.id;

