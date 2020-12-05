# todo Реализовать функцию, принимающую несколько параметров, описывающих
# todo данные пользователя: имя, фамилия, год рождения, город проживания,
# todo email, телефон. Функция должна принимать параметры как именованные аргументы.
# todo Реализовать вывод данных о пользователе одной строкой.

def print_data_user(**kwargs):
    return F"{kwargs.get('first_name')} " \
           F"{kwargs.get('last_name')} " \
           F"{kwargs.get('year')} " \
           F"{kwargs.get('city_live')} " \
           F"{kwargs.get('email')} " \
           F"{kwargs.get('phone')}"


user = {'first_name': "Alex",
        'last_name': "Kart",
        'year': 1922,
        'city_live': "Moscow",
        'email': "m@ya.ru",
        'phone': "7(999)123321123"}

print(print_data_user(**user))
