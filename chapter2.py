# # print(3.14e-2)
#
# # length_of_number = len(str(2**1000000))
# #
# # #str converts int to a string
# #
# # print(length_of_number)
#
# import math
#
# # print(math.pi)
# # print(math.sqrt(25))
#
# import random
# # print(random.random()*100)
# # print(int(random.random()*100)) # a random integer between 0 and 100
# #
# # print(random.randinnt(1, 6)) # a random integer between 1 and 6
# #
# # print(random.choice(["valerie", "aob",
# #                      "Maddison" "Becky"])) # a random name in the list
# #
# #
# # print(random.choice([2, 5, 7587]))
# #
# # lower = input("Place a number as the lower bound:")
# # upper = input("another one as an upper bound")
# lower = int(input("Place a number as the lower bound:"))
# upper =int(input("Place a number as the upper bound:"))
#
#
#
# # Strings
# # I'm saying "OK".
#
# print("I'm saying\"OK\".") # back slash means negate
#
#
# print('I\'m learning\n\nPython.')


## Boolean

# print(3 > 2)
# print(3 > 5)
#
# print(3 > 2 and 3 > 5)
# print(3 > 2 or 3 > 5 or False or 100 < 7)





age = int(input("How old are you?"))

is_in_US = True

answer = input('Are you in the US?')
if answer == 'no':
    is_in_US = False


if age >= 21:    # boolean
    print('Yes, you can.')
else:
    print('Sorry, you cannot.')







