CREATE DATABASE loja;
USE loja;

CREATE TABLE vendas(
id		INT		NOT NULL	auto_increment,
prod	VARCHAR(20)		NOT NULL,
valor	FLOAT,
PRIMARY KEY(id)
);

select * from vendas;