CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    total_purchase NUMERIC(10,2),
    signup_date DATE
);

INSERT INTO customers (first_name, last_name, email, phone, total_purchase, signup_date) VALUES
('Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543210', 15000.00, '2024-01-15'),
('Priya', 'Verma', 'priya.verma@example.com', '9123456780', 4200.50, '2024-02-10'),
('Aman', 'Gupta', 'aman.gupta@example.com', '9988776655', 850.00, '2024-03-05'),
('Sneha', 'Patel', 'sneha.patel@example.com', '9090909090', 22000.00, '2024-01-28'),
('Vikram', 'Singh', 'vikram.singh@example.com', '9012345678', 300.00, '2024-04-02');