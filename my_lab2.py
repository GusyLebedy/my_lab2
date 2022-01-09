import csv


def check_num(anime_num, user_num):
    if anime_num != 'Unknown':
        if float(anime_num) >= user_num:
            return True
        else:
            return False


def check_bank(anime_bank, user_bank):
    for word in user_bank:
        if word in anime_bank:
            return True
        else:
            return False


def check_truth(anime_truth, user_truth):
    if anime_truth == user_truth:
        return True
    else:
        return False


def anime_comparison(feature, anime_character, user_character, coord):
    if anime_character(coord[feature], user_character):
        return True
    else:
        return False


print('Вас приветсвтует поисковый помощник сайта Anime-planet. Пожалуйста, вводите ответы на английском языке')

user_score = float(input('Укажите минимальный рейтинг'))

user_tags = input('Укажите жанры').split(', ')

user_warning = input('Укажите предупреждения, которые нужно исключить').split(', ')

user_type = input('Укажите формат показа').split(', ')

user_episodes = int(input('Укажите минимальное кол-во эпизодов'))

user_finished = input('Хотите посмотреть полностью вышедшее аниме?(True/False)')

user_duration = int(input('Укажите длительность'))

user_startYear = int(input('Укажите год начала показа'))

user_studios = input('Укажите студию').split(', ')

with open('anime.csv', 'r', encoding='utf-8') as f:
    wr = csv.DictReader(f, delimiter=',')
    top_anime = []
    for row in wr:
        key_score = anime_comparison('Rating Score', check_num, user_score, row)
        key_episodes = anime_comparison('Episodes', check_num, user_episodes, row)
        key_genre = anime_comparison('Tags', check_bank, user_tags, row)
        key_warnings = anime_comparison('Content Warning', check_bank, user_warning, row)
        key_types = anime_comparison('Type', check_bank, user_type, row)
        key_finish = anime_comparison('Finished', check_truth, user_finished, row)
        key_studio = anime_comparison('Studios', check_bank, user_studios, row)
        key_duration = anime_comparison('Duration', check_num, user_duration, row)
        key_start = anime_comparison('StartYear', check_num, user_startYear, row)
        filter_keys = [key_score, key_episodes, key_genre, key_warnings, key_types, key_finish, key_studio,
                       key_duration, key_start]
        if all(filter_keys):
            top_anime.append(row['Name'])

with open('anime_top.txt', 'w', encoding='utf-8') as f:
    for name in range(len(top_anime)):
        f.write(top_anime[name] + '\n')
print('Теперь вам доступен файл anime_top со списком подходящих аниме')