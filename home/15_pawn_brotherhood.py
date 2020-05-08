# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
# With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
# We have several white pawns on the chess board and only white pawns.
# You should design your code to find how many pawns are safe.
# You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
#
# Input: Placed pawns coordinates as a set of strings.
#
# Output: The number of safe pawns as a integer.


def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    print(pawns_indexes)
    count = 0
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
