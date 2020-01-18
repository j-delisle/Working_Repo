word = input('Enter a word to determine if it is a pallendrome: ')
word_rev = []
for letter in word[::-1]:
    word_rev.append(letter)
wordrev = ''
for l in word_rev:
    wordrev+=l

print(wordrev)

# def palindrome(word):
#     word_rev = []
#     for letter in word:
#         word_rev.append(letter)
#
