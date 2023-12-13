CREATE TABLE city (
    id INT PRIMARY KEY,
    name VARCHAR(30)
);

INSERT INTO `city` (`id`, `name`)
VALUES
	(1, 'New York'),
    (2, 'Lviv');


DELIMITER //


CREATE TRIGGER on_insert_address
BEFORE INSERT ON addrescalculate_statistics
FOR EACH ROW
BEGIN
    IF NEW.city_id IS NOT NULL AND NEW.city_id NOT IN (SELECT id FROM city) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No city with given city_id';
    END IF;
END //


CREATE TRIGGER prevent_data_modification
BEFORE UPDATE ON bank_account
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data in this table is not allowed';
END //

CREATE TRIGGER prevent_data_deletion
BEFORE DELETE ON bank_account
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion of data in this table is not allowed';
END //

CREATE TRIGGER restrict_names
BEFORE INSERT ON people
FOR EACH ROW
BEGIN
    IF NEW.first_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid name. Allowed names are: Svitlana, Petro, Olha, Taras';
    END IF;
END //

CREATE PROCEDURE insert_city ( 
    IN city_name VARCHAR(45)
)
BEGIN
    INSERT INTO city (name) VALUES (city_name);
END //

CREATE PROCEDURE insert_into_junction_table (
    IN property_id INT,
    IN reservation_id INT
)
BEGIN
    INSERT INTO property_has_reservations (property_id, reseravation_id) VALUES (property_id, reseravation_id);
END //

CREATE PROCEDURE insert_rows_in_package()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
       INSERT INTO city (name) VALUES (CONCAT('Noname', i));
       SET i = i + 1;
    END WHILE;
END //

CREATE FUNCTION `calculate_statistic`(
	operation VARCHAR(10)
) RETURNS int
    READS SQL DATA
BEGIN
	    DECLARE result DECIMAL DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(total_cost) INTO result FROM reservation;
    ELSEIF operation = 'max' THEN
        SELECT MAX(total_cost) INTO result FROM reservation;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(total_cost) INTO result FROM reservation;
  ELSEIF operation = 'sum'  THEN
        SELECT SUM(total_cost) INTO result FROM reservation;
    END IF;
    RETURN result;
END //

CREATE PROCEDURE `get_avg`(
	IN operation VARCHAR(3)
)
BEGIN
	DECLARE result INT;
    set result = calculate_statistic(operation);
    SELECT result;
END //

CREATE PROCEDURE create_tables_from_column(
    IN custom_column_name VARCHAR(45),
    IN custom_table_name VARCHAR(45)
)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 0;
    DECLARE table_name VARCHAR(45);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE num_columns INT;
    DECLARE column_list VARCHAR(255);
    DECLARE column_name VARCHAR(45);

    DECLARE mycursor CURSOR FOR SELECT price FROM user_view;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @query = CONCAT('CREATE OR REPLACE VIEW propery_view AS SELECT ', custom_column_name, ' AS price FROM ', custom_table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN mycursor;
    my_loop: LOOP
        FETCH mycursor INTO table_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_columns = FLOOR(1 + RAND() * 9);
		SELECT num_columns;
		SET column_list = '';
		WHILE b < num_columns DO
			SET column_name = CONCAT('column_', b + 1);
			SET column_list = CONCAT(column_list, column_name, ' INT ');
			IF b < num_columns - 1 THEN
				SET column_list = CONCAT(column_list, ', ');
			END IF;
			SET b = b + 1;
		END WHILE;
		SET b = 0;

        SET column_list = SUBSTRING(column_list, 1, LENGTH(column_list) - 1);

		SET @sql_query = CONCAT('CREATE TABLE IF NOT EXISTS ', table_name, '_', UNIX_TIMESTAMP(), ' (', column_list, ')');
		PREPARE stmt FROM @sql_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

        DROP VIEW IF EXISTS user_view;
        SET a = a + 1;
    END LOOP my_loop;

    CLOSE mycursor;
END //


DELIMITER //