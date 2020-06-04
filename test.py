def disconnected_users(net, users, source, crushes):
    sub_list = []
    sub_list1 = []
    count = 0
    if len(crushes) == 1:
        for i in net:
            if crushes[0] not in i:
                sub_list.append(i)
        if len(sub_list) == 0:
            return sum(users.values()) - users[crushes[0]]
        else:
            for i in sub_list:
                for j in i:
                    sub_list1.append(j)
            if source in set(sub_list1):
                for i in set(sub_list1):
                    count += users[i]
                return sum(users.values()) - count
            else:
                return sum(users.values()) - users[source]
    else:
        for i in crushes:
            for j in net:
                if i in j:
                    sub_list.append(j)
        print('удаленные связи между отправляющей и сломанными станциями:')
        print(sub_list)  # удаленные связи между отправляющей и сломанными станциями
        for i in net:
            if i not in sub_list:
                sub_list1.append(i)
        print('исправные связи между станциями:')
        print(sub_list1)
        sub_list2 = []
        for i in sub_list:
            for j in i:
                sub_list2.append(j)
        a = set(sub_list2)
        a.remove(source)
        for i in a:
            count += users[i]
        return count


assert disconnected_users(
    [["A", "B"], ["A", "C"], ["A", "D"], ["A", "E"], ["A", "F"]],
    {"A": 10, "B": 10, "C": 10, "D": 10, "E": 10, "F": 10},
    "A",
    ["B", "C"]
) == 20
