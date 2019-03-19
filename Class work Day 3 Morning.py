# # def quadreatic(a,b,c):
# #     result = 0
# #     return(a**2 + b +c, 0)
# #
# #
# #
# # def square_plus_one(a):
# #     result = a*a+1
# #     return result
# # print(square_plus_one(2))
# #
# #
# # print(square_plus_one(12))
# #
# #
# # def square_plus_one(a):
# #     result = a*a+1
# #     return result
# # print(square_plus_one(2
# #
#
# # max (1, 3, 650, -435435)
# #
# # max (1, 3, 650, -435435)
#
# import math
#
# def quadratic(a, b, c):
#     x_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
#     x_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
#     return x_1, x_2
#
# print (quadratic (1, 2, 3))


# ##   In class exercise
#
def calculate_bmi(weight, height):

    bmi = 703 * weight / (height * height)
    if bmi <= 18.5:
        return 'your bmi is {:.1f}. You are underweight.'.format(bmi)
    elif bmi <= 25:
        return 'your bmi is {:.1f}. you are normal-weight.'.format(bmi)
    elif bmi < 30:
        return 'your bmi is {:.1f}. You are overweight.'.format(bmi)

weight = float(input('Type your weight in lbs:'))
height = float(input('Type your height in inches:'))

print(calculate_bmi(weight, height))
#
#
#
#
# def fab(n):
#     """
#     this function will return the nth Fabonacci number.
#     """
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fab(n-2) + fab(n-1)
#
# for i in range(1, 10):
#     print('The {}th Fabonacci number is {}.'.format(i,fab(i)))
#
# sum = 0
# for i in range(1, 5):
#     print('in the {}th iteration, current i is {}, sum is {}'.format(i, i, sum))
#     sum = sum + i
#     print('\t after adding i, the new sum is {}\n'.format(sum))
#
# print(sum)
#
# sum = 0
# for i in range(1, 5):
#     print('in the {}th iteration, current i is {}, sum is {}'.format(i, i, sum))
#     sum = sum + i*i
#     print('\t after adding i, the new sum is {}\n'.format(sum))
#
# print(sum)

# Calculate the value of your name, if we say 'a' is worth 1

# total_value = 0
# name = 'maddison'
#
# for letter in name:
#     total_value = total_value + (ord(letter) - 96)
#
# print('The value of name {} is {}.'.format(name, total_value))
#
#
# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#         print('Blastoff!')

