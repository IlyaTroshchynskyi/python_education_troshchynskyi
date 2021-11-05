--Задание:
--Использовать транзакции для insert, update, delete на 3х таблицах.
--Предоставить разнообразные примеры включая возврат к savepoints.

CREATE TABLE test_users
(
    id serial PRIMARY KEY,
    name VARCHAR(255),
    age integer
);


INSERT INTO test_users(name, age) VALUES('Oleg', 20);
SELECT * FROM test_users;
BEGIN;
INSERT INTO test_users(name, age) VALUES('Petr', 22);
SAVEPOINT my_first;
UPDATE test_users
SET age = 40
WHERE name = 'Petr';

--Возраст не был обновлен в связи откатом к сейвпоинту
ROLLBACK TO my_first;
SELECT * FROM test_users;

COMMIT;


--==========================================================================================
BEGIN;
INSERT INTO test_users(name, age) VALUES('Den', 22);
SELECT * FROM test_users;
SAVEPOINT my_first;
UPDATE test_users
SET age = 40
WHERE name = 'Den';

SAVEPOINT my_second;

UPDATE test_users
SET age = 90
WHERE name = 'Den';
SAVEPOINT my_third;
--Too old должен оставить возраст 40
ROLLBACK TO my_second;
SELECT * FROM test_users;
COMMIT;

--=========================================================================================


BEGIN;
INSERT INTO test_users(name, age) VALUES('Sveta', 41);
UPDATE test_users SET age = age + 1;
-- выполняется параллельно:  DELETE FROM test_users WHERE age = 41;
COMMIT;
--ничего не удалиться

--===============================================================================================
BEGIN;
INSERT INTO test_users(name, age) VALUES('Sveta2', 41);
--Увидим свету2 без комита
SELECT * FROM test_users WHERE name = 'Sveta2'

-- выполняется параллельно:  INSERT INTO test_users(name, age) VALUES('Sveta3', 41);
--COMMIT;
--Увидим свету3 так как паралельная транзакция была закомичена
SELECT * FROM test_users WHERE name = 'Sveta3'
COMMIT;



--========================================================================================
CREATE TABLE posts
(
    id serial  PRIMARY KEY,
    title VARCHAR(255),
    full_text TEXT
);

INSERT INTO posts(title, full_text) VALUES('Pos1', 'Post first');
INSERT INTO posts(title, full_text) VALUES('Post2', 'Post second');

SELECT * FROM posts;
BEGIN;

INSERT INTO posts(title, full_text) VALUES('Post3', 'Post third');
DELETE FROM posts WHERE id = 3;
INSERT INTO posts(title, full_text) VALUES('Post3', 'Post third');

--Ищем по новому айди так как был инкрментирован хотя в таблице 3 записи
UPDATE posts
SET full_text = 'Post third edit'
WHERE id = 4;
SELECT * FROM posts WHERE full_text LIKE '%edit';


COMMIT;

--===============================================================================

CREATE TABLE schools
(
    number serial PRIMARY KEY,
    title VARCHAR(255)
);

INSERT INTO schools(title) VALUES('high');
INSERT INTO schools(title) VALUES('middle');
INSERT INTO schools(title) VALUES('low');

SELECT * FROM schools;

BEGIN;
DELETE FROM schools;
--Таблица не удалится
ROLLBACK;
SELECT * FROM schools;

--=====================================================================================
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;

UPDATE schools SET title = title || '_school';

SELECT * FROM schools;

--паралельная транзакция UPDATE schools SET title = title + '_school_new';
--COMMIT;
--не увидим изменений из параллельной транзакции
SELECT * FROM schools;
COMMIT;
ROLLBACK;

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
--паралельная транзакция DELETE schools WHERE id = 3';
--COMMIT;
--ОШИБКА: не удалось сериализовать доступ из-за параллельного изменения
UPDATE schools SET title = 'deleted' WHERE id = 3;
COMMIT;