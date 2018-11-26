def find_word_vertical(crosswords, word):
    x = [None, None]
    for j in range(len(crosswords)):
        column = ''
        for i in range(len(crosswords)):
            column += crosswords[i][j]
        if word in column:
            x[0] = column.index(word)
            x[1] = j
            break
    if x[0] != None:       
        return x 

def find_word_horizontal(crosswords, word):
    x=[None, None]
    for i in range(len(crosswords)):
        row = ''.join(crosswords[i])
        if word in row:
            x[0] = i 
            x[1] = row.index(word)
            break
    if x[0] != None:       
        return x 

def capitalize_word_in_crossord(crosswords, word):
    index = find_word_horizontal(crosswords, word)
    if index != None:
        i = index[0]
        j = index[1]
        crosswords[i][j:j + len(word)] = word.upper()
    else:
        index = find_word_vertical(crosswords, word)
        if index != None:
            i = index[0]
            j = index[1]
            for k in range(len(word)):
                crosswords[i + k][j] = word[k].upper()       
    return crosswords 

crosswords = [
['s','d','o','g'],
['c','u','c','m'],
['a','c','a','t'],
['t','e','t','k']
]
word = 'cat'

print(capitalize_word_in_crossord(crosswords, word))
