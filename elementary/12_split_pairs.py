from itertools import zip_longest

def split_pairs(a):
    # result = []
    # for l, r in zip_longest(a[::2], a[1::2]):
    #     if r is not None:
    #         result.append(l + r)
    #     else:
    #         result.append(l + '_')
    # return result

    result = []
    for i in range(0, len(a), 2):
        sub_s = a[i:i + 2]
        if len(sub_s) < 2:
            result.append(sub_s + '_')
        else:
            result.append(sub_s)
    return result

    # text = list(a)
    # print(len(text))
    # mass = []
    #
    # if len(text) == 0:
    #     return mass
    #
    # if len(text) % 2 == 0:
    #     for i in range(len(text) // 2):
    #         mass.append(text.pop(0) + text.pop(0))
    #     return mass
    #
    # if len(text) % 2 == 1:
    #     for i in range((len(text) // 2) + 1):
    #         try:
    #             a = text.pop(0)
    #             mass.append(a + text.pop(0))
    #         except:
    #             mass.append(a + '_')
    #     return mass


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
