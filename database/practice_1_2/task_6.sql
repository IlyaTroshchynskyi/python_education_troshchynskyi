--Get statistics the orders for certain month and year

CREATE TABLE statistics_rent_by_month
(
    id serial PRIMARY KEY,
	year_rent integer NOT NULL,
    month_rent integer,
    count_rent integer
);


CREATE OR REPLACE FUNCTION rent_by_month()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
declare
	rec record;
BEGIN
    SELECT * FROM statistics_rent_by_month INTO rec WHERE
     year_rent = EXTRACT(YEAR FROM NEW.date_rent) AND month_rent = EXTRACT(MONTH FROM NEW.date_rent);

	if not found then
	INSERT INTO statistics_rent_by_month(year_rent, month_rent, count_rent)
		 VALUES(EXTRACT(YEAR FROM NEW.date_rent), EXTRACT(MONTH FROM NEW.date_rent), 1);
	else
	    UPDATE statistics_rent_by_month SET count_rent = count_rent + 1 WHERE
		 year_rent = EXTRACT(YEAR FROM NEW.date_rent) AND month_rent = EXTRACT(MONTH FROM NEW.date_rent);
	end if;
	RETURN NEW;
END;$$;

DROP TRIGGER statistics_rent_by_month;
CREATE TRIGGER statistics_rent_by_month
	AFTER INSERT
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE rent_by_month();


INSERT INTO orders(date_rent, rent_period, car_id, customer_id)
	VALUES ('2021-11-27', 1, 1, 1);


INSERT INTO orders(date_rent, rent_period, car_id, customer_id)
	VALUES ('2021-11-27', 2, 2, 2);

SELECT * FROM statistics_rent_by_month;








--If user wants to update the price model car should not be in future order.

CREATE OR REPLACE FUNCTION update_price()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
DECLARE
    id integer;
BEGIN

    SELECT model_id INTO id FROM car_model INNER JOIN cars USING(model_id)
    INNER JOIN orders USING (car_id) WHERE date_rent > now() AND car_model.model_id = OLD.model_id;
	IF FOUND THEN
	    RAISE EXCEPTION 'You can update the price of model when this model are not in orders after current date';
	END IF;
	RETURN NEW;
END;$$;

DROP TRIGGER validate_price_updating;
CREATE TRIGGER validate_price_updating
	BEFORE UPDATE
	ON car_model
	FOR EACH ROW
	EXECUTE PROCEDURE update_price();


UPDATE car_model SET price = 100 WHERE model_id = 15814;