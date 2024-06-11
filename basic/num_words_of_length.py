alphabet = set(input('Enter symbols in alphabet separated by spaces: ').split(' '))
word_length = int(input('Word length: '))

# from functools import reduce
# max_len = len(reduce(lambda a, b: a if len(a) > len(b) else b, alphabet))
# min_len = len(reduce(lambda a, b: a if len(a) < len(b) else b, alphabet))


words_of_length = {
    0 : [''],
    # 1: list(filter(lambda x: len(x) == 1, alphabet))
}

for length in range(1, word_length + 1):
    # valid = list(filter(lambda x: len(x) <= length, alphabet))
    
    # symbols such that len of symbol + some previous word length == required word length
    words = []
    for symbol in alphabet:
        l = len(symbol)
        try:
            prev_words = words_of_length[length - l]
            left_concat = list(map(lambda prev_word: symbol + prev_word, prev_words))
            right_concat = list(map(lambda prev_word: prev_word + symbol, prev_words))
            words += (left_concat + right_concat)
        except:
            pass
    
    
    words_of_length[length] = list(set(words))
    
for length in words_of_length.keys():
    print(f'Word Length: {length}, Total Words: {len(words_of_length[length])}\nWords: {sorted(words_of_length[length])}\n')