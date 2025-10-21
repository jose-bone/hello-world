sentences ={}

while True:
    sentence = input("Enter a sentence: ")
    if sentence == "":
        break

    if sentence not in sentences:
        sentences[sentence] = 1
    else:
        sentences[sentence] += 1

items = list(sentences.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)