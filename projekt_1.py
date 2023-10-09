'''
projekt_1.py: první projekt od Engeto Online Python Akademie

author: Jan Uher
email: honza.uher@post.cz
discord: eechuckyee#3664 
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


separator = '=' * 32
registred_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }

text_number = dict(enumerate(TEXTS))

user = input('Username: ')
pwd = input('Password: ')

print(separator)

if user in registred_users and registred_users[user] == pwd:
    print('Welcome to the app', user)
    print('We have 3 texts to be analyzed', separator, sep='\n')

else:
    print('unregistered user, terminating the program..')
    quit()

text_choose = int(input('Enter the number of text: ')) -1

print(separator)

if text_choose not in text_number:
    print('Text not found, terminating the program..')

else:
    all_words = []
    text_split = text_number[text_choose].split()
    
    for word in text_split:
        clear_words = word.strip('0123456789,.?! ')
        all_words.append(clear_words.lower())
    
    print('There are', len(all_words), 'words in the selected text.')

    titlecase_words = 0
    for word in text_split:
        if word[0].isupper():
            titlecase_words += 1

    print(f'There are {titlecase_words} titlecase words.')

    upper_words = 0
    for word in text_split:
        if word[:].isupper():
            upper_words += 1

    print(f'There are {upper_words} uppercase words.')

    lower_words = 0
    for word in text_split:
        if word[0:].islower():
            lower_words += 1

    print(f'There are {lower_words} lowercase words.')

    numeric = 0
    for word in text_split:
        if word.isdigit():
            numeric += 1

    print(f'There are {numeric} numeric strings.')

    num_sum = 0
    for word in text_split:
        if word.isdigit():
            num_sum += int(word)

    print(f'The sum of all the numbers {num_sum}.')
   

print(f'{separator}\nLEN|\tOCCURENCES\t|NR.\n{separator}')

word_counter = {}

for word in text_split:
    word_lenght = len(word)

    if word_lenght in word_counter:
        word_counter[word_lenght] += 1

    else:
        word_counter[word_lenght] = 1

sorted_w_len = dict(sorted(word_counter.items()))

graph = '*'

for word_lenght, count in sorted_w_len.items():
    graph = '*' * count
    fmt = ('{0:3}{1:15}{2:10}'.format(word_lenght,graph,count))
    print(fmt)

    
    

   
