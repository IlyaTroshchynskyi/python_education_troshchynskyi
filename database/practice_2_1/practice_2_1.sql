CREATE TABLE categories
(
    category_id integer PRIMARY KEY,
    category_title VARCHAR(25),
    category_description TEXT
);


CREATE TABLE products
(
    product_id integer PRIMARY KEY,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock integer,
    price FLOAT,
    slug VARCHAR(45),
    category_id integer REFERENCES categories (category_id)
);

CREATE TABLE users (
    user_id integer PRIMARY KEY,
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

CREATE TABLE carts
(
    cart_id integer PRIMARY KEY,
    users_user_id integer REFERENCES users (user_id),
    subtotal DECIMAL,
    total DECIMAL,
    timestamp TIMESTAMP(2)
);

CREATE TABLE order_status
(
    order_status_id integer PRIMARY KEY,
    status_name VARCHAR(255)
);



CREATE TABLE orders
(
    order_id integer PRIMARY KEY,
    carts_cart_id integer REFERENCES carts (cart_id),
    order_status_order_status_id integer REFERENCES order_status (order_status_id),
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2)
);



CREATE TABLE cart_product
(
    id serial PRIMARY KEY,
    carts_cart_id integer REFERENCES carts (cart_id),
    products_product_id integer REFERENCES products (product_id)
);

COPY categories(category_id, category_title, category_description)
FROM '/usr/src/categories.csv'
DELIMITER ',';

COPY products(product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM '/usr/src/products.csv'
DELIMITER ',';

COPY users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/usr/src/users.csv'
DELIMITER ',';

COPY carts(cart_id, users_user_id, subtotal, total, timestamp)
FROM '/usr/src/carts.csv'
DELIMITER ',';

COPY order_status(order_status_id, status_name)
FROM '/usr/src/order_statuses.csv'
DELIMITER ',';

COPY orders(order_id, carts_cart_id, order_status_order_status_id, shipping_total, total, created_at, updated_at)
FROM '/usr/src/orders.csv'
DELIMITER ',';


COPY cart_product(carts_cart_id, products_product_id)
FROM '/usr/src/cart_products.csv'
DELIMITER ',';


SELECT * FROM cart_product;
SELECT * FROM carts;
SELECT * FROM categories;
SELECT * FROM order_status;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM users;

ALTER TABLE users ADD COLUMN phone_number integer;

ALTER TABLE users ALTER COLUMN phone_number TYPE VARCHAR;

UPDATE products SET price = price * 2;