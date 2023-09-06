
# # Дан список повторяющихся элементов. 
# # Вернуть список с дублирующимися элементами. 
# # В результирующем списке не должно быть дубликатов.

given_list = ['d', 'd', 's', '1', '1', '1', '1', '3', 'f', 'F', 'f']
print("список повторяющихся элементов\n", given_list)

new_list = given_list
list =[]
while len(new_list) > 0:
    st = new_list[0]
    k = new_list.count(st)
    if k != 1: list.append(st)
    for _ in range(k):
        new_list.remove(st)
print("список с дублирующимися элементами без дубликатов\n", list)

# В большой текстовой строке подсчитать количество встречаемых слов
#  и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации 
# к языку.

original_text = "Python 3.0 ( называемый также « Python 3000 » или « Py3K ») разрабатывался с целью устранения фундаментальных изъянов в языке . Эти изменения не могли быть сделаны при условии сохранения полной обратной совместимости с 2.x версией , поэтому потребовалось изменение главного номера версии . Ведущим принципом разработки Python 3 было : « уменьшение дублирующейся функциональности устранением устаревших способов сделать это» ."
# trans_table = str.maketrans({'о': 'и', 'л': 'к', '—': None})
# original_text = original_text.translate(trans_table)
list = original_text.split(" ")
# print(list)
count_word = [] 
for i in range(len(list)):
    count_word.append(list.count(list[i]))
max_count = max(count_word)
print(" максимальное повторение слова: ", max_count)
# print(count_word)


# Создайте словарь со списком вещей для похода 
# в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав 
# его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

things = { "things 1" : 1.4 , "things 2": 1.6, "things 3": 3.0,
           "things 4" : 10.1 , "things 5": 12.5, "things 6": 20.5 }
maximum_weight = float(input("введите максимальную грузоподъёмность :\n"))   

my_list_values = list(dict.values(things))
my_list_key= list(dict.keys(things))

# print(my_list_values)
# print(my_list_key)

print("спикок вещей которые влезут в рюкзак при ограничении веса")
for i in range(len(things)-1, -1, -1):
   sum_weight = sum(my_list_values) 
   if sum_weight <= maximum_weight :
    print(my_list_key)
   my_list_values.pop()
   my_list_key.pop()
