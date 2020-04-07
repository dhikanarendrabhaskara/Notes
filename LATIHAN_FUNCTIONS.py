


########## SOAL 1 (SEEK THE HIGHEST VALUE)

# def max_two(x,y):
#     if x > y:
#         return x
#     elif x < y:
#         return y

# def max_three (x, y, z):
#     return max_two(x, max_two(z,y))
# print(max_three(-3,-2,-7))                ### hasilnya -2



########## SOAL 2 (SUM THE NUMBERS MANUALLY)

# num = [8, 2, 3, 0, 7]

# def sum(x):
#     total = 0
#     for i in num:
#         total += i
#     return total

# print(sum(num))             ### hasilnya 20



########## SOAL 3 (MULTIPLY THE NUMBERS MANUALLY)

# num = [8, 2, 3, -1, 7]

# def multiply(x):
#     total = 1
#     for i in num:
#         total *= i
#     return total

# print(multiply(num))



########## SOAL1 LATIHAN PURWA (COMPUND INTEREST)

# def calculate_years (principal,interest,tax,desired):
#     year = 0
#     while (principal < desired):
#         principal = principal + ((principal*interest) - (principal*interest*tax))
#         year += 1
#     return year

# print(calculate_years(1000,.05,.18,1100))           ### hasilnya 3



########## SOAL2 LATIHANPURWA (EXPAND INPUT)

# def expandForm(num):
#     number = str(num)
#     expand = []
#     for i in range (len(number)):
#         if number[i] != '0':
#             if i == len(number)-1:
#                 expand.append(number[i])
#             else:
#                 expand.append(str(int(number[i])* 10**(len(number)-1-i)))
#     expand1 = " + ".join(expand)
#     return expand1
# print(expandForm(2001)


########## SOAL 4 (MANUALLY REVERSE WORDS)

# def reverse(x):
#     z = ''
#     index = len(x)

#     while index > 0:
#         z += x[index-1]
#         index -= 1
#     return z

# print(reverse('word'))


########## SOAL 5 (MANUALLY REVERSE WORDS)

# def num(x):
#     if x in range(1,10):
#         print("num is within range")
#     else:
#         print("num is beyond range")

# num(4)        

# def test_range(n):

#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(111)


############# SOAL 6 (FAKTORIAL)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Input a number to compute factorial: "))
# print(factorial(n))


########### SOAL 7 (NGITUNG BRP UPPER & LOWER)


# def calculate(string):
#     upper = 0
#     lower = 0
#     for i in string:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#         else:
#             pass
#     print("upper ada {}".format(upper))
#     print("lower ada {}".format(lower))  

# calculate("Aku dan Kamu")


######### SOAL 8 (SORTIR ANGKA UNIK)

# num = [1,2,2,3,25,1,2,333,2,1,2,2,2,1,1,2,3]
# num = list(set(num))
# num = sorted(num)

# print(num)                  ### Hasilnya udh di sortir unik/set dan sorted [1, 2, 3, 25, 333]



######### SOAL 9 (CARI ANGKA PRIMA)


# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))



########### SOAL 10 (NGAMBIL ANGKA GENAP & GANJIL DR LIST)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# z = []
# z1 = []

# for i in list:
#     if i % 2 == 0:
#         z.append(i)
#     else:
#         z1.append(i)
# print(z)                            #### [2, 4, 6, 8]
# print(z1)                           #### [1, 3, 5, 7, 9]



########## SOAL 11 (CHECK PERFECT NUMBER OR NOT)

# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))



############ SOAL 12 (CEK KATA2 PALINDROME ATAU ENGGA)

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza'))          ### True


######## SOAL 13 (COUNT FIRST N ROWS OF PASCAL"S TRIANGLE )

# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6)



######## SOAL 14 (CEK KALIMAT PANGRAM/MENGANDUNG SEMUA ALFABET ATAU ENGGA)

# import string, sys
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
 
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 


    
########## SOAL 15 (NGESORT HURUF DARI INPUT)

# list = input()
# items=[n for n in list.split('-')]
# items.sort()
# print('-'.join(items))
 
# ATAU

# list = ["green", "red", "yellow", "blue"]
# list.sort()
# print(list)



########## SOAL 16 (LIST BERISI RANGE 1-30 dan KUADRATNYA)

# my_list = []

# for i in range(1,31):
#     result = i**2
#     my_list.append(result)
# print(my_list)


######## SOAL 17 (*BOLD/ITALIC/UNDERLINE)

# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"
# print(hello()) ## returns "<b><i><u>hello world</u></i></b>"





####### SORTIR ALPHANUMERIC

# def alphanumeric(string):
#     import re
#     result = True

#     if not (re.search('[a-z]',string)):
#         result = False
#     if not (re.search('[A-Z]',string)):
#         result = False
#     if not (re.search('[0-9]',string)):
#         result = False
#     else:
#         result = True
    
#     return result

# print(alphanumeric("heyhoHooo123"))
# print(alphanumeric("heyho ooo"))
# print(alphanumeric("heyhoHooo!!!!"))
# print(alphanumeric(".heyhoooo"))

#### ATAU ####

# def alphanumeric(string):
#     result = True
#     mylist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
#     for i in string:
#         i = i.lower()
#         if i not in mylist:
#             result = False
#             break
#         if i in mylist:
#             result = True 
#     return result
    
# print(alphanumeric("heyhoHooo123"))
# print(alphanumeric("heyho ooo"))
# print(alphanumeric("heyhoHooo!!!!"))
# print(alphanumeric(".heyhoooo"))

#### ATAU ####

# def alphanumeric(string):
#     return string.isalnum()
    
# print(alphanumeric("heyhoHooo123"))
# print(alphanumeric("heyho ooo"))
# print(alphanumeric("heyhoHooo!!!!"))
# print(alphanumeric(".heyhoooo"))