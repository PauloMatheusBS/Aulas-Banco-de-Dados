import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("all_seasons.csv") #carregando arquivo


# # a = (1,2,3,4,5)
# # b = (1,2,3,4,5)

# # plt.plot(a,b,'r--o', ) #gerando a linha com cor e recursos
# # plt.plot((8,9),(1,5),'b--o', ) #gerando a linha com cor e recursos
# # plt.plot((15,22),(1,5),'g--o', ) #gerando a linha com cor e recursos
# # plt.ylabel(u'Salario') #linha vertical
# # plt.xlabel(u'Tempo') #linha horizontal
# # plt.title(u'Titulo') #titulo do grafico
# # plt.axis((0,6,0,20)) #limites do grafico
# # plt.show() #deve ser por ultimo, mostra o grafico


# # x = [1, 2, 3, 4, 5]
# # y1 = [1, 2, 3, 4, 5]
# # y2 = [2, 3, 4, 5, 6]
# # y3 = [3, 4, 5, 6, 7]

# # # Plotando várias linhas
# # plt.plot(x, y1, 'r--o', label='Linha 1')  # Linha vermelha
# # plt.plot(x, y2, 'b--o', label='Linha 2')  # Linha azul
# # plt.plot(x, y3, 'g--o', label='Linha 3')  # Linha verde

# # # Configurações do gráfico
# # plt.ylabel('Salário')  # Eixo vertical
# # plt.xlabel('Tempo')    # Eixo horizontal
# # plt.title('Título')    # Título do gráfico
# # plt.axis((0, 6, 0, 20))  # Limites do gráfico
# # plt.legend()           # Adiciona legenda
# # plt.grid(True)        # Adiciona grade para melhor visualização
# # plt.show()            # Mostra o gráfico
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Select the relevant columns
# df1 = df.loc[0:11145, ["player_height"]]
# df2 = df.loc[0:11145, ["player_weight"]]

# # # Combine the height and weight into a single DataFrame
# data = pd.concat([df1, df2], axis=1)

# # # Drop any rows with missing values
# data = data.dropna()

# # # Create a scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(data['player_height'], data['player_weight'], alpha=0.5)
# plt.title('Relação de Altura e Peso')
# plt.xlabel('Altura')
# plt.ylabel('Peso')
# plt.grid()
# plt.show()

# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.scatter(a,b)
# plt.show()  
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.bar(a,b)
# plt.show() 
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.hist(a,b)
# plt.show() 
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
a = (10,20,30)
explode=(0.1,0,0)
labels = ["HB20","Gol","Fusca"]
plt.pie(a,explode=explode,labels=labels,autopct='%.2f%%',shadow=True)
plt.title('Teste')
plt.grid(True)
plt.show()
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# anos = [
#     2000, 2001, 2002, 2003, 2004, 
#     2005, 2006, 2007, 2008, 2009, 
#     2010, 2011, 2012, 2013, 2014, 
#     2015, 2016, 2017, 2018, 2019, 
#     2020, 2021
# ]

# salarios_minimos = [
#     280.00, 300.00, 305.00, 350.00, 360.00, 
#     380.00, 400.00, 380.00, 415.00, 465.00, 
#     510.00, 545.00, 622.00, 678.00, 724.00, 
#     788.00, 880.00, 937.00, 954.00, 998.00, 
#     1045.00, 1100.00
# ]



# plt.plot(anos,salarios_minimos,'b--o', ) #gerando a linha com cor e recursos
# plt.ylabel(u'Valor') #linha vertical
# plt.xlabel(u'Ano') #linha horizontal
# plt.title(u'Titulo') #titulo do grafico
# plt.show() #deve ser por ultimo, mostra o grafico