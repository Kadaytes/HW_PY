# 1. Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

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
    
    show_balance(_balance)
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
 
    show_balance(_balance)
    return _balance

# исходное состояние
balance = 0
count_operation = 1

# управление движением
work = True   
while work:  
    print("\n ========== \n введите код опирации Ваших действий: \n",
#   "1 - узнать балланс \n",
    "2 - пополнить \n",
    "3 - снять \n",
    "4 - выйти \n ========== ")
    operation_code = int(input())
    match operation_code :
 #      case 1: show_balance(balance)
        case 2: balance = top_up_money(balance, count_operation)   
        case 3: balance = withdraw_money(balance, count_operation)
        case 4: work = False

 # периодическое начисление комиссии       
    count_operation += 1
    if count_operation % 3 == 0: 
        balance = int(balance * 0.97)
        print(f"на сумму балланса {balance} начислены -3% {-int(balance * 0.03)} у.е")
        show_balance(balance)


# 2. Напишите программу, которая получает целое число и возвращает
#  его шестнадцатеричное строковое представление.
#  Функцию hex используйте для проверки своего результата.

number = int(input("введите целое число   "))
notation = 16
print(f"перевод числа {number} из десятичной системеы в {notation}-ричную систему")
print("функция hex() дает значения", hex(number )) 

representation = ""
#representation = []
new_number = number 
count = 1
while count > 0 :
    rest = new_number % notation
    match rest :
        case 0: lit ='0'
        case 1: lit ='1'
        case 2: lit ='2'
        case 3: lit ='3'
        case 4: lit ='4'
        case 5: lit ='5'
        case 6: lit ='6'
        case 7: lit ='7'
        case 8: lit ='8'
        case 9: lit ='9'
        case 10: lit ='a'
        case 11: lit ='b'
        case 12: lit ='c'
        case 13: lit ='d'
        case 14: lit ='e'
        case 15: lit ='f'
    
    #representation.append(lit)
    representation = lit + representation
    new_number =  new_number // notation 
    count = new_number 
representation = '0x'+ representation
#representation = '0x'+"".join(reversed(representation))
print("найденное значение :  ", representation) 


# 3. Напишите программу, которая принимает две строки вида “a/b” 
# - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

str1 = input(" введите первую дробь в виде а/в : ")
a, b = map(float, str1.split('/'))
str2 = input(" введите первую дробь в виде а/в : ")
c, d = map(float, str2.split('/'))
multy = a * c / (b * d)
sum = (a * d + b * c) / (b * d)
print(str, a, b, c, d, multy, sum)

control_multy = float(Fraction(str1) * Fraction(str2))
control_sum = float(Fraction(str1) + Fraction(str2))
print(str, a, b, c, d, multy, sum, control_multy, control_sum )

