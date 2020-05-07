

text = 'sims'
subtext = 's'
if text.count('s') < 2:
    return None

result = []

flag = False
n = 1

for i, element in enumerate(text):
    if flag:
        if n > len(subtext) - 1:
            flag = False
            n = 1
        elif element == subtext[n]:
            n += 1
        elif element != subtext[n]:
            result = result[:-1]
            n = 1
            flag = False
    if element == subtext[0] and not flag:
        flag = True
        result.append(i)

return result[1]