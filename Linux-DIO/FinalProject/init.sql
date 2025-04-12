CREATE DATABASE IF NOT EXISTS meubanco;

USE meubanco;

CREATE TABLE IF NOT EXISTS dados (
    AlunoID int AUTO_INCREMENT PRIMARY KEY,
    Nome varchar(50),
    Sobrenome varchar(50),
    Endereco varchar(150),
    Cidade varchar(50),
    Host varchar(50)
);
