import re


EMPTY_TEXT = ' - '


def correct_name(query):
    corrected = re.sub(r'[^а-яА-Я]+', '', query)
    if len(corrected) > 0:
        return corrected.capitalize()
    else:
        return EMPTY_TEXT


if __name__ == '__main__':
    print('test')
