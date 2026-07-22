from datetime import datetime
try :
     transactions = []
     
     with open ("transactions.txt", "r", encoding = "utf-8") as file:
          for line in file :
               parts = line.strip().split(";")
               if (len(parts) >= 5) :
                    try :
                         parts[1] = float(parts[1])
                    except ValueError :
                         continue
                    transactions.append(parts)
except FileNotFoundError :
    transactions = []
def save_transactions() :
    with open ("transactions.txt", "w", encoding = "utf-8") as file :
        for transaction in transactions :
             file.write(transaction[0] + ";" +  str(transaction[1]) + ";" + transaction[2] + ";" + transaction[3] + ";" + transaction[4] + "\n")
def get_date() :
     return datetime.now().strftime("%d.%m.%Y")
def add_income() :
     try :
          income = float(input(" Введите ваш заработок: "))
     except ValueError :
          print(" Введите число! ")
          return
     if (income <= 0) :
          print(" Число должно быть положительным! ")
          return
     category = input(" Введите категорию: ")
     comment = input(" Введите комментарий: ")
     transactions.append(["Доход", income, category, comment, get_date()])
     save_transactions()
def add_expense() :
     try :
          expense = float(input("Введите ваши расходы: "))
     except ValueError :
          print("Введите число! ")
          return
     if (expense <= 0) :
          print(" Число должно быть положительным! ")
          return
     category = input(" Введите категорию: ")
     comment = input(" Введите комментарий: ")
     
     transactions.append(["Расход", expense, category, comment, get_date()])
     save_transactions()
def show_transactions() :
    if (len(transactions) < 1) :
        print (" Транзакций пока нет! ")
        return
    for i, transaction in enumerate(transactions) :
        print(i+1,".",transaction[0], "-", transaction[1], "-", transaction[2], "-", transaction[3], "-", transaction[4])
def show_balance() :
    balance = 0
    for transaction in transactions :
        if (transaction[0] == "Доход") :
            balance += transaction[1]
        elif (transaction[0] == "Расход") :
            balance -= transaction[1]
    print (" Ваш баланс:", balance)
def show_total_income() :
    total_income = 0
    for transaction in transactions :
        if (transaction[0] == "Доход") :
            total_income += transaction[1]
    print(" Ваш общий доход:", total_income)
def show_total_expense() :
    total_expense = 0
    for transaction in transactions :
        if (transaction[0] == "Расход") :
            total_expense += transaction[1]
    print(" Ваш общий расход:", total_expense)
def clear_all_transactions() :
   answer = input(" Вы уверены? (да/нет) ")
   if (answer.lower() == "да") :
       transactions.clear()
       print(" Все транзакции удалены! ")
       save_transactions()
   elif (answer.lower() == "нет") :
       return
   else :
       print(" Такой команды нет! ")
def delete_transaction() :
    show_transactions()
    try :
         number = int(input(" Введите номер транзакции, которую вы хотите удалить: "))
    except ValueError :
         print (" Введите целое число! ")
         return
    if (number < 1 or number > len(transactions)) :
        print (" Такой транзакции нет! ")
    else :
        del transactions[number - 1]
        print (" Транзакция успешно удалена! ")
        save_transactions()
def find_transactions() :
    word = input(" Введите слово для поиска:  ")
    found = False
    for transaction in transactions :
        if (word.lower() in transaction[0].lower() or word.lower() in transaction[2].lower() or word.lower() in transaction[3].lower()) :
            found = True
            print (transaction)
    if not found :
        print(" Ничего не найдено! ")
def sort_transactions() :
     print(" 1 - По возрастанию суммы ")
     print(" 2 - По убыванию суммы ")
     try :
          number = int(input(" Введите номер сортировки (1/2) "))
     except ValueError :
          print(" Введите целое число! ")
          return
     if (number == 1) :
          transactions.sort(key = lambda x: x[1])
     elif (number == 2) :
          transactions.sort(key = lambda x: x[1], reverse = True)
     else :
          print(" Такой команды нет! ")
     show_transactions()
     save_transactions()
def show_expense_categories() :
     expenses = {}

     for transaction in transactions :
          if transaction[0] == "Расход" :
               category = transaction[2]
               amount = transaction[1]
               if category not in expenses :
                    expenses[category] = 0
               expenses[category] += amount
     for category in expenses :
          print(category, ":", expenses[category])
     if len(expenses) < 1 :
          print (" Расходов нет! ")
def show_income_categories() :
     incomes = {}

     for transaction in transactions :
          if transaction[0] == "Доход" :
               category = transaction[2]
               amount = transaction[1]
               if category not in incomes :
                    incomes[category] = 0
               incomes[category] += amount
     for category in incomes :
          print(category, ":", incomes[category])
     if len(incomes) < 1 :
          print (" Доходов нет! ")
while True :
    print (" 1 - Добавить доход ")
    print (" 2 - Добавить расход ")
    print (" 3 - Показать все транзакции ")
    print (" 4 - Показать баланс ")
    print (" 5 - Показать общий доход ")
    print (" 6 - Показать общий расход ")
    print (" 7 - Очистить все транзакции ")
    print (" 8 - Удалить транзакцию ")
    print (" 9 - Найти транзакции по слову ")
    print (" 10 - Сортировать транзакции ")
    print (" 11 - Показать расходы по категориям ")
    print (" 12 - Показать доходы по категориям ")
    print (" 13 - Выход ")
    try :
        number = int(input(" Введите число: "))
    except ValueError :
        print (" Введите целое число! ")
        continue
    if (number == 1) :
        add_income()
    elif (number == 2) :
        add_expense()
    elif (number == 3) :
        print ("\n" + "=" * 50)
        show_transactions()
        print ("=" * 50 + "\n")
    elif (number == 4):
        show_balance()
    elif (number == 5) :
        show_total_income()
    elif (number == 6) :
        show_total_expense()
    elif (number == 7) :
        clear_all_transactions()
    elif (number == 8) :
        delete_transaction()
    elif (number == 9) :
        find_transactions()
    elif (number == 10) :
        sort_transactions()
    elif (number == 11) :
        show_expense_categories()
    elif (number == 12) :
        show_income_categories()
    elif (number == 13) :
        print (" Спасибо, что использовали программу! ")
        break
    else :
        print(" Нет такой операции! ")
