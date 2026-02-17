# Задача следующего уровня: Напиши функцию validate_users(users), которая принимает список пользователей и возвращает кортеж из двух элементов:
# Список валидных пользователей
# Список ошибок для невалидных пользователей
# Требования к валидному пользователю:
# Должен быть словарем
# Должен содержать ключи: id (int), username (str), email (str)
# id должен быть положительным числом
# username должен быть непустой строкой без пробелов
# email должен содержать символ @ и точку после @
# Формат ошибки:
# Для каждого невалидного пользователя верни строку с описанием ошибки в формате:
# "User [id] invalid: [error_description]"
# Если id отсутствует или невалиден, используй "N/A" вместо id.
# Пример:
# users = [
#     {"id": 1, "username": "john", "email": "john@example.com"},
#     {"id": -1, "username": "jane", "email": "jane@example.com"},
#     {"id": 2, "username": "", "email": "bob@example.com"},
#     {"id": 3, "username": "alice", "email": "invalid-email"},
#     "not_a_dict",
#     {"id": 4, "username": "test", "email": "test@example.com"}
# ]
#
# result = validate_users(users)
# Ожидаемый результат:
# (
#     [
#         {"id": 1, "username": "john", "email": "john@example.com"},
#         {"id": 4, "username": "test", "email": "test@example.com"}
#     ],
#     [
#         "User -1 invalid: invalid id",
#         "User 2 invalid: invalid username",
#         "User 3 invalid: invalid email",
#         "User N/A invalid: not a dictionary"
#     ]
# )
from IPython.lib.pretty import pprint
import re
from operator import itemgetter


EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$')


def validate_users(users) -> ():
    getter = itemgetter('id', 'username', 'email')
    result = ([], [])

    u_s = "User"
    i_s = "invalid"
    for user in users:
        if not (isinstance(user, dict)):
            result[1].append(f"{u_s} {id} {i_s}: not a dictionary")
            continue

        try:
            id, username, email = getter(user)

            if id is None or not (isinstance(id, int)) or id <= 0:
                result[1].append(f"{u_s} {id} {i_s}: invalid id")
                continue

            if username is None or not (isinstance(username, str)) or (username.find(" ") >= 0):
                result[1].append(f"{u_s} {id} {i_s}: invalid username")
                continue

            if email is None or not (re.match(EMAIL_PATTERN, email)):
                result[1].append(f"{u_s} {id} {i_s}: invalid email")
                continue

            result[0].append(user)
        except KeyError:
            result[1].append(f"Key error")
            continue

    return result


pprint(validate_users(
    [
        {"id": 1, "username": "john", "email": "john@example.com"},
        {"id": -1, "username": "jane", "email": "jane@example.com"},
        {"id": 2, "username": "", "email": "bob@example.com"},
        {"id": 3, "username": "alice", "email": "invalid-email"},
        "not_a_dict",
        {"id": 4, "username": "test", "email": "test@example.com"},
        {"id": 5, "username": "te st", "email": "test@example.com"},
        {"id": 6, "username": " test", "email": "test@example.com"},
        {"id": 7, "username": "test", "email": "user@domain..com"}
    ]
))
