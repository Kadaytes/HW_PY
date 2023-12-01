"""
программа банкомат:
1. Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

class Atm():

    """ Установки Банкомата
    """
    _START_SUM = 0.00
    _MULTIPLICITY_RUR = 50.00
    _MIN_WITHDRAWAL_COMMISSION_RUR = 30.00
    _MAX_WITHDRAWAL_COMMISSION_RUR = 600.00
    _WEALTH_RUR = 5_000_000.00

    _MAXIMUM_MENU_ITEMS = 4 
    _START_COUNT = 0
    _REMUNERATION_COUNT = 3

    _WITHDRAWAL_COMMISSION_PERCENT = 0.015
    _REMUNERATION_PERCENT = 0.03
    _WEALTH_PERCENT = 0.1

    def __init__(self):
     
     """ Переменные клиента        
     """
     self._balance = 0
     self._count_operation = 1
     self._operation_code = 0
     self._max_operation_code = 4
     self._money = 0
     self._name = 'user'

""" вывод суммы остатка
"""
def show_balance():
    print(f'Ваш балланс {client._balance}  y.e')
    logging.info(f'{datetime. now()}, код опирации {client._operation_code}, внесенные/снятые средства {client._money}, итоговый балланс {client._balance}')
    
""" вывод средств
"""
def money_input():  
    try:
        money = int(input("введите сумму кратную 50 у.е :    "))
        if money < 0: 
                money  = - money 
        return money    
    except ValueError as e:
        print(f'ошибка <{e}> \n=== не корректный ввод, попробуйте еще раз, число должно быть целым ===')  
        money = 0
        return money 
""" пополнение 
"""
def top_up_money(): 
    print('>>>  для внесения')   
    money = money_input()
    client._money = money
    if money % Atm._MULTIPLICITY_RUR == 0 :
        print (f"Внесена сумма {money} у.е \n ")
        client._balance = client._balance + money
# начисление налога на богатство
        if  client._balance >= Atm._WEALTH_RUR:
            wealth_tax = int(client._balance * Atm._WEALTH_PERCENT)
            print(f"на сумму балланса начислен налог на богатство в размере {wealth_tax} у.е")
            logging.info(f"на сумму балланса начислен налог на богатство в размере {wealth_tax} у.е")
            client._balance = client._balance - wealth_tax 
    else:
        print("Средства не внесены")
        logging.info("Средства не внесены")
    
    show_balance()
    return 

""" снятие
"""  
def withdraw_money():
    print('>>>  для снятия')   
    money = money_input()
    client._money = money

# начисление сервисного сбора
    service_charge = int(money * Atm._WITHDRAWAL_COMMISSION_PERCENT)
    new_balance = client._balance - money - service_charge 
   
    #print(money, Atm._MULTIPLICITY_RUR,Atm._MIN_WITHDRAWAL_COMMISSION_RUR, service_charge, Atm._MAX_WITHDRAWAL_COMMISSION_RUR, new_balance)
    if money %  Atm._MULTIPLICITY_RUR == 0 and Atm._MIN_WITHDRAWAL_COMMISSION_RUR <= service_charge <= Atm._MAX_WITHDRAWAL_COMMISSION_RUR and new_balance >= 0 :
        print (f"Снята сумма {money} у.е \n ")
        print(f"с суммы {money} удержан сбор за снятие в размере {service_charge} у.е")
        logging.info(f"с суммы {money} удержан сбор за снятие в размере {service_charge} у.е")
        client._balance = new_balance 
    else:
        print("снятие средств не возможно")
        logging.info("снятие средств не возможно")

    show_balance()
    return 

""" периодическое начисление комиссии  
"""     
def count_operation():
    client._count_operation += 1
    if client._count_operation % Atm._REMUNERATION_COUNT == 0: 
        client._balance = int(client._balance* (1 - Atm._REMUNERATION_PERCENT))
        print(f"на сумму балланса начислены -3% {-int(client._balance * Atm._REMUNERATION_PERCENT )} у.е")
        logging.info(f"на сумму балланса начислены -3% {-int(client._balance * Atm._REMUNERATION_PERCENT )} у.е")
        show_balance()
    return

""" управление движением
"""
def named_atm(namе):   

    client._name = namе
    logging.basicConfig(level=logging.INFO, filename="m_atm_history.log",filemode="w")
    print(f'\n\n>>>>> счет клиента {client._name}   >>>>> ')
    print(datetime. now())
    logging.info(f'клиент {client._name}')
    work = True   
    while work:  
        print("\n",
        "====================================== \n",
        "введите код опирации Ваших действий: \n",
        "1 - узнать балланс \n",
        "2 - пополнить \n",
        "3 - снять \n",
        "4 - выйти \n",
        "====================================== ")
        try:
            operation_code = int(input())
            if operation_code < 0: 
                operation_code = - operation_code
            if operation_code > client._max_operation_code:
                operation_code = 0
        except ValueError as e:
            print(f'ошибка <{e}> \n=== не корректный ввод, попробуйте еще раз, число должно быть целым ===')  
            operation_code = 0
        client._operation_code = operation_code
        match operation_code :
            case 1: show_balance()
            case 2: top_up_money()   
            case 3: withdraw_money()
            case 4: work = False; show_balance()
        count_operation()
    return

""" основная
"""
import logging
from datetime import datetime
# from sys import argv

client = Atm()
client._name = 'Petrov_Ivan_Sidorovich_192837465'
# для вызова из строки :
# python3 main.py 'Petrov_Ivan_Sidorovich_192837465'
# client._name = argv[1]

named_atm(client._name)
