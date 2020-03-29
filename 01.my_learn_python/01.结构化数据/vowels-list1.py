word = ['a','e','i','o','u']
found = []
#mil = 'Milliways'
mil = input("input word:");
for letter in mil:
    if letter in word :
        if letter not in found:
            print(letter)
            found.append(letter)

print(found)
