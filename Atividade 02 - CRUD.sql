CREATE DATABASE sprite;
USE sprite;


CREATE TABLE Filme (
    idFilme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(50),
    genero VARCHAR(40),
    diretor VARCHAR(40)
);


INSERT INTO Filme (titulo, genero, diretor) VALUES 
    ('Filme1', 'Ação', 'Diretor1'),
    ('Filme2', 'Comédia', 'Diretor1'),
    ('Filme3', 'Drama', 'Diretor2'),
    ('Filme4', 'Suspense', 'Diretor3'),
    ('Filme5', 'Ação', 'Diretor4'),
    ('Filme6', 'Comédia', 'Diretor2'),
    ('Filme7', 'Suspense', 'Diretor4');

-- a. Exibir todos os dados da tabela
SELECT * FROM Filme;
SET SQL_SAFE_UPDATES = 0;


-- b. Adicionar o campo protagonista do tipo VARCHAR(50) na tabela
ALTER TABLE Filme ADD protagonista VARCHAR(50);

-- c. Atualizar o campo protagonista de todos os filmes inseridos
UPDATE Filme SET protagonista = 'Ator Principal';

-- d. Modificar o campo diretor do tamanho 40 para o tamanho 150
ALTER TABLE Filme MODIFY diretor VARCHAR(150);

-- e. Atualizar o diretor do filme com id=5
UPDATE Filme SET diretor = 'NovoDiretor5' WHERE idFilme = 5;

-- f. Atualizar o diretor dos filmes com id=2 e com id=7
UPDATE Filme SET diretor = 'NovoDiretor2e7' WHERE idFilme IN (2, 7);

-- g. Atualizar o título do filme com o id=6
UPDATE Filme SET titulo = 'NovoTitulo6' WHERE idFilme = 6;

-- h. Excluir o filme com o id=3
DELETE FROM Filme WHERE idFilme = 3;

-- i. Exibir os filmes em que o gênero é diferente de 'drama'
SELECT * FROM Filme WHERE genero != 'Drama';

-- j. Exibir os dados dos filmes que o gênero é igual 'suspense'
SELECT * FROM Filme WHERE genero = 'Suspense';

-- k. Descrever os campos da tabela mostrando a atualização do campo protagonista e diretor
DESCRIBE Filme;

-- l. Limpar os dados da tabela
TRUNCATE TABLE Filme;
