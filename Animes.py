import pandas as pd
import matplotlib.pyplot as plt



df_animes = pd.read_csv("C:\\Users\\PauloSouza\\Desktop\\Animes\\anime.csv")
top_animes = df_animes.sort_values(by='members', ascending=False).head(20)
bad_animes = df_animes.sort_values(by='members', ascending=True).head(20)
top_notas = df_animes.sort_values(by='rating', ascending=False).head(20)
bad_notas = df_animes.sort_values(by='rating').head(20)
tipo_contagem = top_notas['type'].value_counts()


df_animes.set_index('anime_id',inplace=True)
print(df_animes.head(10))
print(df_animes.info(10))
print(df_animes.columns)



###############Consultas########################
print(df_animes.query('episodes > "10"').head())
print(df_animes.query('episodes < "10"').head())
print(df_animes.query('type == "Movie"').head())
print(df_animes.query('type == "TV"').head())
print(df_animes.query('rating > 8.0').head())
print(df_animes.query('rating < 8.0 & rating >= 4.0').head())
print(df_animes.query('rating < 4.0').head())


###############Graficos########################

plt.figure(figsize=(12, 6))
plt.bar(top_animes['name'], top_animes['members'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Número de Membros por Anime (Top 20)')
plt.xlabel('Animes')
plt.ylabel('Número de Membros')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.bar(bad_animes['name'], bad_animes['members'], color='salmon')
plt.xticks(rotation=45, ha='right')
plt.title('Número de Membros por Anime (Piores 20)')
plt.xlabel('Animes')
plt.ylabel('Número de Membros')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.bar(top_notas['name'], top_notas['rating'], color='lightgreen')
plt.xticks(rotation=45, ha='right')
plt.title('Maiores Notas por Anime (Top 20)')
plt.xlabel('Animes')
plt.ylabel('Notas')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.bar(bad_notas['name'], bad_notas['rating'], color='salmon')
plt.xticks(rotation=45, ha='right')
plt.title('Menores Notas por Anime (Top 20)')
plt.xlabel('Animes')
plt.ylabel('Notas')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 10))
plt.pie(tipo_contagem, labels=tipo_contagem.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral', 'green'])
plt.title('Distribuição de Tipos entre os 10 Animes com Maiores Notas')
plt.show()




