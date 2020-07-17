CREATE DATABASE flaskcontacts;

USE flaskcontacts;

/* TABLE USER*/
CREATE TABLE contacts (
    id INT(11) NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    email VARCHAR(60) NOT NULL
);

ALTER TABLE contacts
    ADD PRIMARY KEY (id);

ALTER TABLE contacts
    MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;
