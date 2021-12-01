import csv

print('Вас приветствует поисковый помощник Anime-planet. Пожалуйста, вводите ответы на английском языке.')

with open('anime.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    anime_names = []
    for name in reader:
        anime_names.append(name['Name'])

    def creating_top(person_answer, answer):
        csvfile.seek(0)
        for row in reader:
            if person_answer not in row[answer]:
                anime_names.append(row['Name'])
                anime_names.remove(row['Name'])

    questions = ['Укажите рейтинг', 'Укажите интересующие вас жанры',
                 'Какие предупреждения хотите отключить?', 'Укажите формат показа',
                 'Укажите кол-во эпизодов', 'Хотите посмотреть полностью вышедшее анимэ?(True/False)',
                 'Укажите длительность', 'Укажите год выпуска', 'Укажите предпочтительную студию']
    answers = ['Rating Score', 'Tags', 'Content Warning', 'Type', 'Episodes', 'Finished', 'Duration', 'StartYear',
               'Studios']

    for index in range(len(questions)):
        print(questions[index])
        response = input()
        if response == ' ':
            continue
        else:
            creating_top(response, answers[index])
    with open('top_anime.txt', 'w', encoding='utf-8') as file:
        for name in anime_names:
            file.write(name + '\n')

print('Теперь вам доступен файл anime_top со списком аниме по вашему запросу')