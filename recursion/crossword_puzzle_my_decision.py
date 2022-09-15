from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def crosswordPuzzle(crossword, words, index, index_word, index_in_word, reversed=None, end=None):
    if end:
        return crossword
    else:
        try:
            if reversed:
                letter = words[index_word][index]
                crossword[0] = crossword[0].replace(letter, "-", 1)
                # print(crossword[list_word_index][index_in_word])
                for i in crossword[index]:
                    if i == '-':
                        letter = words[index_word][index]
                        crossword[0] = crossword[0].replace(i, letter, 1)
                        index += 1
                index_word += 1
                index = 0
                print(crossword[0])
                return crosswordPuzzle(crossword, words, index, index_word, index_in_word, reversed=False)
            else:
                letter = words[index_word][index]
                crossword[index] = crossword[index].replace("-", letter, 1)
                print(crossword[index])
                index += 1
                return crosswordPuzzle(crossword, words, index, index_word, index_in_word, reversed=False)
        except Exception as ex:
            if str(ex) == 'list index out of range':
                return crosswordPuzzle(crossword, words, index, index_word, index_in_word, reversed=True, end=True)
            index_word += 1
            index = 0
            index_in_word += 1
            return crosswordPuzzle(crossword[list_word_index[index_in_word]:], words, index, index_word,
                                   index_in_word, reversed=True)


if __name__ == '__main__':
    # crossword = []
    # for _ in range(10):
    #     crossword_item = input()
    #     crossword.append(crossword_item)
    # words = input()
    crossword = ['+-++++++++', '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++',
                 '++------++', '+++++-++++', '+++++-++++']
    words = "LONDON;DELHI;ICELAND;ANKARA"
    words = words.split(";")
    index = 0
    index_word = 0
    list_word_index = []
    for word, word_next in pairwise(words):
        for word_n in word_next:
            if word_n in word:
                list_word_index.append(word.index(word_n))
                break
    index_in_word = -1
    crossword = crosswordPuzzle(crossword, words, index, index_word, index_in_word, reversed=False)
    print(crossword)

