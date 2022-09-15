import copy

N=10

word_map = []

for n in range(0, N):
    word_map.append([x for x in input().strip()])

words = input().strip().split(';')


def char_is_letter(ch):
    char_code = ord(ch)
    return 65 <= char_code <= 90


def char_is_minus(ch):
    return ord(ch) == 45


def char_is_minus_or_letter(ch):
    return char_is_letter(ch) or char_is_minus(ch)


def find_vertical_words(word_map, words, row=0, col=0):
    if not words:
        return results.append(word_map)
    new_word_len = 0
    no_words_in_col = True
    for r in range(row, N):
        ch = word_map[r][col]
        new_word_len = new_word_len + 1 if char_is_minus_or_letter(ch) else 0
        for word in words:
            if len(word) == new_word_len:
                new_word_map = copy.deepcopy(word_map)
                word_completed = False
                for i in range(new_word_len):
                    old_ch = word_map[r - new_word_len + 1 + i][col]
                    if char_is_minus(old_ch) or old_ch == word[i]:
                        new_word_map[r - new_word_len + 1 + i][col] = word[i]
                        word_completed = True
                    else:
                        word_completed = False
                        break
                if word_completed:
                    no_words_in_col = False
                    find_vertical_words(new_word_map, [w for w in words if w != word], r + 1, col)
    if no_words_in_col and col < N - 1:
        find_vertical_words(word_map, words, 0, col + 1)


def find_horizontal_words(word_map, words, row=0, col=0):
    if row > N - 1:
        return find_vertical_words(word_map, words)
    new_word_len = 0
    no_words_in_row = True
    for c in range(col, N):
        ch = word_map[row][c]
        new_word_len = new_word_len + 1 if char_is_minus(ch) else 0
        for word in words:
            if len(word) == new_word_len:
                no_words_in_row = False
                new_word_map = copy.deepcopy(word_map)
                for i in range(new_word_len):
                    new_word_map[row][c - new_word_len + 1 + i] = word[i]
                find_horizontal_words(new_word_map, [w for w in words if w != word], row, c + 1)

    if no_words_in_row:
        find_horizontal_words(word_map, words, row + 1)


results = []
find_horizontal_words(word_map, words)
for result in results:
    for row in result:
        print(''.join(row))