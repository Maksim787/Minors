import pandas as pd

with open("site.txt", encoding="utf-8") as file:
    site = file.readlines()
site = list(map(lambda x: x.strip(), site))

start = site.index(
    "Майнор	Мин./Макс. кол-во мест	Выбрали первым приоритетом	Выбрали вторый приоритетом	Выбрали третьим приоритетом"
)
end = site.index("Записи с 1 до 86 из 86 записей")
site = site[start + 1:end]

minors = []
index = []

for line in site:
    name_index = 0
    while not line[name_index].isalpha():
        name_index += 1
    name_start = name_index
    while line[name_index] != '6':
        name_index += 1
    name_end = name_index

    name = line[name_start:name_end].strip()
    line = line[:name_start] + line[name_end:]
    i, min_max, first, second, third = line.split()
    i = int(i)
    min_places, max_places = map(int, min_max.split('/'))
    first = int(first)
    second = int(second)
    third = int(third)
    minors.append([name, min_max, first, second, third])
    index.append(i)

df = pd.DataFrame(minors, index=index, columns=["name", "places", "first", "second", "third"])
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = df.sort_values(by=["first", "second", "third"], ascending=False)
print(sum(df["first"]))
print(sum(df["second"]))
print(sum(df["third"]))
df.to_csv("Minors.csv")
print(df)
