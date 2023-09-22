# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def tuple_elements(file_path):
    *path_file, name_file = file_path.split('/')
    name_file, type_file = name_file.split('.')
    return (path_file, name_file, type_file)

file_path = "Users/kadaytes/study/python/hw5_py.py"
print(f"\nабсолютный путь до файла \n{file_path}\n")
print(f"кортеж из трёх элементов: путь, имя файла, расширение файла\n{tuple_elements(file_path)}\n")

# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

list_names = ['1', 'a', 'ew']
list_rates = [10, 14, 11]
list_pst = ['10.25%','14.5%', '9.34%']

dict_new = {list_names[i] : float(list_pst[i].translate({ord('%') : None})) * 0.01 * float(list_rates[i]) for i in range(len(list_names))}
print(dict_new)    

#✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# генератор положительных чисел последовательности Фибоначчи
def fibonacci(n):
        first, second = 0, 1
        fibonacci_num = 0
        for _ in range(n):
            fibonacci_num, second = first + second, first
            first = fibonacci_num
        yield fibonacci_num

# введем длину выводимой последовательности Фибоначчи
set_number = (input("введите количество чисел последовательности Фибоначчи:   "))
while not set_number.isdigit():
    set_number = (input("введите еще раз целое число:   "))
set_number =  int(set_number)

# вывод последовательно чисел последовательности Фибоначчи
for i in range(1, set_number+1):
    print(next(fibonacci(i)))

