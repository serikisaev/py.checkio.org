# Дана строка и нужно найти ее первое слово.
#
# При решении задачи обратите внимание на следующие моменты:
#
# В строке могут встречатся точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
# Входные параметры: Строка.
#
# Выходные параметры: Строка.

# Precondition: text can contain a-z A-Z , . '


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    count = 0
    sublist = []

    for i in text:
        if ord(i) in range(0, 65) or ord(i) in range(91, 96) or ord(i) in range(123, 127):
            if count > 0:
                break
            else:
                continue
        else:
            if ord(i) in range(65, 90) or ord(i) in range(97, 122) or ord(i) == 39:
                sublist.append(i)
                count += 1
    return ''.join(sublist)


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
