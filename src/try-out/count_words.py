# Задача следующего уровня: Напиши функцию count_words(sentence), которая принимает строку и возвращает словарь,
# где ключи — это уникальные слова в строке, а значения — сколько раз каждое слово встретилось.
#
# Условия:
#
# Считай слова независимо от регистра (т.е. "Hello" и "hello" — это одно и то же слово).
#
# Знаки препинания в начале и конце слов нужно удалить (например, "hello," должно стать "hello").
#
# Пример:
#
# python
# count_words("Hello world, hello Python! Hello again.")
# Должно вернуть:
# {'hello': 3, 'world': 1, 'python': 1, 'again': 1}
#
# Жду твоего решения!
import string


import string
from collections import Counter


def count_words(sentence) -> dict:
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.lower().split()
    cleaned_words = [word.translate(translator) for word in words if word.translate(translator)]
    return dict(Counter(cleaned_words))


print(count_words('Hello world, hello Python! Hello again.'))
