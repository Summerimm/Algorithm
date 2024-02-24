sentence = input()
for c in sentence:
    if c.isupper():
        print(c.lower(), end="")
    else:
        print(c.upper(), end="")
print()