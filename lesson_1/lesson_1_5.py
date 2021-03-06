# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input('Введите выручку в рублях: '))
expenses = float(input('Введите издержки в рублях: '))

if revenue == expenses:
    print('Выручка равна издержкам. Вы ходите по тонкому льду!')
elif revenue < expenses:
    print('Плохие новости: издержки больше выручки, ваша фирма скоро обанкротится!')
else:
    profit = revenue - expenses
    print(f'Прибыль составляет: {profit:.2f} руб. Коэффициент рентабельности составил {profit / revenue:.2f}')
    staff_count = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет {profit / staff_count:.2f} руб.')


