# Utilizamos a blibioteca Random para ter números aleatórios, ja que python não faz isso naturalmente.
import random

# Criamos uma classe chamada student que vai segurar os atributos necessários para um Estudante
class student :
    # Dentro da classe definimos INIT que faz com que sejamos capaz de dar atributos a classe.
    def __init__(self, matrícula, sexo, altura, statusFisico) -> None:
        self.matrícula = matrícula
        self.sexo = sexo
        self.altura = altura
        self.statusFisico = statusFisico

# Definimos variáveis para uso posterior, mesmo que elas não sejam absolutamente necessárias aqui.
listaEstudantes = []
mat = 0
sexo = ""
altura = 0
statusFisico = 1

quantidadeAlunas170Altura = 0
quantidadeAlunosFisico1 = 0

# Definimos um Método para selecionar o sexo do aluno. "Também poderiamos fazer isso para o status físico mas decidi que nível fica melhor" - Luís
def sexoAleatório():
    sexo = ["Masculino","Feminino"]
    return random.choice(sexo)

# Primeiro criamos um loop para definir aleatóriamente as variáveis dos alunos.
for i in range(50):
    # Nota-se que o número da matricula inicia-se em 111.111. Puramente cosmético, isso impede que tenha números de matricula abaixo de 
    mat = random.randint(111111,999999)
    sexo = sexoAleatório()
    altura = random.randint(130,220)
    statusFisico = random.randint(1,3)
    estudante = student(mat,sexo,altura,statusFisico)
    listaEstudantes.append(estudante)

for aluno, student in enumerate(listaEstudantes, start= 1):
    print(f"Aluno {aluno}: Matricula : {student.matrícula}, sexo : {student.sexo}, altura : {student.altura} e Nivel Fisico {student.statusFisico}")
    if student.sexo == "Feminino" and student.altura >= 171:
        quantidadeAlunas170Altura += 1
    if student.sexo == "Masculino" and student.statusFisico == 1:
        quantidadeAlunosFisico1 += 1

print("A Quantidade de alunas com altura superior mas não igual a 1.70 M é de :", quantidadeAlunas170Altura)
print("A Quantidade de alunos homens com um bom status fisico, em porcentagem a quantia de alunos totais é de :", int((quantidadeAlunosFisico1 / 50) * 100), "%")




