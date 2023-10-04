# ПРОШЛЫЙ ДОЛЖОК

# � Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# печать шахматного поля
def see_chessboard_field(chessboard_field, n):
    print("\n\n           ШАХМАТНОЕ ПОЛЕ  \n")
    [print(*data_tabs(i,chessboard_field, n), sep='\t') for i in range(n)]
    return

# заполнение побитого поля 
def killing_field( i_queen_point,j_queen_point, chessboard_field, n):
    sum = j_queen_point +i_queen_point
    for m in range(n):
        chessboard_field [i_queen_point][m] = False
        chessboard_field [m][j_queen_point] = False
        
        if 0<=i_queen_point+1+m <=n-1 and 0<=j_queen_point+1+m <=n-1 :
            chessboard_field [i_queen_point+1+m][j_queen_point+1+m] = False
        
        if 0<=i_queen_point-1-m <=n+1 and 0<=j_queen_point-1-m <=n+1 :
            chessboard_field [i_queen_point-1-m][j_queen_point-1-m] = False

        if 0<= sum - m <=n-1 :
            chessboard_field [m][sum - m] = False

    #see_chessboard_field(chessboard_field, n)
    chessboard_field [i_queen_point][j_queen_point] = None
    return chessboard_field

# символы отображения поля
def data_tabs(i,chessboard_field, n):
        j= 0
        for k in range (n):
            if chessboard_field[i][k]:
                data_tabs = str(i+1) + ',' + str(k+1)
            elif chessboard_field[i][k] == None:
                data_tabs = '♕'
            else:
                data_tabs = '.'
            j += 1
            yield data_tabs 

def mutual_defeat(list_place_queens):
    
    n = 8    # размерность квадратной матрицы       
    chessboard_field = [[True] * n for i in range(n)]
    rez = True
    for l in range (len(list_place_queens)): 
        i, j = list_place_queens[l]
        if chessboard_field[i][j] == False:
            print(f'положение [{i}.{j}] бьется предыдущими ферзями')
            rez = False
            break
        chessboard_field = killing_field(i, j, chessboard_field, n)
        see_chessboard_field(chessboard_field, n)  
    print("значение функции результата:   ", rez)
    return rez

# положение ферзей
import random as rnd

ist_size = 8
list_place_queens = [0] * ist_size
for i in range(ist_size): 
    list_place_queens[i] = [0] * 2
 
for i in range(8):
    list_place_queens [i][0] = rnd.randint(0,ist_size-1)
    list_place_queens [i][1] = rnd.randint(0,ist_size-1)  
print(f'\nрасстановка ферзей:\n{list_place_queens}\n')

if mutual_defeat(list_place_queens): 
    print("ферзи не бьют друг друга")
else:
    print("имеются пары ферзей бьющие друг друга\n")

# 2. Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов name_file. 
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере number_digits.
# принимать параметр расширение исходного файла. 

import os

def rename_file(old_name_file, name_file, extension_file, number_digits ):
    #new_name_file = []
    for ind in range(len(old_name_file)):
        if len(old_name_file) >= number_digits * 10:
            print("количество файлов больше допустимого значения")
            break  
        new_name = name_file + '_'+ str(ind) + '.' + extension_file
        #old_name = old_name_file [ind].split('.')
        print(f'старое имя файла: {old_name_file [ind]},  новое имя файла: {new_name}')
        os.rename(old_name_file [ind], new_name)

name_file = 'required'
extension_file = 'jpeg'
number_digits = 4
old_name_file = ['hw7_fgfgfpy.py', 'dfgh.rty', 'hjgd,hhh', 'dfg,we']

rename_file(old_name_file, name_file, extension_file, number_digits)

# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 
# из исходного имени файла. К ним прибавляется желаемое конечное имя, 
# если оно передано. Далее счётчик файлов и расширение. 

import os

def rename_file(old_name_file, name_file, extension_file, number_digits, pos1, pos2 ):
    #new_name_file = []
    for ind in range(len(old_name_file)):
        if len(old_name_file) >= number_digits * 10:
            print("количество файлов больше допустимого значения")
            break  
        old_name_list = old_name_file [ind].split('.')
        old_name = old_name_list [0]
        current_name = ''
        for position in range(pos1 - 1, pos2):
            if position >= len(old_name):
                break
            current_name += old_name[position]     
        new_name = current_name + '_' + name_file + '_' + str(ind) + '.' + extension_file
        
        print(f'старое имя файла: {old_name_file [ind]},  новое имя файла: {new_name}')
        os.rename(old_name_file [ind], new_name)

name_file = 'required'
extension_file = 'jpeg'
number_digits = 4
pos1, pos2 = 3, 6
old_name_file = ['hghghgw7_py.py', 'dfgweerh.rty', 'hhgsyrtfdxjgd.hhh', 'dertyuijhfg.we']

rename_file(old_name_file, name_file, extension_file, number_digits, pos1, pos2)
