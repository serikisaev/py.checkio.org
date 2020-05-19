# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# Input: Date and time as a string
#
# Output: The same date and time, but in a more readable format


import datetime


def date_time(time: str) -> str:
    sub_date = (time.split()[0]).split(sep='.')
    sub_time = (time.split()[1]).split(sep=':')
    sub_list1 = []
    sub_list2 = []
    for i in sub_date:
        sub_list1.append(int(i))
    for i in sub_time:
        sub_list2.append(int(i))
    sub_list1[2], sub_list1[0] = sub_list1[0], sub_list1[2]
    sub_list3 = sub_list1 + sub_list2
    date_all = datetime.datetime(
        tuple(sub_list3)[0],
        tuple(sub_list3)[1],
        tuple(sub_list3)[2],
        tuple(sub_list3)[3],
        tuple(sub_list3)[4]
    )

    if date_all.strftime("%H") == '01' and date_all.strftime("%M") == '01':
        return date_all.strftime('{}{}{}{}{}{}'.format(str(date_all.day), " %B %Y year ", str(date_all.hour),
                                                       " hour ", str(date_all.minute), " minute"))
    if date_all.strftime("%H") == '01':
        return date_all.strftime('{}{}{}{}{}{}'.format(str(date_all.day), " %B %Y year ", str(date_all.hour),
                                                       " hour ", str(date_all.minute), " minutes"))
    if date_all.strftime("%M") == '01':
        return date_all.strftime('{}{}{}{}{}{}'.format(str(date_all.day), " %B %Y year ", str(date_all.hour),
                                                       " hours ", str(date_all.minute), " minute"))
    else:
        return date_all.strftime('{}{}{}{}{}{}'.format(str(date_all.day), " %B %Y year ", str(date_all.hour),
                                                       " hours ", str(date_all.minute), " minutes"))


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
