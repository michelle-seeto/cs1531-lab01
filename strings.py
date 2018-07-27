strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

# Join all of the strings
for i, word in enumerate(strings):
    if i == len(strings) -1:
        sentence = sentence + word
    else:
        sentence = sentence + word + " "
print(sentence)

print(' '.join(strings))
