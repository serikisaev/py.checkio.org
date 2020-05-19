# You have to split a given array into two arrays.
# If it has an odd amount of elements, then the first array should have more elements.
# If it has no elements, then two empty arrays should be returned.


from math import ceil


def split_list(items: list) -> list:
    sub_len = ceil(len(items) / 2)
    sub_list_1 = []
    for i in range(sub_len):
        sub_list_1.append(items[i])
    return [sub_list_1, items[sub_len:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
