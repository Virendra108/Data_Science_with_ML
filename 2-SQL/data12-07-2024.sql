--12/07/2024
show timezone;
create table timezones(
	ts timestamp without time zone,
	tz timestamp with time zone
)

insert into timezones values(
	timestamp without time zone '2023-03-07 10:50',
	timestamp with time zone '2023-03-07 10:50'
);

select * from timezones;

select now()::date;
select current_date;

select to_char(current_date,'dd/mm/yy');
select to_char(current_date,'ddd');
select to_char(current_date,'ww');
select age(date'1800-01-01');
select age(date '1992/11/13',date '1800/01/01');
select extract(day from date'1992/11/13')as day;
select extract(month from date'1992/11/13')as month;
select extract(year from date'1992/11/13')as year;
select date_trunc('year',date '1992/11/13');

--Q select employees above 60 age
select age(birth_date), *from employees
where(
	extract(year from age(birth_date))
)>60;

--Q how many employees were hired in february
select count(emp_no) from employees where extract(month from hire_date)=3;

--Q how many emoplloyees were born in noovember
select count(emp_no) from employees where extract(month from birth_date)=11;

--Q who is the oldest employee
select max(age(birth_date))from employees;

-------------------------------------------------------------------------------------------------------

select max(salary) from salaries;
select *,
	max(salary)
	from salaries;

select *,
	max(salary) over()
	from salaries;

select *,
	max(salary) over()
	from salaries
limit 100;

select *,
	max(salary) over()
	from salaries
	where salary<70000;

select *,
	avg(salary) over()
from salaries;

select *,
d.dept_name,
avg(salary) over()
from salaries
join dept_emp as de using (emp_no)
join departments as d using (dept_no);

select *,
d.dept_name,
avg(salary) over(partition by d.dept_name)
from salaries
join dept_emp as de using (emp_no)
join departments as d using (dept_no);