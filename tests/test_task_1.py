from task_1 import unique_names, top_3_names, super_names
from unittest import TestCase

class Test_for_Task_1(TestCase):
    def test_1(self):
        expected = ("Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир,"
                    " Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман,"
                    " Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий")
        result = unique_names()
        self.assertEqual(result, expected)

    def test_2(self):
        expected = ["Александр: 10 раз(а)", "Евгений: 5 раз(а)", "Максим: 4 раз(а)"]
        expected_1 = "Александр"
        result = top_3_names()
        self.assertListEqual(result, expected)
        self.assertIn(expected_1, str(result))

    def test_3(self):
        expected = ("На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар")
        result = super_names()
        self.assertIn(expected, result)