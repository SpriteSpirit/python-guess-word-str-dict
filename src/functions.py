import json

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Словарь с уровнями сложности и их ключами в файле
DIFFICULTY_LEVELS = {
    "легкий": "words_easy",
    "средний": "words_medium",
    "сложный": "words_hard",
}

WORDS_FILE = 'words.json'

answers = {}


def get_dict_words(difficult: str) -> dict:
    """
    Читает словарь из файла words.json.
    :param difficult: Уровень сложности в виде строки
    :return: Возвращает выбранный словарь из файла
    """
    with open(WORDS_FILE, 'r', encoding='utf-8') as file:
        dict_words = json.load(file)

    return dict_words[difficult]


def role(text: str = "", members: int = 2) -> None or str:
    """
    Возвращает ответ пользователя, если подразумевается ответ пользователя
    """

    progr = "Программа:"
    user = "Пользователь:"

    if members == 1:
        print(f"{progr} {text} ")
    elif members == 2:
        print(f"{progr} {text} ")
        user = input(f"{user} ")

        return user
