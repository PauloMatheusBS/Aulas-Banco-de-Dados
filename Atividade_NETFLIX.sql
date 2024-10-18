CREATE DATABASE NETFLIX;
USE NETFLIX;

CREATE TABLE usuarios (
    email VARCHAR(255) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    cpf VARCHAR(14) UNIQUE NOT NULL,
    endereco_cobranca TEXT NOT NULL,
    numero_cartao_credito VARCHAR(20) NOT NULL
);


CREATE TABLE mensalidades (
    numero_cobranca INT AUTO_INCREMENT PRIMARY KEY,
    email_usuario VARCHAR(255) NOT NULL,
    data_cobranca DATE NOT NULL,
    status_pag ENUM('Pendente', 'Pago') DEFAULT 'Pendente',
    FOREIGN KEY (email_usuario) REFERENCES usuarios(email)
);


CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE videos (
    id_videos INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano_producao YEAR NOT NULL,
    duracao INT NOT NULL, 
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria)
);


CREATE TABLE episodios (
    id_episodios INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano_producao YEAR NOT NULL,
    duracao INT NOT NULL, 
    temporada INT NOT NULL,
    numero_ep INT NOT NULL,
    proximo_ep_id INT,
    serie_id INT NOT NULL,
    FOREIGN KEY (proximo_ep_id) REFERENCES episodios(id_episodios),
    FOREIGN KEY (serie_id) REFERENCES videos(id_videos),
    UNIQUE (serie_id, temporada, numero_ep)
);


CREATE TABLE documentarios (
    id_documentario INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano_producao YEAR NOT NULL,
    duracao INT NOT NULL, 
    nome_produtora VARCHAR(255) NOT NULL
);


CREATE TABLE avaliacoes (
    id_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
    email_usuario VARCHAR(255) NOT NULL,
    video_id INT NOT NULL,
    nota INT CHECK (nota BETWEEN 0 AND 10),
    FOREIGN KEY (email_usuario) REFERENCES usuarios(email),
    FOREIGN KEY (video_id) REFERENCES videos(id_videos),
    UNIQUE (email_usuario, video_id)
);


CREATE TABLE atores (
    id_ator INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    local_nascimento VARCHAR(255) NOT NULL
);


CREATE TABLE atores_videos (
    ator_id INT NOT NULL,
    video_id INT NOT NULL,
    FOREIGN KEY (ator_id) REFERENCES atores(id_ator),
    FOREIGN KEY (video_id) REFERENCES videos(id_videos),
    PRIMARY KEY (ator_id, video_id)
);


INSERT INTO categorias (nome) VALUES ('Filme');
INSERT INTO categorias (nome) VALUES ('Série');
INSERT INTO categorias (nome) VALUES ('Documentário');


CREATE TABLE filme (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    ano_de_produção DATE NOT NULL,
    duração_filme VARCHAR(255) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria)
);






