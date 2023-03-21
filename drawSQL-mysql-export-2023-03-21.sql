CREATE TABLE `Employers`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` TEXT NOT NULL,
    `year` INT NOT NULL,
    `phone_num` BIGINT NOT NULL,
    `position` INT NOT NULL
);
ALTER TABLE
    `Employers` ADD PRIMARY KEY `employers_id_primary`(`id`);
CREATE TABLE `Orders`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `client` INT NOT NULL,
    `service` INT NOT NULL,
    `employer` INT NOT NULL
);
ALTER TABLE
    `Orders` ADD PRIMARY KEY `orders_id_primary`(`id`);
CREATE TABLE `Client_base`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` TEXT NOT NULL,
    `age` INT NOT NULL,
    `phone_num` BIGINT NOT NULL
);
ALTER TABLE
    `Client_base` ADD PRIMARY KEY `client_base_id_primary`(`id`);
CREATE TABLE `Service`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `price` BIGINT NOT NULL,
    `time` INT NOT NULL
);
ALTER TABLE
    `Service` ADD PRIMARY KEY `service_id_primary`(`id`);
CREATE TABLE `Position`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` TEXT NOT NULL,
    `salary` BIGINT NOT NULL,
    `service` INT NOT NULL
);
ALTER TABLE
    `Position` ADD PRIMARY KEY `position_id_primary`(`id`);
ALTER TABLE
    `Position` ADD CONSTRAINT `position_service_foreign` FOREIGN KEY(`service`) REFERENCES `Service`(`id`);
ALTER TABLE
    `Employers` ADD CONSTRAINT `employers_position_foreign` FOREIGN KEY(`position`) REFERENCES `Position`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_client_foreign` FOREIGN KEY(`client`) REFERENCES `Client_base`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_service_foreign` FOREIGN KEY(`service`) REFERENCES `Service`(`id`);
ALTER TABLE
    `Orders` ADD CONSTRAINT `orders_employer_foreign` FOREIGN KEY(`employer`) REFERENCES `Employers`(`id`);