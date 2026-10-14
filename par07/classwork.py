import os


# name = input("Enter your name: ")

# print("Створення файлу")

# with open('hello.txt', "w", encoding="utf-8") as file: #open - функція відкривае файл
#    file.write("Аня обіцяє вчитись!\n")         # w - режим

# r - режим читання (файл вже існує)
# w - запис, кщо файл вже існує то файл перезаписується
# a - додае контент в кінець вміст не стирається
# x - створює новий файл але якщо вже такий є то буде помилка

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популрна мова програмування. \n")
        file.write("Python - використовується для роботи з даними. \n")
        file.write("Файли дозволяють зберігати інфорацію. \n")
        file.write("Python - вимагає практики. \n")
        file.write("Сьогодні ми працюємо з текствими файлами. \n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivsnenko Anna;91 \n")
        file.write("Leshchenko Ivan;76 \n")
        file.write("Komarova Sophie;97 \n")
        file.write("Bondarenko Illya;84 \n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11 \n")
        file.write("Anna;Math;10 \n")
        file.write("Ivan;Python;6 \n")
        file.write("Ivan;Math;5 \n")
        file.write("Sophie;Python;12 \n")
        file.write("Sophie;Math;9 \n")
        file.write("Illya;Python;9 \n")
        file.write("Illya;Math;8 \n")



with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(text)

# with - автоматично закриває файл після закінчення роботи
# file - можна назвати як хочеш
# text.txt - шлях файла який ми відкриваємо

with open('log.txt', 'w', encoding="utf-8") as file:
    file.write("Перший запуск\n") #\n - перехід на новий рядок
with open('log.txt', 'w', encoding="utf-8") as file:
    file.write("Другий запуск, перший видалено\n")
with open('log.txt', 'a', encoding="utf-8") as file:
    file.write("Новий запис, доаєо у кінець\n")
with open('log.txt', 'r', encoding="utf-8") as file:
    print(file.read())

#способи читання
with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(f'read -> {type(text)}, count -> {len(text)}')

with open('text.txt', 'r', encoding="utf-8") as file:
    line1 = file.readline() #read_line - наступний рядок
    line2 = file.readline() #readlines - створюється новий із тих що ще не прописані
    other_lines = file.readlines()
print(line1)
print(line2)
print(other_lines)

with open('text.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
print(other_lines)
print(other_lines[0] if lines else '')

#перебір файла

with open('text.txt', 'r', encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f'number -> {number}, clean_line -> {clean_line}')


# розпакування

line = "Ivanenko Anna;91 \n"
clean_line = line.strip()
name, score = clean_line.split(';')
print(f'name-> {name}, score-> {score}')


numbers = []
with open('numbers.txt', 'r', encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))
print(f'numbers-> {numbers}')

students = []
with open('students.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(';')
        students.append([name, int(score)])
print(f'students -> {students}')


#CSV
grades = []
with open('grades.csv', 'r', encoding="utf-8") as file:
    for line in file:
        name, subject, score = line.strip().split(';')
        grades.append([name,subject, int(score)])