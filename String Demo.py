# team = 'New England Patriots'
#
#
# print(len(team))
#
# letter = team[1]
# print(letter)
#
# print(team[0])
# print(team[2])
#
# print(team[19])
#
# print(team[len(team)-1])
# print(team[-20])
#
# team = 'New England Patriots'
# for letter in team:
#     print(letter)
#
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)
#
#
# result = 0
# for number in range(1, 1001):
#     if number%2 == 0:    # this means number is an odd number
#        result = result + number  # do nothing so don't need else
# print(result)


team = 'New England Patriots'

print(team[0:11])     # we want to slice str to get all chr in  str before the 11 chr
print(team[12:20])

print(team[12:])     # gives you all the letters after letter 12
print(team[::2])   # gives you every other letter

a = 'level'
print(a == a[::-1])   # sees if word is a palindrome


def is_palidrome(word):
    return word == word[::-1]

print(is_palindrome(word))

new_team = ""
for letter in team:
    if letter != 'a':
        new_team = new_team+letter  # add letter into new_team if letter isn't 'a'

print(new_team)

print(team.upper())  # converts all letters to uppercase

print(team.find('e'))  # finds the letter position of 'e'






