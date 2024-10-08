import pandas as pd
import matplotlib.pyplot as plt

df_prefeitos = pd.read_csv("C:\\Users\\PauloSouza\\Desktop\\Eleições 2024\\prefeitos_campo_grande_2024.csv")
df_vereadores = pd.read_csv("C:\\Users\\PauloSouza\\Desktop\\Eleições 2024\\vereadores_campo_grande_2024.csv")


print(df_prefeitos.head(10))
print(df_prefeitos.info(10))
print(df_prefeitos.columns)
print(df_vereadores.head(10))
print(df_vereadores.info(10))
print(df_vereadores.columns)


#########################################################################################################################################################################################
a = (31.67,29.56,25.96,9.43,2.45,0.70,0.24)
explode=(0.1,0,0,0,0,0,0)
nomesa = ["Adriane Lopes","Rose Modesto","Beto Pereira","Camila Jara","Beto Figueiró","Luso de Queiroz","Ubirajara Martins"]
plt.pie(a,explode=explode,labels=nomesa,autopct='%.2f%%',shadow=True)
plt.title('Prefeitura Campo Grande')
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.bar(nomesa, a, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Prefeitura Campo Grande')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()




b = (50.05,28.19,14.78,4.54,2.03,0.31,0.10)
explode=(0.1,0,0,0,0,0,0)
nomesb = ["Marçal Filho","Alan Guedes","Tiago Botelho","Bela Barros","Racib Harb","Beto Teles","Valderi Garcia"]
plt.pie(b,explode=explode,labels=nomesb,autopct='%.2f%%',shadow=True)
plt.title('Prefeitura Dourados')
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.bar(nomesb, b, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Prefeitura Dourados')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()



c = (68.61,28.88,2.51)
explode=(0.1,0,0)
nomesc = ["Dr Cassiano Maia","Dr Ruy Costa","Professor Vitor"]
plt.pie(c,explode=explode,labels=nomesc,autopct='%.2f%%',shadow=True)
plt.title('Prefeitura Três Lagoas')
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.bar(nomesc, c, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Prefeitura Três Lagoas')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()



d = (56.74,21.30,11.88,10.08)
explode=(0.1,0,0,0)
nomesd = ["Dr. Gabriel","Luiz Antonio Pardal","André Campos","Delcídio Amaral"]
plt.pie(d,explode=explode,labels=nomesd,autopct='%.2f%%',shadow=True)
plt.title('Prefeitura Corumbá')
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.bar(nomesd, d, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Prefeitura Corumbá')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()



e = (51.76,29.71,15.97,2.57)
explode=(0.1,0,0,0)
nomese = ["Eduardo Campos","Pompilio Júnior","Carlos Bernardo","Álvaro Soares"]
plt.pie(e,explode=explode,labels=nomese,autopct='%.2f%%',shadow=True)
plt.title('Prefeitura Ponta Porã')
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.bar(nomese, e, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Prefeitura Ponta Porã')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()

#########################################################################################################################################################################################
nomes = [
    "Marquinhos Trad",
    "Rafael Tavares",
    "Carlão Comunitário Mesmo",
    "Silvio Pitu",
    "Veterinário Francisco",
    "Fabio Rocha",
    "Professor Riverton",
    "Junior Coringa",
    "Dr Victor Rocha",
    "Professor Juari",
    "Flavio Cabo Almi",
    "Luiza Ribeiro",
    "André Salineiro Agente Federal",
    "Papy",
    "Ana Portela",
    "Neto Santos",
    "Maicon Nogueira",
    "Delei Pinheiro",
    "WIlson Lands",
    "Herculano Borges",
    "Beto Avelar",
    "Dr Jamal",
    "Landmark",
    "Dr Sandro",
    "Betinho",
    "Clodoilson Pires",
    "Jean Ferreira",
    "Professor João Rocha",
    "Valdir Gomes",
    "Dr Lívio"
]

votos = [
    8.567,
    8.128,
    6.912,
    6.409,
    6.371,
    6.314,
    6.271,
    6.131,
    5.355,
    5.050,
    5.003,
    4.982,
    4.782,
    4.641,
    4.577,
    4.576,
    4.236,
    4.179,
    4.148,
    4.119,
    4.063,
    4.030,
    4.022,
    3.922,
    3.877,
    3.859,
    3.768,
    3.693,
    3.648,
    3.636
]


plt.figure(figsize=(12, 6))
plt.bar(nomes, votos, color='skyblue')  
plt.xticks(rotation=45, ha='right')
plt.title('Vereadores Campo Grande')
plt.xlabel('Candidatos')
plt.ylabel('Número de Votos')
plt.tight_layout()
plt.show()
