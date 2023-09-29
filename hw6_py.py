#� Решить задачи, которые не успели решить на семинаре.

def data_tabs(i, ln, lk):
        j= 2
        for k in range (ln, lk):
            data_tabs = str(k)+"x"+str(i)+"="+str(k*i)
            j += 1
            yield data_tabs 

count_lines = 9
count_columns = 9
print("\n\n       ТАБЛИЦА УМНОЖЕНИЯ  \n")
start_columns, end_columns = 2, int(0.5*count_columns )+2
[print(*data_tabs(i, start_columns, end_columns), sep='\t') for i in range(2, count_lines+1)]
print()
start_columns, end_columns = int(0.5*count_columns )+2, count_columns+1
[print(*data_tabs(i, start_columns, end_columns), sep='\t') for i in range(2, count_lines+1)]
print()

# � В модуль с проверкой даты добавьте возможность запуска 
# в терминале с передачей даты на проверку.

from sys import argv

def control_date(current_date):
    day, month, year = current_date.split('.') 
    day, month, year = int(day), int(month), int(year)
    #print(current_date, day, month, year)
    if 32 <= day or 13 <= month or month <= 0:
        print('дата введена не корректно')
        return False
    print('дата введена корректно') 
    return True

#python3 hw6_py.py 21.01.2023
current_date = input("введите дату: ")
print(argv)
print(control_date(current_date))   

# � Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def see_chessboard_field(chessboard_field, n):
    print("\n\n           ШАХМАТНОЕ ПОЛЕ  \n")
    [print(*data_tabs(i,chessboard_field, n), sep='\t') for i in range(n)]
    return

def killing_field( j_queen_point, i_queen_point, chessboard_field, n):
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

list_place_queens = [[0,0],[4,3],[2,5],[4,5],
              [6,6],[5,0],[0,5],[6,6]]

n = 8    # размерность квадратной матрицы       
cahessboard_field = [0] * n
chessboard_field = [[True] * n for i in range(n)]

for l in range (len(list_place_queens)): 
    i, j = list_place_queens[l]
    if chessboard_field[i][j] == None:
        print(i,j,'бьется предыдущими ферзями')
        break  
    chessboard_field = killing_field(i, j, chessboard_field, n)
    see_chessboard_field(chessboard_field, n)    
