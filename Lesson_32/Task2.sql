SELECT
first_name as "First Name",
last_name as "Last Name"
FROM
employees;

SELECT DISTINCT department_id
FROM employees;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT
first_name as "First Name",
last_name as "Last Name",
salary,
salary * 0.12 as "PF"
FROM
employees;

SELECT MAX(salary), MIN(salary) FROM employees;

SELECT
first_name as 'First Name',
last_name as 'Last Name',
ROUND(salary / 12, 2) as 'Monthly salary' FROM employees;