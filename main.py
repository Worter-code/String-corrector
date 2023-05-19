import re


EMPTY_TEXT = ' - '


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


if __name__ == '__main__':
    print('test')
