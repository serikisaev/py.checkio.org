# The function should recognise if a subject line is stressful.
# A stressful subject line means that all letters are in uppercase,
# and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words:
# "help", "asap", "urgent". Any of those "red" words can be spelled in
# different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way
# "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
#
# Input: Subject line as a string.
#
# Output: Boolean.


def is_stressful(subj):
    if subj.isupper():
        return True
    if subj[-3:] == '!!!':
        return True
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
    assert is_stressful("where are you?!!!!") == True, "Third"
    assert is_stressful("HI HOW ARE YOU?") == True, "Fourth"
    print('Done! Go Check it!')
