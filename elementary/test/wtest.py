def correct_sentence(text: str) -> str:
    if text[-1] != '.' and text.istitle() == False:
            return text[0].upper() + text[1:] +'.'
    else:
        return text[0].upper() + text[1:]


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))