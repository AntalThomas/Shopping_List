CREATE DATABASE shopping_list_db;
\c shopping_list_db

CREATE TABLE lists(
    id SERIAL PRIMARY KEY,
    name TEXT,
    linked_user INTEGER
);

CREATE TABLE items(
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