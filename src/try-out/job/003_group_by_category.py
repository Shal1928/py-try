# Отлично! Рад, что помог. Двигаемся дальше.
#
# **Задача следующего уровня:** Напиши функцию `group_by_category(products)`, которая принимает список словарей товаров
# и возвращает словарь, сгруппированный по категориям.
#
# **Структура товара:**
# ```python
# {
#     "id": 1,
#     "name": "Product Name",
#     "category": "Category Name",
#     "price": 100.0
# }
# ```
#
# **Требования:**
# 1. Функция должна возвращать словарь, где:
#    - **Ключи** - названия категорий
#    - **Значения** - списки товаров этой категории
# 2. Если товар без категории (None или пустая строка), поместить его в категорию `"Uncategorized"`
# 3. Сохранять оригинальный порядок товаров within каждой категории
#
# **Пример:**
# ```python
# products = [
#     {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1000},
#     {"id": 2, "name": "Book", "category": "", "price": 20},
#     {"id": 3, "name": "Phone", "category": "Electronics", "price": 500},
#     {"id": 4, "name": "Pen", "category": None, "price": 2}
# ]
#
# result = group_by_category(products)
# ```
#
# **Ожидаемый результат:**
# ```python
# {
#     "Electronics": [
#         {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1000},
#         {"id": 3, "name": "Phone", "category": "Electronics", "price": 500}
#     ],
#     "Uncategorized": [
#         {"id": 2, "name": "Book", "category": "", "price": 20},
#         {"id": 4, "name": "Pen", "category": None, "price": 2}
#     ]
# }
# ```

# if category is None or category is '':
#     result["Uncategorized"].append(product)
# else:
#     current = result.get(category)
#     if current is None:
#         result[category] = [product]
#     else:
#         current.append(product)
from collections import defaultdict


def group_by_category(products) -> dict:
    result = defaultdict(list)

    for product in products:
        category = product.get("category")
        if not category:
            result["Uncategorized"].append(product)
        else:
            result[category].append(product)

    return dict(result)


print(group_by_category(
    [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1000},
        {"id": 2, "name": "Book", "category": "", "price": 20},
        {"id": 3, "name": "Phone", "category": "Electronics", "price": 500},
        {"id": 4, "name": "Pen", "category": None, "price": 2}
    ]
))
