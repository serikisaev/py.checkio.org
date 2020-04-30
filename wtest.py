def first_word(text: str) -> str:

    a = str.replace(text, '.', ' ')
    b = str.replace(a, ',', ' ')

    c = b.split()
    return c[0]
#     count = 0
#     sublist = []
#
#     for i in text:
#         if ord(i) in range(0, 65) or ord(i) in range(91, 96) or ord(i) in range(123, 127):
#             if count > 0:
#                 break
#             else:
#                 continue
#         else:
#             if ord(i) in range(65, 90) or ord(i) in range(97, 122):
#                 sublist.append(i)
#                 count += 1
#     return ''.join(sublist)
#
#
if __name__ == '__main__':
    print("Example:")
    print(first_word("..., and so on ..."))

