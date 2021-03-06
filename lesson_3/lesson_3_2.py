# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Вариант с **kwargs (универсальная функция)

def data_string(**kwargs):
    """Принимает параметры как именованные аргументы и возвращает данные одной строкой"""
    result = [f'{key}: {value}' for key, value in kwargs.items()]
    return ', '.join(result)


# Вариант с параметрами, имеющими значения по умолчанию:
def user_data(name='неизвестно', surname='неизвестно', birth_year='неизвестно', city='неизвестно', e_mail='неизвестно',
              phone='неизвестно'):
    """Принимает параметры как позиционные и/или именованные аргументы и
    возвращает данные о пользователе одной строкой"""
    return f'Имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город проживания: {city}, e-mail: {e_mail},' \
           f' телефон: {phone} '


print(data_string(name='Елена', surname='Максимова', birth_year='1986', city='Москва',
                  e_mail='неизвестно', phone='+7 999 999-99-99'))

print(user_data('Елена', 'Максимова', '1986', 'Москва', phone='+7 999 999-99-99'))
