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


def get_user_choice_level() -> str:
    """
    Запрашивает у пользователя уровень сложности.
    :return: Возвращает строковое значение ключа
    """
    role("Выберите уровень сложности.", 1)
    user_choice = role(f"{', '.join(DIFFICULTY_LEVELS.keys()).capitalize()}.", 2)

    if isinstance(user_choice, str):
        user_choice = user_choice.strip().lower()

        if user_choice not in DIFFICULTY_LEVELS:
            role("Неверный ввод.", 1)
            role(f"Пожалуйста, введите {', '.join(DIFFICULTY_LEVELS.keys()).title()}.", 1)
            return get_user_choice_level()
        else:
            role(f"Выбран {user_choice} уровень сложности, мы предложим 5 слов, подберите перевод.", 1)
            return DIFFICULTY_LEVELS[user_choice]


def press_enter() -> None:
    """
    Запрашивает у пользователя нажать Enter
    """
    role("Нажмите Enter для продолжения.", 2)


def clear_answer(answer: str) -> None:
    """
    Очищает ответ пользователя от символов . , !
    """
    clean_answer = answer.replace('.','').replace('!','').replace(',','')
    return clean_answer.strip().lower()


def total_score(answers: dict) -> int:
    """
    Считает сумму все верных ответов
    """
    score = sum([1 for answer in answers.values() if answer])

    return score


def quiz() -> None:
    """
    Основная функция игры
    """
    words = get_dict_words(get_user_choice_level())
    print(words)

    for word, translate in words.items():
        user_answer = role(f"{word}, {len(translate)} букв, начинается на {translate[0]}...", 2)

        if clear_answer(user_answer) == translate.lower():
            answers[word] = True
            role(f"Верно, {word} - это {translate}.", 1)
        else:
            answers[word] = False
            role(f"Неверно, {word} - это {translate}.", 1)

        press_enter()

    role("Правильно отвечены слова:", 1)
    [print(key) for key, val in answers.items() if val]
    role("Неправильно  отвечены слова:", 1)
    [print(key) for key, val in answers.items() if not val]

    role(f"Ваш ранг:\n{levels[total_score(answers)]}", 1)
