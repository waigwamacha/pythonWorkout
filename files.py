from io import StringIO
from collections import Counter
import os
import pathlib
import csv 
from random import randrange

fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')

def get_final_line(filename):
    final_line = ''
    vowels = 'aeiou'
    for current_line in filename:
        final_line = current_line
    # for x in vowels:
    #     for char in filename:
    #         if char == x:
    #             count = sum[x]
    #         print(count)
            
    print(final_line)


# get_final_line(fakefile)
def passwd_to_dict(filename):
    passnames = {}
    with open(filename) as passwd:
        for line in passwd:
            # print(line)
            if not line.startswith(('#')):
                user_info = line.split(':')
                # print(user_info)
                passnames[user_info[0]] = user_info[2] 
        print(passnames)

# passwd_to_dict('passwd.txt')

def login_shells(filename):
    logins = {}
    
    with open(filename) as shells:
        for line in shells:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                # print(user_info[-1])
                logins[user_info[-1]] = user_info[0]
                print(logins) #can't have duplicate keys in a dict
                # d = dict(zip(user_info[-1], user_info[0]))
                # print(d)
                # if user_info[-1]:
                #         logins[user_info[-1]] = user_info[0]
                #         print(logins)
                # logins[user_info[-1]].update(user_info[0])
    # print(logins)

# login_shells('passwd.txt')

def wordcount(filename):
    num_chars = 0
    num_words = 0
    num_lines = 0
    num_uniq_words = set()
    with open(filename) as myfile:
        for line in myfile:
            num_lines += 1
            num_chars += len(line)
            wordslist = line.split()
            num_words += len(wordslist)
            # print(num_chars)
            for word in wordslist:
                num_uniq_words.add(word.lower())
        print(f'Number of lines is: {num_lines}')
        print(f'Number of characters with whitespace: {num_chars}')
        print(f'Number of words with whitespace: {num_words}')
        print(f'Number of unique words: {len(num_uniq_words)}')

# wordcount('wcfile.txt')

def find_longest_word(filename):
    """finds and returns longest word in a filename
    """
    max_word = ''
    with open(filename) as book:
        for line in book:
            one_line = line.split()
            # print(one_line)
            for word in one_line:
                if len(word) > len(max_word):
                    max_word = word
        print(max_word)

# find_longest_word('passwd.txt')

def find_all_longest_words(dirname):
    """Find all longest words in multiple
    files in a directory
    """
    return {filename: \
        find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname,\
            filename))}

# print(find_all_longest_words('books'))

# p = pathlib.Path('books')
# for one_filename in p.iterdir(): 
#     print(one_filename)
    # with one_filename[1].open() as f:
    #     lines = f.readline().split()
    #     print(lines[0:15])

def passwd_to_csv(file1, file2):
    with open(file1) as input:
        with open(file2, 'w') as output:
            infile = csv.reader(input, delimiter=':')
            outfile = csv.writer(output, delimiter='\t')
            for line in infile:
                if len(line) > 1:
                    outfile.writerow((line[0], line[2]))

    print(file2)

# passwd_to_csv('passwd.txt', 'this.csv')

def rand_nums(file1):
    with open(file1) as output:
        outfile = csv.writer(output)
        for num in range(10):
            num = randrange(10,100)
            outfile.writerow(num[:])

rand_nums('file.csv')