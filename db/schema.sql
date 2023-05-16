CREATE DATABASE shopping_list_db;
\c shopping_list_db

CREATE TABLE lists(
    id SERIAL PRIMARY KEY,
    name TEXT,
    linked_user INTEGER,
    favourite INTEGER
);

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name TEXT,
    linked_list INTEGER,
    linked_user INTEGER,
    crossed_off INTEGER
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);