#1
import os


if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популрна мова програмування. \n")
        file.write("Python - використовується для роботи з даними. \n")
        file.write("Файли дозволяють зберігати інфорацію. \n")
        file.write("Python - вимагає практики. \n")
        file.write("Сьогодні ми працюємо з текствими файлами. \n")

tch = 0
tdig = 0
twords = 0
tlines = 0
lline = ""
lline_num = 0

with open('text.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    tlines = len(lines)

    for i, line in enumerate(lines, 1):
        tch += len(line.rstrip('\n'))
        twords += len(line.split())

        for chr in line:
            if chr.isdigit():
                tdig += 1

        if len(line.rstrip('\n')) > len(lline.rstrip('\n')):
            lline = line
            lline_num = i

print(f"Рядків: {tlines}")
print(f"Слів: {twords}")
print(f"Символів: {tch}")
print(f"Найдовший рядок: №{lline_num}, {len(lline.rstrip('\n'))} символів")
print(f"Текст: {lline.strip()}")

#2
import os

fg = input()
if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування. \n")
        file.write("Python - використовується для роботи з даними. \n")
        file.write("Файли дозволяють зберігати інформацію. \n")
        file.write("Python - вимагає практики. \n")
        file.write("Сьогодні ми працюємо з текстовими файлами. \n")

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

results = False

for inx, line in enumerate(lines, start=1):
    if fg.lower() in line.lower():
        print(f"{inx}: {line.strip()}")
        results = True

if not results:
    print("Збігів не знайдено.")

#3

if not os.path.exists('st.txt'):
    with open('st.txt', 'w', encoding='utf-8') as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Petrenko Ivan;76\n")
        file.write("Komarova Olha;97\n")

with open('st.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

st = []

for line in lines:
    line = line.strip()
    if line:
        name, scr = line.split(';')
        sc = int(scr)
        if sc > 80:
            st.append((name, sc))

def gsc(student):
    return student[1]

st.sort(key=gsc, reverse=True)

with open('result.txt', 'w', encoding='utf-8') as file:
    for name, sc in st:
        file.write(f"{name};{sc}\n")


