# Let's teach the Robots to distinguish words and numbers.
#
# You are given a string with words and numbers separated by whitespaces (one space).
# The words contains only letters. You should check if the string contains three words in succession.
# For example, the string "start 5 one two three 7 end" contains three words in succession.
#
# Input: A string with words.
#
# Output: The answer as a boolean.


def checkio(words: str) -> bool:
    count = 0
    sub_list = words.split()
    for i in sub_list:
        try:
            if count == 3:
                break
            int(i)
            count = 0
        except:
            if i not in '0123456789':
                count += 1
            else:
                if count == 3:
                    break
                count = 0
    if count >= 3:
        return True
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "four five six"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
