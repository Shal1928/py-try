# Новая задача того же уровня: Напиши функцию find_common_words(text1, text2), которая принимает две строки и возвращает множество слов, которые встречаются в обеих строках.
# # Условия:
# # Слова считаются независимо от регистра ("Hello" и "hello" - одно слово)
# # Знаки препинания нужно игнорировать
# # Вернуть множество в нижнем регистре

# find_common_words("Hello world!", "World is amazing")
# Должно вернуть: {'world'}
import string


def find_common_words(text1, text2) -> set:
    translator = str.maketrans('', '', string.punctuation)
    words2 = get_clean_words(text2, translator)
    return set(word for word in get_clean_words(text1, translator) if word in words2)


def get_clean_words(text, translator) -> set:
    words = text.lower().split()
    return {word.translate(translator) for word in words if word.translate(translator)}


print(find_common_words("Hello world!", "World is amazing"))
