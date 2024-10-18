import pandas as pd #importar e apelidar
# #print(pd.__version__) #printar versão
# df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv") #carregar arquivo
# #print(df.head(10)) #mostrar 10 primeiros
# # print(df.tail(10)) mostrar 10 ultimos
# #print(df.info(10)) #mostrar as colunas
# df.set_index('PassengerId',inplace=True) #tirar indice criado para colocar o da tabela
# # print(df.head(10)) #mostrando indice tirado
# # print(df.columns) #nome das colunas
# # print(df.values) #valores ds campos
# # print(df.loc[1]) #buscando valores do indice 1
# # print(df.loc[[1,2],['Name','Sex','Age']]) #aqui ele buscou indices 1 e 2 e mostra apenas os campos Name, Sex e Age
# # print(df.loc[1:10]) #for i in ...
# # print(df.loc[1:10:2]) #for in interval
# # print(df.loc[10:]) #a partir de ate ....
# # print(df.loc[1:10,['Name','Sex','Age']]) #search interval and columns
# # print(df.query('Age > 20').head())
# # print(df.query('Age > 20 & Sex == "male"').head()) concatenandoas querys
# #df.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig') #save




# def salva (i):
#     teste = i
#     teste.to_csv('dataset{i}.csv',sep=";", index=False,encoding='utf-8sig')
#     print("SALVOUUU!!!!")
#     i += 1
#     return teste

# i = 0
# print("TESTANDO")
# print(df.query('Survived == 1 & Age < 15').head()) 
# salva(i)
# # a = df.query('Survived == 1 & Age < 15').head()
# # a.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig')
# print(df.query('Survived == 1 & Sex == "male"').head())
# salva(i)
# # b = df.query('Survived == 1 & Sex == "male"').head()
# # b.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig')
# print(df.query('Survived == 1 & Sex == "female"').head())
# salva(i)
# # c = df.query('Survived == 1 & Sex == "female"').head()
# # c.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig')
# print(df.query('Survived == 1 & Age > 50').head())
# salva(i)
# # d = df.query('Survived == 1 & Age > 50').head()
# # d.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig')
# print(df.query('Survived == 1 & Age < 12 & Sex == "female"').head())
# salva(i)
# e = df.query('Survived == 1 & Age < 12 & Sex == "female"').head()
# e.to_csv('dataset.csv',sep=";", index=False,encoding='utf-8sig')
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
df = pd.read_csv("all_seasons.csv") 
 
