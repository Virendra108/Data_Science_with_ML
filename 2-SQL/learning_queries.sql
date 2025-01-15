--10-07-2024
select * from job;
insert into job(job_name) values ('cowboy');
delete from job where job_name='cowboy' returning job_id,job_name;

--ALTER
create table information(
	info_id serial primary key,
	title varchar(500) not null,
	person varchar(50) not null unique
);
select * from information;
alter table information rename to new_info; 

select * from new_info;
alter table new_info rename column person to people;
insert into new_info(title) values ('some new title'); --ERROR not null constraint
alter table new_info alter column people drop not null; 
insert into new_info(title) values ('some new title');
select * from IF EXISTS new_info;

--DROP
alter table new_info drop column people;
alter table new_info drop column if exists people;

--CHECK CONSTRAINTS
create table employees(
	emp_id serial primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	birthdate date check(birthdate> '1900-01-01'),
	hire_date date check(hire_date>birthdate),
	salary integer check (salary>0)
);
insert into employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)values(
	'Jose',
	'Portilla',
	'1899-11-03', --violates condition
	'2010-01-01',
	'100'
);

insert into employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)values(
	'Jose',
	'Portilla',
	'1990-11-03',
	'2010-01-01',
	'100'
);

insert into employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)values(
	'Samay',
	'Portilla',
	'1990-11-03',
	'2010-01-01',
	'-100'          --violates condition >0
);
insert into employees(
	first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)values(
	'Samay',
	'Portilla',
	'1990-11-03',
	'2010-01-01',
	'101'
);
select * from employees;


--11/07/2024
/*
https://www.postgresql.org/docs/12/sql-copy.html
*/

