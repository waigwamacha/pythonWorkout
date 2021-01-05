
# class wordLength():
#     """takes a list of words and returns a tuple with the longest, shortest words and average of all words"""
empty_list = []
result = []
list_input = int(input("Enter the number of words for this list: \n"))
for word in range(0, list_input):
    word = input("Enter word" + str(word+1)+ ": ")
    empty_list.append(word)

def longestWord():
    """finds longest word and returns it"""
    max1 = len(empty_list[0])
    longest_word = empty_list[0]
    for longest in empty_list:
        if len(longest)>max1:
            max1 = len(longest)
            longest_word = longest
            long_len = len(longest_word)
            result.append(long_len)
    print(f"The longest word ({longest_word}) has a length of {long_len}")

longestWord()

def shortesWord():
    """finds the shortest word in the list"""
    min1 = len(empty_list[0])
    shortest_word = empty_list[0]
    for shortest in empty_list:
        if len(shortest)<min1:
            min1 = len(shortest)
            shortest_word = shortest
            short_len = len(shortest_word)
    print(f"The shortest word ({shortest_word}) has a length of {short_len}")

shortesWord()

def averageWordLength():
    """find the average word length in a list"""
    w_length = 0
    num_words = 0
    for word in empty_list:
        word_length = len(word)
        w_length += word_length
        num_words += 1
    average_l = w_length/num_words
    print(f"Average word length is {average_l}")

averageWordLength()

