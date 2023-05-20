import re


EMPTY_TEXT = '___'


def correct_name(query):
    corrected = re.sub(r'[^а-яА-Я]+', '', query)
    if len(corrected) > 0:
        return corrected.capitalize()
    else:
        return EMPTY_TEXT


def correct_phone(query):
    corrected = re.sub(r'\D+', '', query)
    if len(corrected) == 11 and corrected[0] in '78':
        part1 = corrected[1:4]
        part2 = corrected[4:7]
        part3 = corrected[7:9]
        part4 = corrected[9:11]
        return f'+7 ({part1}) {part2}-{part3}-{part4}'
    else:
        return EMPTY_TEXT


def correct_email(query):
    corrected = re.sub(r'\s+', '', query)
    duplicates = '@.'
    for symbol in duplicates:
        corrected = re.sub(f'[{symbol}]+', symbol, corrected)

    email_regex = re.compile(r'[\w-]+(\.[\w-]+)*@[\w-]+(\.\w+)*\.[A-Za-z]{2,}')
    if re.fullmatch(email_regex, corrected):
        return corrected
    else:
        return EMPTY_TEXT


def correct_age(query):
    corrected = re.sub(r'\D+', '', query)
    if len(corrected) > 0:
        return corrected
    else:
        return EMPTY_TEXT


def open_input(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines_from_file = file.readlines()
    return lines_from_file


def correct_all(source_lines):
    corrected = ''
    for line in source_lines:
        line_content = line.rstrip().split('|')
        if len(line_content) != 4:
            corrected += 'Некорректная строка\n'
            continue

        name, age, phone, email = line_content
        name = correct_name(name)
        age = correct_age(age)
        phone = correct_phone(phone)
        email = correct_email(email)

        corrected_line = '|'.join((name, age, phone, email))
        corrected += f'{corrected_line}\n'

    return corrected


def save_result(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    lines = open_input('Input.txt')
    corrected_lines = correct_all(lines)
    save_result(corrected_lines, 'output.txt')
    print('Файл прошел корректировку')
