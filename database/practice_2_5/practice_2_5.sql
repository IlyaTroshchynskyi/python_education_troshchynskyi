CREATE TABLE test_orders
(
    order_id serial PRIMARY KEY,
    carts_cart_id integer REFERENCES carts (cart_id),
    order_status_order_status_id integer REFERENCES order_status (order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2)
);
--Generated 117000 rows;

INSERT INTO test_orders
(carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
SELECT carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at
FROM orders;


SELECT * FROM test_orders;

-- Look for orders which cost more than average price * 1.5
-- Without index "Execution Time: 76.262 ms"
-- With index "Execution Time: 50.368 ms"
BEGIN;
CREATE INDEX ON test_orders(total);
WHERE total > (SELECT AVG(total) *1.5 FROM test_orders);


EXPLAIN ANALYZE SELECT * FROM test_orders
WHERE total > (SELECT AVG(total) *1.5 FROM test_orders);
ROLLBACK;



CREATE TABLE test_users (
    user_id serial PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff BOOLEAN,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT
);

--Generated 102000 rows
INSERT INTO test_users
(email, password, first_name, last_name, middle_name, is_staff, country, city, address)
SELECT email, password, first_name, last_name, middle_name, is_staff, country, city, address
FROM users;


--Look for password which starts with 5 and end with 8;
--"Execution Time: 37.907 ms"
--"Execution Time: 1.054 ms"


SELECT * FROM test_users;
BEGIN;
CREATE INDEX ON test_users(password)
WHERE SUBSTR(password, 1, 1) = '5' AND SUBSTR(password, LENGTH(password), 1) = '8';

EXPLAIN ANALYZE SELECT email, password
FROM test_users WHERE SUBSTR(password, 1, 1) = '5' AND SUBSTR(password, LENGTH(password), 1) = '8';

ROLLBACK;



SELECT * FROM test_orders;

Look for orders as of month of quarter in 2020
--"Execution Time: 59.564 ms"
--"Execution Time: 6.667 ms"

BEGIN;
CREATE INDEX ON test_orders(created_at)
WHERE EXTRACT(YEAR FROM created_at) = 2020 AND EXTRACT(MONTH FROM created_at) IN (3,6,9,12);


EXPLAIN ANALYZE SELECT * FROM test_orders WHERE
EXTRACT(YEAR FROM created_at) = 2020 AND EXTRACT(MONTH FROM created_at) = 12
ROLLBACK;


Look for finished orders;
--"Execution Time: 39.569 ms"
--"Execution Time: 14.427 ms"

BEGIN;
CREATE INDEX ON test_orders(order_status_order_status_id);

EXPLAIN ANALYZE SELECT order_id FROM test_orders
WHERE order_status_order_status_id IN
(SELECT order_status_id FROM order_status WHERE status_name = 'Finished')
ROLLBACK;
