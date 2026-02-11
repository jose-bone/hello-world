word = input("Enter with a word: ").lower()

count = 0

for letter in word:
    count += int(letter == "a")

print(f"The word '{word}' has {count} 'a'.")