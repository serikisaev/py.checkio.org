# Input: Four arguments: network structure (as a list of connections between the nodes),
# users of each node (as dict where keys are the node-names and values are the amounts of users),
# name of the node that sends email, and the list of crashed nodes.
#
# Output: Int. The amount of users that won't receive an email.


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




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
