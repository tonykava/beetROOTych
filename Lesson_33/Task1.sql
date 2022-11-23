SELECT employees.first_name,
employees.last_name,
employees.department_id,
departments.depart_name
FROM employees
JOIN departments ON departments.department_id = employees.department_id;



SELECT employees.first_name,
employees.last_name,
departments.depart_name,
locations.city,
locations.state_province
FROM employees
INNER JOIN departments ON departments.department_id = employees.department_id
INNER JOIN locations ON locations.location_id = departments.location_id;



SELECT employees.first_name,
employees.last_name,
departments.department_id,
departments.depart_name
FROM employees
INNER JOIN departments ON departments.department_id = employees.department_id
WHERE employees.department_id = 80;



SELECT departments.depart_name
FROM departments



SELECT e.first_name || ' ' || e.last_name AS 'Employee',
       m.first_name || ' ' || m.last_name AS 'Manager'
FROM employees e
INNER JOIN employees m ON e.manager_id = m.employee_id
ORDER BY Manager;



SELECT employees.first_name || ' ' || employees.last_name as 'Full Name',
jobs.job_title,
jobs.max_salary - employees.salary as 'Difference between max salary and real salary'
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id;



SELECT
jobs.job_title,
round(avg(employees.salary), 2) as 'Average job salary'
FROM
jobs
INNER JOIN employees ON employees.job_id = jobs.job_id
GROUP BY
jobs.job_title;



SELECT
employees.first_name || ' ' || employees.last_name as 'Full Name',
employees.salary
FROM
employees
JOIN departments
JOIN locations
WHERE
employees.department_id = departments.department_id and departments.location_id = locations.location_id and locations.city = 'London';



SELECT
departments.depart_name,
COUNT(*) as 'Number of employees in department'
FROM
employees
INNER JOIN
departments ON departments.department_id = employees.department_id
GROUP BY
departments.depart_name;
