words_list = []
sorted_wordlist = []

for x in range(1, 11):
    word = input(f"Enter word {x}:")
    words_list.append(word)

length = int(input("Enter the length of word/number of characters:"))

for y in words_list:
    if len(y) >= length:
        sorted_wordlist.append(y)
        
print(f"Your words are: {sorted_wordlist}")
    