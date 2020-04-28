te = ''


def split_pairs(a):
    text = list(a)
    print(len(text))
    mass = []

    if len(text) == 0:

        return mass


    if len(text) % 2 == 0:
        for i in range(len(text) // 2):
            mass.append(text.pop(0) + text.pop(0))
        return mass

    if len(text) % 2 == 1:
        for i in range((len(text) // 2) + 1):
            try:
                a = text.pop(0)
                mass.append(a + text.pop(0))
            except:
                mass.append(a + '_')
        return mass


print(split_pairs(te))
