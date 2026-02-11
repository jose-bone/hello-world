word = input("Enter with a word: ").lower()

count = 0

for letter in word:
    if letter == "a":
        count += 1
    
print(f"The word '{word}' has {count} 'a'.")