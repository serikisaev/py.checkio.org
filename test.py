def disconnected_users(net, users, source, crushes):
    sub_list = []
    sub_list1 = []
    count = 0
    if len(crushes) == 1:
        if source in crushes:
            return sum(users.values())
        else:
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
        for i in net:
            if i not in sub_list:
                sub_list1.append(i)
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
    [["A","B"],["B","C"],["C","D"]],
    {"A":10,"B":20,"C":30,"D":40},
    "A",
    ["A"]
) == 100
