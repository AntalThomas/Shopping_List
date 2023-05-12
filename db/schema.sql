CREATE DATABASE shopping_list_db;
\c shopping_list_db

CREATE TABLE lists(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name TEXT,
    linked_list TEXT
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name TEXT,
    linked_list TEXT
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);

INSERT INTO items(name, linked_list) VALUES('Carrots', 22);
INSERT INTO items(name, linked_list) VALUES('Apples', 22);
INSERT INTO items(name, linked_list) VALUES('Blake', 15);