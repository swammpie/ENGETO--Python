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

user = input('Username: ')
pwd = input('Password: ')

registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

if user not in registered_users or registered_users[user] != pwd:
    print('Unregistered user. Terminating the program..')
    quit()

print(separator)

text_number = input('Enter the number of text: ')
if text_number.isdigit() and 1 <= int(text_number) <= len(TEXTS):
    text_number = int(text_number) - 1
else:
    print('Invalid input or text not found. Terminating the program..')
    quit()

selected_text = TEXTS[text_number]

word_stats = {
    'total_words': 0,
    'titlecase_words': 0,
    'uppercase_words': 0,
    'lowercase_words': 0,
    'numeric_strings': 0,
    'numeric_sum': 0
}

word_lengths_histogram = {}

words = selected_text.split()
for word in words:
    clear_word = word.strip(',.?! ')
    word_length = len(clear_word)
    word_stats['total_words'] += 1

    if word.istitle():
        word_stats['titlecase_words'] += 1
    if word.isupper():
        word_stats['uppercase_words'] += 1
    if word.islower():
        word_stats['lowercase_words'] += 1
    if word.isdigit():
        word_stats['numeric_strings'] += 1
        word_stats['numeric_sum'] += int(word)

    word_lengths_histogram[word_length] = word_lengths_histogram.get(word_length, 0) + 1

print(separator)

print(f'There are {word_stats["total_words"]} words in the selected text.')
print(f'There are {word_stats["titlecase_words"]} titlecase words.')
print(f'There are {word_stats["uppercase_words"]} uppercase words.')
print(f'There are {word_stats["lowercase_words"]} lowercase words.')
print(f'There are {word_stats["numeric_strings"]} numeric strings.')
print(f'The sum of all the numbers is {word_stats["numeric_sum"]}.')
print(separator)
print(f'{"LEN":<3}{"|":<2}{"OCCURRENCES":<15}{"|":<2}{"NR.":<10}')
print(separator)

word_lengths = [len(word.strip(',.?! ')) for word in words]
word_counter = {}
for length in word_lengths:
    word_counter[length] = word_counter.get(length, 0) + 1

for length, count in sorted(word_counter.items()):
    print(f'{length:<3}{"|":<2}{"*"*count:<15}{"|":<2}{count:<10}')
