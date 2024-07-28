"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Laskafeld
email: ondrej.laskafeld@gmail.com
discord: khadnin
"""

# Import regular expresion (na dělení textu)
import re

texts = ['''
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

# Slovník {uživatel : heslo}
number_of_texts = [1, 2, 3]
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

# Definování proměnných potřebných pro výstup
amount_of_words = 0
amount_of_words_capital = 0
amount_of_words_upper = 0
amount_of_words_lower = 0
amount_of_numbers = 0
sum_of_numbers = 0

# Slovník pro počty slov podle délky
words_len = {}

# Vstup uživatelské jméno a jeho testování
username = input("username: ")

if username in users:
# Vstup uživatelské heslo a jeho testování
    password = input("password: ")
    if password == users[username]:
        print(
            "-----------------------------------\n",
            "Welcome to the app,", username, "\n",
            "We have 3 texts to be analyzed.\n"
            "-----------------------------------",
            )
        # Vstup výběr textu pro analýzu
        text_no = input("Enter a number btw. 1 and 3 to select: ")
        # Testování zda vstup je číslo a v rozmezí 1-3
        if text_no.isdigit() and int(text_no) in number_of_texts:
            selected_text = texts[int(text_no)-1]
            # Čištění textu od čárek a teček a mezer na začátku/konci
            cleaned_text = selected_text.replace(",", "").replace(".", "").strip()
            # Rozdělení textu na slova podle mezer a konců řádků
            splited_text = re.split(" |\n", cleaned_text)
            # Počítání druhů slov
            for word in splited_text:
                amount_of_words += 1
                if word.isdigit():
                    amount_of_numbers += 1
                    sum_of_numbers += int(word)
                elif word == word.capitalize() or word[0].isdigit():
                    amount_of_words_capital += 1
                elif word == word.lower():
                    amount_of_words_lower += 1
                elif word == word.upper():
                    amount_of_words_upper += 1
            # Počítání slov podle délky
            for word in splited_text:
                if len(word) not in words_len:
                    words_len[len(word)] = 1
                else:
                    words_len[len(word)] += 1
        else:
            print("Wrong selection (1-3), terminating the program...")
            quit()
    else:
        print("Wrong password, terminating the program...")
        quit()
else:
    print("Unregistered user, terminating the program...")
    quit()

# Seřazení slovníku s počtem délek slov podle klíče
words_len_sorted = dict(sorted(words_len.items()))

# Zobrazení výstupu  
print(
    "-----------------------------------\n"
    "There are", amount_of_words, "words in the selected text.\n"
    "There are", amount_of_words_capital, "titlecase words.\n"
    "There are", amount_of_words_upper, "uppercase words.\n"
    "There are", amount_of_words_lower, "lowercase words.\n"
    "There are", amount_of_numbers, "numeric strings.\n"
    "The sum of all the numbers", sum_of_numbers, "\n"
    "-----------------------------------"
    )

# Nastavení délky prostředního sloubce "grafu" podle nejčetnějšího prvku
max_value_len = max(words_len_sorted.values())
middle_format_header = "{:^" + str(max_value_len + 2) + "}"
middle_format = "{:<" + str(max_value_len + 2) + "}"

# Zobrazení tabulky s délky slov
print("{:>3}".format("LEN"), "|", middle_format_header.format("OCCURENCES"), "|", "{:<3}".format("NR."))
for key, value in words_len_sorted.items():
    print("{:>3}".format(key), "|", middle_format.format("*" * value), "|", "{:<3}".format(value))