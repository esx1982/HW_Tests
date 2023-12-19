courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов",
     "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков",
     "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
     "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко",
     "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко",
     "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая",
     "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

all_list = []
def unique_names():
    for m in mentors:
        for names in m:
            all_list.append(names)
    all_names_list = []
    for mentor in all_list:
        all_names_list.append(mentor.split()[0])
    unique_names = set(all_names_list)
    all_names_sorted = sorted(list(unique_names))

    print(f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}')
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'

def top_3_names():
    for m in mentors:
        for names in m:
            all_list.append(names)
    all_names_list = []
    for mentor in all_list:
        all_names_list.append(mentor.split()[0])

    unique_names = [(i, all_names_list.count(i)) for i in (all_names_list)]
    popular = []
    for name, qty_ in set(unique_names):
        popular.append([name, qty_])
    popular.sort(key=lambda x:x[1], reverse=True)

    top_3 = []
    for name, qty_ in popular[0:3]:
        top_3.append(f'{name}: {qty_} раз(а)')
    print(", ".join(top_3))
    # return ", ".join(top_3)
    return top_3
def super_names():
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)
    pairs = []
    total = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = sorted([courses[id1], courses[id2]])
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    # print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
                    total.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
    return total

# unique_names()
# top_3_names()
# super_names()