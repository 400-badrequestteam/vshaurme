from transliterate import translit
from flask import current_app
from wtforms import ValidationError


def get_english_black_list(path_to_english_black_list_file):
    with open(path_to_english_black_list_file, 'r') as source_file:
        return source_file.read().split(',')


def get_russian_black_list(path_to_russian_black_list_file):
    with open(path_to_russian_black_list_file, 'r') as source_file:
        return source_file.read().split(',')


def transliterate_to_english(word_list):
    transliterate_list = []
    for word in word_list:
        en_word = translit(word, 'ru', reversed=True)
        transliterate_list.append(en_word)
    return transliterate_list


def username_in_black_lists(username, english_black_list,
                            russian_black_list):

    conditions = [username in english_black_list, username
                  in russian_black_list, username
                  in transliterate_to_english(russian_black_list)]
    return any(condition for condition in conditions)


def is_username_obscene(self, field):
    username = field.data
    bad_username_message = """Недопустимо использовать матерные слова!\n
                              Пожалуйста, не надо так!"""
    russian_words_path = current_app.config['VSHAURME_RUSSIAN_BAD_WORDS']
    english_words_path = current_app.config['VSHAURME_ENGLISH_BAD_WORDS']
    try:
        english_black_list = get_english_black_list(english_words_path)
        russian_black_list = get_russian_black_list(russian_words_path)
    except FileNotFoundError:
        return
    if username_in_black_lists(username, english_black_list,
                               russian_black_list):
        raise ValidationError(bad_username_message)
