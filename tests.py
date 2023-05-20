from unittest import TestCase, main
from main import *
import os


class ProgramTest(TestCase):
    def test_name_correcting(self):
        self.assertEqual(correct_name('Ваня'), 'Ваня')
        self.assertEqual(correct_name('анатолий'), 'Анатолий')
        self.assertEqual(correct_name('ZenimAx'), EMPTY_TEXT)
        self.assertEqual(correct_name('4646К541о2л312я3'), 'Коля')
        self.assertEqual(correct_name('89463765473'), EMPTY_TEXT)

    def test_age_correcting(self):
        self.assertEqual(correct_age('22'), '22')
        self.assertEqual(correct_age('Я там 10 лет прожил'), '10')
        self.assertEqual(correct_age('Возраст'), EMPTY_TEXT)
        self.assertEqual(correct_age(''), EMPTY_TEXT)

    def test_phone_correcting(self):
        self.assertEqual(correct_phone('+78005553535'), '+7 (800) 555-35-35')
        self.assertEqual(correct_phone('4564612345678901'), EMPTY_TEXT)
        self.assertEqual(correct_phone('+84587-8-9-0-1-2-3'), '+7 (458) 789-01-23')
        self.assertEqual(correct_phone('не звоните мне'), EMPTY_TEXT)

    def test_email_correcting(self):
        self.assertEqual(correct_email('uirpo@mag.ru'), 'uirpo@mag.ru')
        self.assertEqual(correct_email('Ivan@@@@Test..ru'), 'Ivan@Test.ru')
        self.assertEqual(correct_email('@create@test@commit'), EMPTY_TEXT)

    def test_opening(self):
        test_path = 'test_opening.txt'
        test_content = 'test'
        with open(test_path, 'w', encoding='utf-8') as file:
            file.write(test_content)
        self.assertEqual(open_input(test_path), [test_content])
        os.remove(test_path)

    def test_correcting_one_line(self):
        test_query = ['Ванечка|22 годика|8(800)555-35-35|lastpractice@uirpo.ru']
        expected = 'Ванечка|22|+7 (800) 555-35-35|lastpractice@uirpo.ru\n'
        self.assertEqual(correct_all(test_query), expected)

    def test_correcting_some_lines(self):
        test_query = ['АнТоШа|4|000000|it@mirea.ru',
                      'Степан|восемдесят два|88005553535|stepan@@mail.ru',
                      'name|age|phone|email']
        expected = f'Василий|10|{EMPTY_TEXT}|it@mirea.ru\n' +\
                   f'Степан|{EMPTY_TEXT}|+7 (800) 555-35-35|stepan@mail.ru\n' +\
                   f'{EMPTY_TEXT}|{EMPTY_TEXT}|{EMPTY_TEXT}|{EMPTY_TEXT}\n'
        self.assertEqual(correct_all(test_query), expected)

    def test_save_file(self):
        test_path = 'test_saving.txt'
        test_content = 'test'
        save_result(test_content, test_path)
        with open(test_path, 'r', encoding='utf-8') as file:
            from_file = file.read()
        self.assertEqual(from_file, test_content)
        os.remove(test_path)


if __name__ == '__main__':
    main()

