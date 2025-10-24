import pandas as pd

print("Datos dataframe:")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}   
df = pd.DataFrame(data) 
print(df)

print("Mayores de 25 años:")
mayores_25 = df[df['Age'] > 25]
print(mayores_25)

df=pd.read_csv('movies.csv')
#El parámetro index=False evita que se guarde una columna adicional con los índices del DataFrame
df.to_csv('archivo_movies.csv', index=False)
print("Datos CSV:", df)
#Columna id del archivo csv
print(df['id'])