# Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
# the number of times they appear in elements.
# If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
#
# Input: Iterable
#
# Output: Iterable


def frequency_sort(items):
    tmp_dict = {}
    tmp_list = []
    for j in items:
        tmp_dict[j] = items.count(j)
    for w in sorted(tmp_dict, key=tmp_dict.get, reverse=True):
        for i in range(tmp_dict[w]):
            tmp_list.append(w)
    return tmp_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
