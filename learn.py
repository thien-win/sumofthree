# # myname = input('What is your name?')
# # print('hello world')
# if __name__ == '__main__':
#     number = int(input().strip())
#     if number % 2 == 0:
#         if number >= 2 and number <= 5:
#             print('Not Weird')
#             if 6 <= number <= 20:
#                 print('Weird')
#                 if number >= 20:
#                     print('Not Weird')
#     else:
#         print('Weird')
# def is_leap(yr):
#     leap = False
#     while yr in range(1900, pow(10, 5)+1):
#         if yr % 4 == 0:
#             if yr % 100 != 0:
#                 return True
#             elif yr % 400 == 0:
#                 return leap
#             else:
#                 return leap
#         else:
#             leap = False
#         return leap

#    # else:
#     #     return leap

#     # return leap


# year = int(input())
# print(is_leap(1992))

number = int(123)
string_number = str(number)
print(string_number)

print(len(string_number))
print(string_number[0])
for i in string_number:
    string_number[0] = string_number[i]
