def pig_latin():
    """Takes a string and translates it into pig latin"""
    words = str(input("Enter a word: ")).split()
    for word in words:
        if word[0] in 'aeiou' and word[0].isupper():
            pig_word = f'{word[0:]}way'
            print(pig_word.upper())
        else:
            pig_word = f'{word[1:]}{word[0]}ay'
            print(pig_word)

# pig_latin()

def pig_sentence():
    """Takes a sentence and converts all its elements into pig latin"""
    sentence = str(input("Enter sentence here: ")).split()
    pig_sentence = []
    for word in sentence:
        if word[0] in 'aeiou':
            word = f'{word[0:]}way'
            print(word)
            pig_sentence.append(word)
        else:
            word = f'{word[1:]}{word[0]}ay'
            print(word)
            pig_sentence.append(word)
    print(pig_sentence)

# pig_sentence()

def ubbi_dubbi():
    """Translate sentence into ubbu dubbi byt prefacing every vowel with ub"""
    word1 = str(input("Enter word that you want translated: "))
    ubbi_sentence = []
    for letter in word1:
        if letter in 'aeiou':
            ubbi_sentence = ubbi_sentence.append(f'ub{letter}')
        else:
            ubbi_sentence = ubbi_sentence.append(letter)
    print(''.join(ubbi_sentence))

ubbi_dubbi()
