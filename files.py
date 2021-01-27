from io import StringIO
from collections import Counter
import os
import pathlib
import csv 
import glob 
import json 

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

# rand_nums('file.csv')

def print_scores(dirname):
    """Takes a directory as argument and \
        prints a summary of student scores founs
    """
    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        print(filename)
        scores[filename] = {}
        print(scores)

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores)/
                                len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')
        
# print_scores('scores')
def find_files(dirname):
    for filename in glob.glob(f'{dirname}/*.pdf'):
        print(filename)

# find_files('/Users/macbook/Desktop')

def csv_to_json(csvfile, jsonfile):
    data = {}
    with open(csvfile) as csvf:
        csvreader = csv.DictReader(csvf)
        print(csvreader)

        # for rows in csvreader:
        #     key = rows['Username']
        #     data[key] = rows

# data1 = {}
# with open('this.csv') as csvf:
#         csvreader = csv.DictReader(csvf)
#         print(csvreader[0])
#         for rows in csvreader:
#             key = rows[0]
#             data1[key] = rows
#         print(data1)

def reverse_lines(file1, file2):
    """
    takes an input file and reverses all characters, saving them in a new file, file2
    """
    with open(file1) as input, open(file2, 'w') as output:
        for word in input:
            word.rstrip() #to remove the newline character at the end
            word1 = word[::-1]
            output.write(f'{word1}\n')
            print(word1)

# reverse_lines('lines.txt', 'reverse.txt')

def vowels_consonants(file1, file2):
    """
    takes a file, file1, finds its vowels and copies them to another file, file2
    """
    present_vowels = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    with open(file1) as infile, open(file2, 'w') as output:
        for word in infile:
            word.rstrip()
            for vowel in vowels:
                if vowel in word:
                    output.write(f'{vowel}')
                    present_vowels.append(vowel)
    print(present_vowels)

vowels_consonants('wcfile.txt', 'vowels.txt')

