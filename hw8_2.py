import pandas as pd

data = {
    'name': ['Ivan', 'Kat', 'Bob', 'Mari' ,'Egor', 'David', 'Eve', 'Alice', 'Petr','Olga'],
    'algebra': [5, 4, 3, 4, 5, 4, 5, 5, 3, 5],
    'physics': [4, 3, 4, 5, 4, 5, 5, 3, 5, 3],
    'geography': [3, 4, 5, 4, 5, 5, 3, 5, 3, 5],
    'russian': [5, 5, 4, 5, 5, 3, 5, 3, 5, 4],
    'english': [4, 4, 4, 5, 3, 3, 5, 3, 5, 4]
}

df = pd.DataFrame(data)

# Первые 5 строк данных
print(f'Первые 5 строк данных:')
print(df.head())

# Средняя оценка по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("Средняя оценка по каждому предмету:")
print(mean_scores)

# Медианная оценка по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Первый (Q1) и третий (Q3) квартили для оценок по алгебре
Q1_math = df['algebra'].quantile(0.25)
Q3_math = df['algebra'].quantile(0.75)
print("\nКвартиль Q1 для оценок по алгебре:", Q1_math)
print("Квартиль Q3 для оценок по алгебре:", Q3_math)

print(f"IQR = {Q3_math - Q1_math}")

# Стандартное отклонение для оценок по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
