import pandas as pd

print(f'Задача №1.')
df = pd.read_csv('World-happiness-report-2024.csv')

print(f'\nПервые 5 строк данных:')
print(df.head())

print(f'\nИнформация о данныхЖ')
print(df.info())

print(f'\nCтатистическое описание')
print(df.describe())

print(f'\n\nЗадача №2.')

df = pd.read_csv('dz.csv')

# print(df.info()
group = df.groupby('City')['Salary'].mean()
print(f'Средняя зарплата по городам:')
print(group)