INSERT INTO `reservation`.`people` (`first_name`, `last_name`)
VALUES
    ('John', 'Doe'),
    ('Jane', 'Smith'),
    ('David', 'Johnson'),
    ('Emily', 'Brown'),
    ('Michael', 'Wilson');

-- Insert data into `reservation`.`address` table
INSERT INTO `reservation`.`address` (`state`, `street`, `street_number`)
VALUES
    ('CA', '123 Main St', 101),
    ('NY', '456 Elm St', 202),
    ('TX', '789 Oak St', 303),
    ('FL', '321 Pine St', 404),
    ('IL', '567 Birch St', 505);

-- Insert data into `reservation`.`property_stats` table
INSERT INTO `reservation`.`property_stats` (`number_of_bedrooms`, `number_of_bathrooms`, `max_guests`, `price_per_night`)
VALUES
    (2, 2, 4, 150),
    (3, 2, 6, 200),
    (1, 1, 2, 100),
    (4, 3, 8, 250),
    (2, 1, 3, 120);

-- Insert data into `reservation`.`property` table
INSERT INTO `reservation`.`property` (`people_id`, `address_id`, `property_stats_id`)
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5);

-- Insert data into `reservation`.`reviews` table
INSERT INTO `reservation`.`reviews` (`rating`, `comment`, `review_date`, `people_id`)
VALUES
    (4.5, 'Great property!', '2023-09-15 10:00:00', 1),
    (5.0, 'Perfect stay!', '2023-09-16 11:30:00', 2),
    (4.0, 'Nice place.', '2023-09-17 09:45:00', 3),
    (4.2, 'Excellent service.', '2023-09-18 14:20:00', 4),
    (3.8, 'Good experience.', '2023-09-19 16:10:00', 5);

-- Insert data into `reservation`.`people_photos` table
INSERT INTO `reservation`.`people_photos` (`photo_url`, `people_id`)
VALUES
    ('john.jpg', 1),
    ('jane.jpg', 2),
    ('david.jpg', 3),
    ('emily.jpg', 4),
    ('michael.jpg', 5);

-- Insert data into `reservation`.`reservation_time` table
INSERT INTO `reservation`.`reservation_time` (`check_in_date`, `check_out_date`)
VALUES
    ('2023-10-01 15:00:00', '2023-10-05 10:00:00'),
    ('2023-10-03 14:00:00', '2023-10-07 11:00:00'),
    ('2023-10-05 16:00:00', '2023-10-09 12:00:00'),
    ('2023-10-07 13:00:00', '2023-10-11 09:30:00'),
    ('2023-10-09 12:30:00', '2023-10-13 08:45:00');

-- Insert data into `reservation`.`reservations` table
INSERT INTO `reservation`.`reservations` (`total_cost`, `status`, `people_id`, `reservation_time_id`)
VALUES
    (600.00, 'Confirmed', 1, 1),
    (800.00, 'Confirmed', 2, 2),
    (400.00, 'Confirmed', 3, 3),
    (1000.00, 'Confirmed', 4, 4),
    (480.00, 'Confirmed', 5, 5);

-- Insert data into `reservation`.`bank_accounts` table
INSERT INTO `reservation`.`bank_accounts` (`account_name`, `people_id`)
VALUES
    ('5375411425256161', 1),
    ('5375411441413131', 2),
    ('5375411441413535', 3),
    ('5375411441412121', 4),
    ('5375411441415555', 5);

-- Insert data into `reservation`.`property_has_reservations` table
INSERT INTO `reservation`.`property_has_reservations` (`property_id`, `reservations_id`)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);

-- Insert data into `reservation`.`reservations_history` table
INSERT INTO `reservation`.`reservations_history` (`reservations_id`, `people_id`)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);