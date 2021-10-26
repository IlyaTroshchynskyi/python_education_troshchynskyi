---Задание 1
--Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city

CREATE TABLE potential_customers
(
    id integer PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255)
);


--Заполните данными таблицу.

INSERT INTO potential_customers (id, email, name, surname, second_name, city)
SELECT user_id, email, first_name, last_name, middle_name, city FROM users;

SELECT * FROM potential_customers;

--Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17

SELECT name, email, 'potential' FROM potential_customers WHERE city = 'city 17'
UNION ALL
SELECT first_name, email, 'exists' FROM users WHERE city = 'city 17';


--Задание 2
--Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)

SELECT first_name, email FROM users ORDER BY city, first_name ASC;

--Задание 3
--Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества

SELECT categories.category_title, COUNT(categories.category_title) as count_category
FROM products INNER JOIN categories ON products.category_id = categories.category_id
GROUP BY categories.category_title
ORDER BY count_category DESC;


--Задание 4
--1. Вывести продукты, которые ни разу не попадали в корзину.

SELECT product_title FROM products LEFT JOIN cart_product ON
products.product_id = cart_product.products_product_id
WHERE cart_product.carts_cart_id IS NULL;

--2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).

SELECT product_title FROM products
INNER JOIN cart_product ON products.product_id = cart_product.products_product_id
INNER JOIN carts ON cart_product.carts_cart_id = carts.cart_id
LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
WHERE orders.carts_cart_id IS NULL;

--3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.

SELECT product_title, COUNT(product_title) count_in_carts FROM products
INNER JOIN cart_product ON products.product_id = cart_product.products_product_id
GROUP BY product_title
ORDER BY count_in_carts DESC
LIMIT 10;

--4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.

SELECT product_title, COUNT(product_title) count_orders FROM products
INNER JOIN cart_product ON products.product_id = cart_product.products_product_id
INNER JOIN carts ON cart_product.carts_cart_id = carts.cart_id
INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
GROUP BY product_title
ORDER BY count_orders DESC
LIMIT 10;

--5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).

SELECT user_id, first_name, SUM(orders.total) as total_orders FROM users
INNER JOIN carts ON users.user_id = carts.users_user_id
INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
GROUP BY user_id, first_name
ORDER BY total_orders DESC
LIMIT 5;



--6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).

SELECT user_id, first_name, COUNT(orders.order_id) as count_orders FROM users
INNER JOIN carts ON users.user_id = carts.users_user_id
INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
GROUP BY user_id, first_name
ORDER BY count_orders DESC
LIMIT 5;


--7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.


SELECT user_id, first_name, COUNT(users.user_id) as count_users FROM users
INNER JOIN carts ON users.user_id = carts.users_user_id
LEFT JOIN orders ON carts.cart_id = orders.carts_cart_id
WHERE orders.order_id IS NULL
GROUP BY user_id, first_name
ORDER BY count_users DESC
LIMIT 5;
