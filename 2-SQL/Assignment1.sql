/* ASSIGNMENT 1
*/

create table machine_log(
	log_id serial primary key,
	machine_id varchar(100) not null,
	production_date date not null,
	production_shift varchar(50)not null,
	products_produced integer not null,
	defects integer not null check (defects<=products_produced),
	runtime float not null
);
INSERT INTO machine_log (machine_id, production_date, production_shift, products_produced, defects, runtime)
VALUES (1, '2024-06-01', 'Morning', 500, 5, 8.0), (1, '2024-06-01', 'Evening', 450, 3, 7.5),
	(2, '2024-06-01', 'Morning', 480, 2, 7.8), (2, '2024-06-01', 'Evening', 470, 4, 8.1),
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), (3, '2024-06-01', 'Evening', 520, 1, 7.9),
	(1, '2024-06-02', 'Morning', 490, 3, 8.0), (1, '2024-06-02', 'Evening', 460, 2, 7.6),
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), (2, '2024-06-02', 'Evening', 465, 5, 8.3),
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), (3, '2024-06-02', 'Evening', 515, 3, 8.2);
/* In Manufacturers monitor production data to ensure efficient operations and quality control,
identify machines with the highest defect rates and their average runtimes.*/
select machine_id from machine_log;
select machine_id,(avg(defects)/avg(products_produced))as defect_rate,avg(runtime)as avg_runtime from machine_log
	group by machine_id order by defect_rate;
select machine_id,(avg(defects)/avg(products_produced))as defect_rate,avg(runtime)as avg_runtime from machine_log
	group by machine_id order by defect_rate desc limit 1;

-------------------------------------------------------------------------------------------------------------

/*ASSIGNMENT 2
*/
CREATE TABLE student_result (
    grade_id SERIAL PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    course_id VARCHAR(20) NOT NULL,
    grade FLOAT NOT NULL,
    grade_date DATE NOT NULL
);
INSERT INTO student_result (student_id, course_id, grade, grade_date)
VALUES 
(1, 101, 85.5, '2024-01-15'), (1, 102, 78.0, '2024-02-20'), (2, 101, 92.0, '2024-01-15'), 
(2, 103, 88.5, '2024-03-10'), (3, 102, 74.0, '2024-02-20'), (3, 103, 81.5, '2024-03-10'), 
(4, 101, 67.0, '2024-01-15'), (4, 104, 90.0, '2024-04-05'), (5, 102, 85.0, '2024-02-20'), 
(5, 104, 87.0, '2024-04-05');
/*Educational institutions track student performance to provide targeted support and interventions.
identify students with an average grade below a passing threshold in their courses.
*/
select * from student_result;
SELECT student_id, avg(grade) as average_grade FROM student_result
GROUP BY student_id HAVING AVG(grade) < 80;

------------------------------------------------------------------------------------------


/*ASSIGNMENT 3
*/
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(300) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(500) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    plan_id VARCHAR(20) NOT NULL,
    last_call_date DATE NOT NULL
);
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, zip_code, plan_id, last_call_date)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'), 
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'), 
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'), 
('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'), 
('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'), 
('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'), 
('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'), 
('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'), 
('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22');
/*Telecom companies analyze customer data to identify patterns that indicate potential churn.
categorizes customers based on their activity levels, indicating their risk of churn.
*/
select * from customers;
SELECT customer_id,age(current_date,last_call_date) AS days_since_last_call from customers group by customer_id order by days_since_last_call desc; --was giving in year month day fromat
SELECT customer_id,(CURRENT_DATE - MAX(last_call_date)) AS days_since_last_call from customers group by customer_id order by days_since_last_call desc; -- now gives in total days format
SELECT customer_id,(CURRENT_DATE - MAX(last_call_date)) AS days_since_last_call,
	case
		when (CURRENT_DATE - MAX(last_call_date))>=90 then 'high risk'
		when 90>(CURRENT_DATE - MAX(last_call_date))and (CURRENT_DATE - MAX(last_call_date))>30 then 'medium risk'
		else 'low risk'
	end as churn_list
	from customers group by customer_id order by days_since_last_call desc;

------------------------------------------------------------------------------------------------


/* SUB ASSIGNMENT OF 3RD
*/
CREATE TABLE products (
    product_id serial PRIMARY KEY,
    product_name varchar(100) NOT NULL,
    category varchar(50),
    quantity integer,
    price float,
    supplier varchar(100),
    last_restock_date date
);
INSERT INTO products (product_name, category, quantity, price, supplier, last_restock_date)
VALUES
    ('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'),
    ('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'),
    ('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'),
    ('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'),
    ('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'),
    ('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'),
    ('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'),
    ('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'),
    ('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'),
    ('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15');
/*Retailers need to manage their inventory to ensure products are in stock and
to avoid overstocking.identify products with low stock levels.*/
select * from products;
select * from products where quantity<80;
-------------------------------------------------------------------------------------

/*ASSIGNMENT 4
*/
CREATE TABLE patients (
    patient_id serial PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    date_of_birth date,
    gender varchar(10),
    phone_number varchar(20),
    email varchar(200),
    address varchar(300),
    city varchar(100),
    state varchar(50),
    zip_code varchar(10),
    medical_history varchar,
    last_visit_date date
);
INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone_number, email, address, city, state, zip_code, medical_history, last_visit_date)
VALUES
    ('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'),
    ('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'),
    ('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'),
    ('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'),
    ('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'),
    ('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'),
    ('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'),
    ('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'),
    ('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'),
    ('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22');
/*Healthcare providers need to manage patient records efficiently for better healthcare delivery.
Write query retrieves patient information for those who visited within a specific date range.*/
select  * from patients where last_visit_date between '2024-05-01' and '2024-06-01';

-------------------------------------------------------------------------------------------------------


/* ASSIGNMENT 5 */

CREATE TABLE transactions (
    transaction_id serial PRIMARY KEY,
    account_id varchar(50) NOT NULL,
    transaction_date timestamp,
    transaction_amount float,
    transaction_type varchar(20),
    merchant varchar(100),
    location varchar(100),
    status varchar(20)
);
INSERT INTO transactions (account_id, transaction_date, transaction_amount, transaction_type, merchant, location, status)
VALUES
    (1, '2024-06-01 10:00:00', 1000.00, 'Credit', 'Amazon', 'Online', 'Completed'),
    (1, '2024-06-01 12:30:00', 500.00, 'Debit', 'Walmart', 'Springfield', 'Completed'),
    (2, '2024-06-02 09:45:00', 15000.00, 'Credit', 'Apple Store', 'Chicago', 'Pending'),
    (2, '2024-06-02 11:00:00', 200.00, 'Debit', 'Starbucks', 'Chicago', 'Completed'),
    (3, '2024-06-03 14:15:00', 250.00, 'Debit', 'Target', 'Springfield', 'Completed'),
    (3, '2024-06-03 16:20:00', 30000.00, 'Credit', 'Tesla', 'San Francisco', 'Pending'),
    (4, '2024-06-04 08:30:00', 120.00, 'Debit', 'McDonalds', 'Springfield', 'Completed'),
    (4, '2024-06-04 10:50:00', 6000.00, 'Credit', 'Best Buy', 'Chicago', 'Pending'),
    (5, '2024-06-05 15:10:00', 70.00, 'Debit', 'CVS Pharmacy', 'Springfield', 'Completed'),
    (5, '2024-06-05 17:00:00', 22000.00, 'Credit', 'Louis Vuitton', 'New York', 'Pending');
/* Financial institutions need to detect and prevent fraudulent transactions.
Write query identifies transactions above a certain threshold within a specified 
date range for further investigation. */
select * from transactions;
select * from transactions where transaction_date between '2024-06-03' and '2024-06-06' and transaction_amount>10000;
