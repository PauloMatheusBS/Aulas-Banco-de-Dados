CREATE DATABASE revistas;
USE revistas;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE Revista (
    idRevista INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    categoria VARCHAR(30)
);


INSERT INTO Revista (nome) VALUES 
    ('Veja'),
    ('Isto é'),
    ('Epoca'),
    ('Quatro Rodas');


SELECT * FROM Revista;

-- 1. Atualizar os dados das categorias das 3 revistas inseridas
UPDATE Revista SET categoria = 'Notícias' WHERE nome = 'Veja';
UPDATE Revista SET categoria = 'Atualidades' WHERE nome = 'Isto é';
UPDATE Revista SET categoria = 'Atualidades' WHERE nome = 'Epoca';

-- 2. Exibir os dados da tabela novamente para verificar se atualizou corretamente
SELECT * FROM Revista;

-- 3. Inserir mais 3 registros completos
INSERT INTO Revista (nome, categoria) VALUES 
    ('Claudia', 'Moda'),
    ('Superinteressante', 'Ciência'),
    ('Info', 'Tecnologia');

-- 4. Exibir novamente os dados da tabela
SELECT * FROM Revista;

-- 5. Exibir a descrição da estrutura da tabela
DESCRIBE Revista;

-- 6. Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres
ALTER TABLE Revista MODIFY categoria VARCHAR(40);

-- 7. Exibir novamente a descrição da estrutura da tabela para verificar a alteração
DESCRIBE Revista;

-- 8. Acrescentar a coluna periodicidade à tabela, que é VARCHAR(15)
ALTER TABLE Revista ADD periodicidade VARCHAR(15);

-- 9. Exibir os dados da tabela
SELECT * FROM Revista;

-- 10. Excluir a coluna periodicidade da tabela
ALTER TABLE Revista DROP COLUMN periodicidade;

