import pandas as pd

# df = pd.read_csv('hh.csv')
# df['Test'] = [new for new in range(29)]
# print(df)
#
# df.drop('Test', axis=1, inplace=True)
# print(df)
#
# df.drop(28, axis=0, inplace=True)
# print(df)

# df = pd.read_csv('animal.csv')
# print(df)

# замена значений NaN на 0
# df.fillna(0, inplace=True)
# print(df)

# удаление подозрительных записей
# df.dropna(inplace=True)
# print(df)
#
# group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
# print(group)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
