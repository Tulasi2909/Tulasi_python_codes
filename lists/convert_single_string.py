letters=[['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
new=""
final=""
for letter in range(len(letters)):
    new=letters[letter]
    for index in range(len(new)):
        final+=new[index]
print(final)

