-- DROP DATABASE IF EXISTS CaquiDB;
DROP DATABASE IF EXISTS db_ra169477;

-- CREATE DATABASE CaquiDB;
CREATE DATABASE db_ra169477;

-- USE CaquiDB
USE db_ra169477;

DROP TABLE IF EXISTS Instituto;

CREATE TABLE Instituto (
ID_Instituto		Int NOT NULL,
Nome				Varchar(75) NOT NULL,
Sigla				Varchar(10) NOT NULL,
Campus				Varchar(20) NOT NULL,

CONSTRAINT PK_Instituto
	PRIMARY KEY (ID_Instituto)
);

DROP TABLE IF EXISTS Gasto_Instituto;

CREATE TABLE Gasto_Instituto (
ID_Instituto		Int NOT NULL,
Receita_Total		Decimal (13,2),
Despesa_Total		Decimal (13,2),
Ano					Int NOT NULL,
ID					Int NOT NULL,

CONSTRAINT PK_Gasto_Instituto
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Auxilio_Estudantil;

CREATE TABLE Auxilio_Estudantil (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Auxilio_Estudantil
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Correios;

CREATE TABLE Correios (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Correios
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Despesas_Centralizadas;

CREATE TABLE Despesas_Centralizadas (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Despesas_Centralizadas
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Energia_Eletrica;

CREATE TABLE Energia_Eletrica (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Energia_Eletrica
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Estagiarios;

CREATE TABLE Estagiarios (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Estagiarios
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Obras_e_Instalacoes;

CREATE TABLE Obras_e_Instalacoes (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Obras_e_Instalacoes
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Pessoal_e_Reflexos;

CREATE TABLE Pessoal_e_Reflexos (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Pessoal_e_Reflexos
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Royalties;

CREATE TABLE Royalties (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Royalties
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Servico_de_Limpeza;

CREATE TABLE Servico_de_Limpeza (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Servico_de_Limpeza
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Telefone;

CREATE TABLE Telefone (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Telefone
	PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS Transporte;

CREATE TABLE Transporte (
ID					Int NOT NULL,
Descricao			Varchar(300),
Receita				Decimal(13,2),
Despesa				Decimal(13,2),
Ano					Int NOT NULL,
ID_Instituto		Int NOT NULL,

CONSTRAINT PK_Transporte
	PRIMARY KEY (ID)
);

ALTER TABLE Gasto_Instituto
	ADD CONSTRAINT FK_Instituto_Gasto_Instituto
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Auxilio_Estudantil
	ADD CONSTRAINT FK_Instituto_Auxilio_Estudantil
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Correios
	ADD CONSTRAINT FK_Instituto_Correios
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Despesas_Centralizadas
	ADD CONSTRAINT FK_Instituto_Despesas_Centralizadas
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Energia_Eletrica
	ADD CONSTRAINT FK_Instituto_Energia_Eletrica
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Estagiarios
	ADD CONSTRAINT FK_Instituto_Estagiarios
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Obras_e_Instalacoes
	ADD CONSTRAINT FK_Instituto_Obras_e_Instalacoes
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Pessoal_e_Reflexos
	ADD CONSTRAINT FK_Instituto_Pessoal_e_Reflexos
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Royalties
	ADD CONSTRAINT FK_Instituto_Royalties
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Servico_de_Limpeza
	ADD CONSTRAINT FK_Instituto_Servico_de_Limpeza
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Telefone
	ADD CONSTRAINT FK_Instituto_Telefone
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

ALTER TABLE Transporte
	ADD CONSTRAINT FK_Instituto_Transporte
		FOREIGN KEY (ID_Instituto)
		REFERENCES Instituto (ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Instituto.csv'
	INTO TABLE Instituto
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID_Instituto, Nome, Sigla, Campus);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Gasto Instituto.csv'
	INTO TABLE Gasto_Instituto
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID_Instituto, Receita_Total, Despesa_Total, Ano, ID);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Auxilio Estudantil.csv'
	INTO TABLE Auxilio_Estudantil
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Correios.csv'
	INTO TABLE Correios
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Despesas Centralizadas.csv'
	INTO TABLE Despesas_Centralizadas
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Energia Eletrica.csv'
	INTO TABLE Energia_Eletrica
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Energia Eletrica.csv'
	INTO TABLE Energia_Eletrica
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Estagiarios.csv'
	INTO TABLE Estagiarios
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Obras e Instalacoes.csv'
	INTO TABLE Obras_e_Instalacoes
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Pessoal e Reflexos.csv'
	INTO TABLE Pessoal_e_Reflexos
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Royalties.csv'
	INTO TABLE Royalties
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Servico de Limpeza.csv'
	INTO TABLE Servico_de_Limpeza
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Telefone.csv'
	INTO TABLE Telefone
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);

LOAD DATA LOCAL INFILE 'C:\\Users\\ra169477\\Desktop\\CaquiDB\\Transporte.csv'
	INTO TABLE Transporte
	CHARACTER SET 'UTF8'
	FIELDS TERMINATED BY '\t'
	IGNORE 1 LINES
	(ID, Descricao, Receita, Despesa, Ano, ID_Instituto);