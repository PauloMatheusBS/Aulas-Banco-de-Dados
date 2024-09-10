CREATE DATABASE professores;
USE professores;

CREATE TABLE Professor (
    idProfessor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    especialidade VARCHAR(40),
    dtNasc DATE
);

INSERT INTO Professor (nome, especialidade, dtNasc) VALUES 
    ('Professor1', 'Matemática', '1980-05-15'),
    ('Professor2', 'Física', '1975-11-22'),
    ('Professor3', 'Matemática', '1983-10-13'),
    ('Professor4', 'Química', '1990-07-30'),
    ('Professor5', 'Física', '1988-02-20'),
    ('Professor6', 'Biologia', '1979-12-05');

-- a. Exibir todos os dados da tabela
SELECT * FROM Professor;
SET SQL_SAFE_UPDATES = 0;


-- b. Adicionar o campo funcao do tipo VARCHAR(50), onde a função só pode ser ‘monitor’, ‘assistente’ ou ‘titular’
ALTER TABLE Professor ADD funcao ENUM('monitor', 'assistente', 'titular');

-- c Atualizar os professores inseridos e suas respectivas funções
UPDATE Professor SET funcao = 'monitor' WHERE idProfessor IN (1, 2, 3);
UPDATE Professor SET funcao = 'assistente' WHERE idProfessor IN (4, 5);
UPDATE Professor SET funcao = 'titular' WHERE idProfessor = 6;

-- d. Inserir um novo professor
INSERT INTO Professor (nome, especialidade, dtNasc, funcao) VALUES 
    ('Professor7', 'História', '1985-03-15', 'monitor');

-- e. Excluir o professor onde o idProfessor é igual a 5
DELETE FROM Professor WHERE idProfessor = 5;

-- f.  Exibir apenas os nomes dos professores titulares
SELECT nome FROM Professor WHERE funcao = 'titular';

-- g. Exibir apenas as especialidades e as datas de nascimento dos professores monitores
SELECT especialidade, dtNasc FROM Professor WHERE funcao = 'monitor';

-- h. Atualizar a data de nascimento do idProfessor igual a 3
UPDATE Professor SET dtNasc = '1984-10-13' WHERE idProfessor = 3;

-- i. Limpar a tabela Professor
TRUNCATE TABLE Professor;
