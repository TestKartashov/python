# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue_txt = input('Enter revenue: ')

cost_txt = input('Enter сost: ')

try:
    revenue = float(revenue_txt)
    cost = float(cost_txt)
except:
    print('Неверное значение')


# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
if revenue == cost:
    print("The company worked without loss and without profit")
elif revenue > cost:
    print("The company worked with a profit")
else:
    print("The firm worked at a loss")

# вычислите рентабельность выручки (соотношение прибыли к выручке).
if revenue > cost:
    profit = revenue - cost
    profitability = float(profit / revenue)

    print(f'Profitability %.2f' % profitability)

    # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
    count_people_txt = input('Enter number of employees of the company: ')
    if not count_people_txt.isdigit() or int(count_people_txt)<0:
        print('Неверное значение')


    # определите прибыль фирмы в расчете на одного сотрудника
    prof_emp = profit / int(count_people_txt)

    print(f"Firm's profit per employee {prof_emp}")
