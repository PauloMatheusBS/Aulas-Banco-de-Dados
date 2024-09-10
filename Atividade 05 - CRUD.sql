CREATE DATABASE Curso;
USE professores;


CREATE TABLE Curso (
    idCurso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    sigla VARCHAR(3),
    coordenador VARCHAR(50)
);


INSERT INTO Curso (nome, sigla, coordenador) VALUES 
    ('Curso de Matemática', 'MAT', 'Coordenador1'),
    ('Curso de Física', 'FIS', 'Coordenador2'),
    ('Curso de Química', 'QUI', 'Coordenador3');

-- a. Exibir todos os dados da tabela
SELECT * FROM Curso;
SET SQL_SAFE_UPDATES = 0;

-- b. Exibir apenas os coordenadores dos cursos
SELECT coordenador FROM Curso;

-- c. Exibir apenas os dados dos cursos de uma determinada sigla
SELECT * FROM Curso WHERE sigla = 'MAT';

-- d. Exibir os dados da tabela ordenados pelo nome do curso
SELECT * FROM Curso ORDER BY nome;

-- e. Exibir os dados da tabela ordenados pelo nome do coordenador em ordem decrescente
SELECT * FROM Curso ORDER BY coordenador DESC;

-- f. Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra
SELECT * FROM Curso WHERE nome LIKE 'a%';

-- g. Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra
SELECT * FROM Curso WHERE nome LIKE '%b';

-- h. Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma determinada letra
SELECT * FROM Curso WHERE nome LIKE '_c%';

-- 11. i) Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma determinada letra
SELECT * FROM Curso WHERE nome LIKE '%d_';

-- 12. j) Eliminar a tabela
DROP TABLE Curso;
