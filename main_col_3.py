# -*- coding: utf-8 -*-

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# Делаем список списков имён
mentors_names = [[y.split(" ")[0].strip() for y in x] for x in mentors]

pairs = []
# Попарное сравнение списков преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
# Пары храним как множества, а не как списки, потому что для множеств не важен порядок элементов
for id1 in range(len(mentors_names)):
	for id2 in range(len(mentors_names)):
		if id1 == id2:
			continue
		intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
		if len(intersection_set) > 0:
			pair = {courses[id1], courses[id2]}
			if pair not in pairs:
				pairs.append(pair)
				# Тренажёру нужен постояннный порядок, поэтому сортируем имена по алфавиту
				all_names_sorted = sorted(list(intersection_set))
				print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")