#Task1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
geo_log = list(filter(lambda x: 'Россия' in list(x.values())[0], geo_logs))
for geo in geo_log:
  for k, v in geo.items():
    print(f'{v[0]} {v[1]}')

#Task2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

print(list(set([x for xs in ids.values() for x in xs])))

#Task3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    ]
search = [len(querie.split()) for querie in queries]
for s in sorted(set(search)):
    print(f'Поисковых запросов, из {s} слов(а){search.count(s)/len(queries):.2%}')

#Task4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
stats_max = max(stats.items(), key = lambda x: x[1])

print(stats_max[0])

#Task5
my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_dict = {my_list[-2]: my_list[-1]}
for i in my_list[:-2][::-1]:
    my_dict = {i: my_dict}

print(my_dict)
