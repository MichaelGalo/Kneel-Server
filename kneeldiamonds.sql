-- Delete Commands if Needed
-- Delete all records from each table
DELETE FROM `Orders`;
DELETE FROM `Jewelry`;
DELETE FROM `Metals`;
DELETE FROM `Style`;
DELETE FROM `Sizes`;

-- Drop each table
DROP TABLE IF EXISTS `Orders`;
DROP TABLE IF EXISTS `Jewelry`;
DROP TABLE IF EXISTS `Metals`;
DROP TABLE IF EXISTS `Style`;
DROP TABLE IF EXISTS `Sizes`;

-- Table Creation 
CREATE TABLE `Jewelry`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `jewelryId` INTEGER NOT NULL,
    `metalId` INTEGER NOT NULL,
    `sizeId` INTEGER NOT NULL,
    `styleId` INTEGER NOT NULL,
    FOREIGN KEY (`jewelryId`) REFERENCES `Jewelry`(`id`),
    FOREIGN KEY (`metalId`) REFERENCES `Metal`(`id`),
    FOREIGN KEY (`sizeId`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY (`styleId`) REFERENCES `Style`(`id`)
);

-- Insert Statements For Seeding
-- Insert data into Style table
INSERT INTO `Style` (`id`, `style`, `price`) VALUES (1, 'Classic', 500);
INSERT INTO `Style` (`id`, `style`, `price`) VALUES (2, 'Modern', 710);
INSERT INTO `Style` (`id`, `style`, `price`) VALUES (3, 'Vintage', 965);

-- Insert data into Sizes table
INSERT INTO `Sizes` (`id`, `carets`, `price`) VALUES (1, 0.5, 405);
INSERT INTO `Sizes` (`id`, `carets`, `price`) VALUES (2, 0.75, 782);
INSERT INTO `Sizes` (`id`, `carets`, `price`) VALUES (3, 1, 1470);
INSERT INTO `Sizes` (`id`, `carets`, `price`) VALUES (4, 1.5, 1997);
INSERT INTO `Sizes` (`id`, `carets`, `price`) VALUES (5, 2, 3638);

-- Insert data into Metal table
INSERT INTO `Metals` (`id`, `metal`, `price`) VALUES (1, 'Sterling Silver', 12.42);
INSERT INTO `Metals` (`id`, `metal`, `price`) VALUES (2, '14K Gold', 736.4);
INSERT INTO `Metals` (`id`, `metal`, `price`) VALUES (3, '24K Gold', 1258.9);
INSERT INTO `Metals` (`id`, `metal`, `price`) VALUES (4, 'Platinum', 795.45);
INSERT INTO `Metals` (`id`, `metal`, `price`) VALUES (5, 'Palladium', 1241);

-- Insert data into Jewelry table
INSERT INTO `Jewelry` (`id`, `type`, `price`) VALUES (1, 'Ring', 100);
INSERT INTO `Jewelry` (`id`, `type`, `price`) VALUES (2, 'Necklace', 200);
INSERT INTO `Jewelry` (`id`, `type`, `price`) VALUES (3, 'Earring', 300);

-- Insert data into Orders table
INSERT INTO `Orders` (`id`, `jewelryId`, `metalId`, `sizeId`, `styleId`) VALUES (1, 1, 1, 2, 1);
INSERT INTO `Orders` (`id`, `jewelryId`, `metalId`, `sizeId`, `styleId`) VALUES (2, 2, 3, 3, 2);
