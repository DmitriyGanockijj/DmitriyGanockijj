char = input('Введите символ: ')
print (char)
print (char + char)
print (char + char + char)
print (char + char + char + char)
print (char + char + char + char + char)

month_name = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'
              }

month_number = int(input ('Введите номер месяца: '))
print (month_name.get(month_number))