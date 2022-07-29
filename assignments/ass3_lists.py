names = ["kaustubh", "prince"]

for name in names:
    print(f"{name} word count: ")
    letters = []
    for letter in name:
        if letter not in letters:
            letters.append(letter)
            print(f"{letter}: {name.count(letter)}")
