
--Задание 1
--Вывести:
--1. всех юзеров,

SELECT first_name, last_name, middle_name FROM users;

--2. все продукты,

SELECT product_title, product_description FROM products;
--3. все статусы заказов

SELECT status_name FROM order_status;



--Задание 2
--Вывести заказы, которые успешно доставлены и оплачены

SELECT order_id, order_status.status_name FROM orders
INNER JOIN order_status ON orders.order_status_order_status_id = order_status.order_status_id
WHERE order_status.status_name IN ('Paid', 'Finished')


--Задание 3
--Вывести:
--(если задание можно решить несколькими способами, указывай все)
--1. Продукты, цена которых больше 80.00 и меньше или равно 150.00

SELECT product_title, product_description, price FROM products
WHERE price BETWEEN 80.01 AND 150;

SELECT product_title, product_description, price FROM products WHERE price > 80 AND price <= 150;

--2. заказы совершенные после 01.10.2020 (поле created_at)
SELECT order_id, created_at FROM orders WHERE created_at > '2020.10.01'

--3. заказы полученные за первое полугодие 2020 года

SELECT order_id, created_at FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2020 AND
EXTRACT(MONTH FROM created_at) < 7;

SELECT order_id, created_at FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2020 AND
EXTRACT(MONTH FROM created_at) > 0 AND EXTRACT(MONTH FROM created_at) < 7;

SELECT order_id, created_at FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2020 AND
EXTRACT(MONTH FROM created_at) BETWEEN 1 AND 6;


--4. подукты следующих категорий Category 7, Category 11, Category 18

SELECT product_title, product_description, price, category_id FROM products
WHERE category_id IN (7, 11, 18);

SELECT product_title, product_description, price,category_id FROM products
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;


--5. незавершенные заказы по состоянию на 31.12.2020

SELECT order_id, created_at, order_status.status_name FROM orders
INNER JOIN order_status ON orders.order_status_order_status_id = order_status.order_status_id
WHERE created_at <= '2020.12.31' AND order_status.status_name NOT IN ('Finished', 'Canceled');

--6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.

SELECT cart_id, order_status.status_name FROM carts
INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
INNER JOIN order_status ON orders.order_status_order_status_id = order_status.order_status_id
WHERE order_status.status_name = 'Canceled';


SELECT cart_id FROM carts INNER JOIN orders ON
carts.cart_id = orders.carts_cart_id
WHERE orders.order_status_order_status_id = (SELECT order_status_id
FROM order_status WHERE status_name = 'Canceled');


--
--Задание 4
--Вывести:
--1. среднюю сумму всех завершенных сделок

SELECT AVG(total) FROM orders INNER JOIN order_status ON
orders.order_status_order_status_id = order_status.order_status_id
WHERE status_name = 'Finished'
GROUP BY order_id, status_name

--2. вывести максимальную сумму сделки за 3 квартал 2020

SELECT MAX(total) FROM orders INNER JOIN order_status ON
orders.order_status_order_status_id = order_status.order_status_id
WHERE EXTRACT(YEAR FROM created_at) = 2020 AND
status_name = 'Finished' AND EXTRACT(MONTH FROM created_at) BETWEEN 7 AND 9;