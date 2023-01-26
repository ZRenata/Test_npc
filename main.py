import requests
from write_func import write_doc
from date_input_func import date_input

BASE_URL = 'https://www.nbrb.by/api/exrates/rates'
ans = 'y'
while(ans == 'y'):
    print('Введите дату в формате ГГГГ-М-Д (если нажать enter или ввести некорректное значение,'
          'то выведет курс на сегодняшний день):')
    date = date_input()
    flag = 1
    while (flag):
        data = requests.get(f"{BASE_URL}?ondate={date}&periodicity=0")
        answer = data.json()
        if len(answer) == 0:
            print('Курс валют на данную дату неизвестен. Введите новую дату:')
            date = date_input()
        else:
            flag = 0
    if write_doc(date, answer):
        print("Файл успешно сохранен!")
    else:
        print("Файл не удалось сохранить")
    key = True
    while(key):
        print('Желаете узнать курс валют за другую дату? y/n')
        ans = input()
        if (ans == 'n' or ans == 'N'):
            quit()
        elif (ans == 'y' or ans == 'Y'):
            ans = 'y'
            key = False
        else:
            print('Неверное значение ответа. Попробуйте снова.')