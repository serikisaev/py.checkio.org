def is_stressful(subj):
    sub_str = ''
    for i in subj.lower():
        if ord(i) in range(97, 122) or ord(i) == 32:
            sub_str = sub_str + i
    sub_list = sub_str.split()
    sub_list_1 = []

    for i in sub_list:
        sub_str_1 = ''
        for j in i:
            if j not in sub_str_1:
                sub_str_1 = sub_str_1 + j
        sub_list_1.append(sub_str_1)
    if 'help' in sub_list_1 or 'asap' in sub_list_1 or 'urgent' in sub_list_1 or 'asp' in sub_list_1:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
