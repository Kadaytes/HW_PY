# Напишите функцию для транспонирования матрицы

def transposed_matrix (matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
    return transposed

matrix = [[1, 2],[3, 4],[5,6],[7,8]]
print(f'исходная матрица\n{matrix} \nтранспонированная матрица\n{transposed_matrix (matrix)}\n')


# Напишите функцию принимающую на вход только ключевые параметры 
# и возвращающую словарь, где ключ — значение переданного 
# аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

def adding_to_dictionary(my_list_key):    
    my_dictionary = {}
    for i in my_list_key:
        if isint(i) : 
            my_dictionary[hex(i)] = i
        else: 
            my_dictionary[i] = i
    return my_dictionary

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False    
    
my_list_key = ['a','b', 2023]
print(f"список входных ключевых параметров\n{my_list_key}")
print(f"сформированный словарь\n {adding_to_dictionary(my_list_key)}")


# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств
# в список. 

# вывод суммы остатка
def show_balance(_balance):
    print(f'Ваш балланс {_balance}  y.e')

# пополнение 
def top_up_money(_balance, count_operation):
    money = int(input("Внесите сумму кратную 50 у.е :    "))
    if money % 50 == 0 :
        print (f"Внесена сумма {money} у.е \n ")
        _balance = _balance + money
 
# начисление налога на богатство
        if  _balance >= 5000000:
            wealth_tax = int(_balance * 0.1)
            print(f"на суммы {_balance} начислен налог на богатство в размере {wealth_tax} у.е")
            _balance = _balance - wealth_tax 
    else:
        print("Средства не внесены")
    return _balance

# снятие  
def withdraw_money(_balance, count_operation):
    money = int(input("Введите сумму для снятия кратную 50 у.е :    "))
# начисление сервисного сбора
    service_charge = int(money * 0.15)
    new_balance = _balance - money - service_charge 
    if money % 50 == 0 and 30 <= service_charge <= 600 and new_balance >= 0 :
        print (f"Снята сумма {money} у.е \n ")
        print(f"с суммы {money} удержан сбор за снятие в размере {service_charge} у.е")
        _balance = new_balance 
    else:
        print("снятие средств не возможно")
    return _balance

# исходное состояние
import datetime
balance = 0
count_operation = 0
list_history = []

# управление движением
work = True   
while work:  
    print("\n ========== \n введите код опирации Ваших действий: \n",
    "1 - узнать балланс \n",
    "2 - пополнить \n",
    "3 - снять \n",
    "4 - история пополнения - снятия\n",
    "5 - выйти \n ========== ")
    operation_code = int(input())
    current_date = datetime.datetime.today().isoformat(sep='*')
    print(current_date)
    match operation_code :
        case 1: 
           show_balance(balance)
        case 2:
            list_history.append(current_date)
            new_balance = top_up_money(balance, count_operation)
            list_history.append(new_balance - balance)
            balance = new_balance
            list_history.append(balance)
            show_balance(balance)
        case 3: 
            list_history.append(current_date)
            new_balance = withdraw_money(balance, count_operation)
            list_history.append(new_balance - balance)
            balance = new_balance
            list_history.append(balance)
            show_balance(balance)
        case 4:
            print(f'история движения по счету банкомата\n"дата", "средства", "баланс"\n{list_history}')
        case 5: 
            work = False

 # периодическое начисление комиссии       
    count_operation += 1
    if count_operation % 3 == 0: 
        new_balance = int(balance * 0.97)
        print(f"на сумму балланса начислены -3% в размере {balance-new_balance} у.е")
        list_history.append(current_date)
        list_history.append(new_balance - balance)
        balance = new_balance
        list_history.append(balance)
        balance = new_balance
        show_balance(balance)