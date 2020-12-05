# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_data_user(**kwargs):
    return F"{kwargs['first_name']} " \
           F"{kwargs['last_name']} " \
           F"{kwargs['year']} " \
           F"{kwargs['city_live']} " \
           F"{kwargs['email']} " \
           F"{kwargs['phone']}"


print(print_data_user(first_name="Alex",
                      last_name="Kart",
                      year=1922,
                      city_live="Moscow",
                      email="m@ya.ru",
                      phone="7(999)123321123"))
