###### SOAL 1 (LENGTH & FRONT-END WORD COUNTER)
# def counter(word):
#     counter = 0
#     for item in word:
#         if len(item)>2 and item[0] == item[-1]:
#             counter += 1
#     return counter

# print(counter(['abc', 'xyz', 'aba', '1221']))         ##hasilnya 2



##### SOAL 2 (MAX & MIN)
# def max(word):
#     max = word[-1]
#     for item in word:
#         if item> max:
#             max = item
#     return max

# def min(word):
#     min = word[0]
#     for item in word:
#         if item < min:
#             min = item
#     return min

# print(max([2,8,-7,0]))          ##hasilnya 8
# print(min([2,8,-7,0]))          ##hasilnya -7



##### SOAL 3 (SORT LIST BY LAST VALUE)
# def last(n): 
#     return n[-1]

# def sort_list(tuples):
#     return sorted(tuples)

# def sort_list_last(tuples):
#     return sorted(tuples, key=last)

# print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))              ## hasilnya: [(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))         ## hasilnya: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



##### SOAL 4 REMOVE DUPLICATE
# a = [10,20,30,20,10,50,60,40,80,50,40]


# sort1 = sorted(list(set(a)))
# print(sort1)                                        ## hasilnya [10, 20, 30, 40, 50, 60, 80]



##### SOAL 5 (CHECK EMPTY LIST)
# L = []
# if not L:
#   print("List is empty")            ## hasilnya List is empty
 


##### SOAL 6 (SORT PANJANG KATA DLM LIST)
# def long_words(n,text):
#     long_words = []
#     counter = 0
#     my_text = text.split() 
#     for item in my_text:
#         if len(item)>= n:
#             long_words.append(item)
#             counter += 1
#     print("There are {} words, and they are:".format(counter))
#     print(long_words)

# long_words(5, "The quick brown fox jumps over the lazy dog")        ## There are 3 words, and they are: ['quick', 'brown', 'jumps']



# ##### SOAL 7 (SIMILARITY BETWEEN LISTS (OR NOT))
# def similarity(list1,list2):
#     result1 = False
#     result2 = []
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 result1 = True
#                 result2.append(i)
#     print(result2)  
#     return result1  


## ATAU ##
# def similarity(list1,list2):
#     result1 = False
#     result2 = []
#     for item in list1:
#         if item in list2:
#             result2.append(item)
#             result1 = True          
#     print(result2)  
#     return result1                 
# print(similarity([1,2,3,4,5],[4,5,6,7,8,9]))                 ## hasilnya: [4, 5] True
# print(similarity([1,2,3,4,5],[6,7,8,9]))                     ## hasilnya: [] False
# print(similarity([1,2,3,4,5],[1,1,1,1,1,1,6,7,8,9]))         ## hasilnya: [1, 1, 1, 1, 1, 1] True


## ATAU ##
# color1 = ["Red", "Green", "Orange", "White"]
# color2 = ["Black", "Green", "White", "Pink"]
# print(set(color1) & set(color2))                                ## hasilnya: {'White', 'Green'}



####### SOAL 7.1 (DIFFERENCE BETWEEN LISTS)
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8,9]
# difference = (set(list1)-set(list2))
# print(difference)                                               ### hasilnya: {1, 2, 3}


# Color1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Color2 = ['White', 'Black', 'Pink', 'Yellow']                   
# diff = []
# same = []

# for item in Color1:
#     if item not in Color2:
#         diff.append(item)
#     if item in Color2:
#         same.append(item)
# print(diff)                                                     ### hasilnya: ['Red', 'Green']
# print(same)                                                     ### hasilnya: ['White', 'Black', 'Pink', 'Yellow']


##### SOAL 8 (ELIMINATE ELEMENTS IN LIST)
# Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Color = [x for (i,x) in enumerate(Color) if i not in (0,4,5)]
# print(Color)                                            ## hasilnya: ['Green', 'White', 'Black']
# enumerateColor = list(enumerate(Color))                 ## hasilnya: [(0, 'Green'), (1, 'White'), (2, 'Black')]
# print(enumerateColor)



##### SOAL 9 (3 x 4 X 6 ARRAY)
# array = [[ ['i' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)      ## hasilnya: [[['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i']], [['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i']], [['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i'], ['i', 'i', 'i', 'i', 'i', 'i']]]



##### SOAL 10 (X FOR X IN NUM)
# num = [7,8, 120, 25, 44, 20, 27]
# even = [x for x in num if x%2 ==0]
# odd = [x for x in num if x%2 !=0]
# belowten = [x for x in num if x < 10]

# print(even)                 ## [8, 120, 44, 20]
# print(odd)                  ## [7, 25, 27]
# print(belowten)             ## [7, 8]



##### SOAL 11 (SHUFLING & RANDOMIZE)
# from random import shuffle
# import random

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# random.shuffle(color)
# print(color)                                        ## shuffled: ['Yellow', 'Pink', 'White', 'Red', 'Green', 'Black']
# randomize = random.choices(color)
# print(randomize)                                    ## pick random: ['Red']



##### SOAL 12 (PRINT FIRST 5 & LAST 5)
# L = []
# for i in range(1,21):
#     L.append(i**2)
# print(L[:5])                    ## [1, 4, 9, 16, 25]
# print(L[-5:])                   ## [256, 289, 324, 361, 400]



##### SOAL 12 (PRINT AFTER 5th ELEMENT)
# L = []
# for i in range(1,21):
#     L.append(i**2)
# print(L[5:])                    ## [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]



##### SOAL 13 (ACCESS INDEX VIA ENUMERATE)
# num = [5, 15, 35, 8, 98]

# for idx, val in enumerate(num):
#     print(idx,val)

# 0 5         ## hasilnya
# 1 15
# 2 35
# 3 8
# 4 98



##### SOAL 14 (COVERT LIST TO STRING)
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = "-".join(color)
# print(color)                        ## hasilnya: Red-Green-White-Black-Pink-Yellow



##### SOAL 15 (FIND INDEX OF VALUE INSIDE LIST)
# num = [10, 30, 4, -6]
# print(num.index(4))                     ## hasilnya: 2



##### SOAL 16 (MERGE LIST)
# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))        ## perlu pake "*" nya
# print(new_merged_list)                                         ## hasilnya: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]



##### SOAL 16.2 (MERGE KONTEN SUATU LIST ANGKA PAKE JOIN)

# L = [11, 33, 50]
# x = "".join(map(str,L))
# print(x)                          ## HASILNYA: 113350

## ATAU ##
# num = [1, 2, 3, 4, 5]
# print(*num)                       ## HASILNYA: 1 2 3 4 5 (PAKE SPASI)

##### SOAL 17 (ADD LIST)

# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = []
# final_list.extend(list1)
# final_list.extend(list2)
# print(final_list)                           ### [1, 2, 3, 0, 'Red', 'Green', 'Black']

# ## ATAU ##
# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# list1.extend(list2)
# print(list1)                                ### [1, 2, 3, 0, 'Red', 'Green', 'Black']

# ## ATAU ##
# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)                           ### [1, 2, 3, 0, 'Red', 'Green', 'Black']

## ATAU ## (REPLACING LAST ELEMENT WITH NEW LIST)
# num1 = [1, 3, 5, 7, 9, 11]
# num2 = [2, 4, 6, 8]
# num1[-1::] = num2
# print(num1)                                 ### [1, 3, 5, 7, 9, 2, 4, 6, 8]



##### SOAL 18 (COMPARING CIRCULAR SIMILARITY BETWEEN LISTS)
# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
# print('Compare list1 and list3')
# print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# #HASILNYA:
# Compare list1 and list2
# True
# Compare list1 and list3
# False



###### (GABUNGIN LIST SECARA ZIP)
# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
# list4 = []
# list4 = list(zip(list1,list2,list3))
# print(list4)                    
# ## HASILNYA: [(10, 10, 1), (10, 10, 10), (0, 10, 10), (0, 0, 0), (10, 0, 0)]

# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# mylist = list(zip(color_name,color_code))
# print(mylist)
## HASILNYA: [('Black', '#000000'), ('Red', '#FF0000'), ('Maroon', '#800000'), ('Yellow', '#FFFF00')]



# ##### SOAL 19 (DETERMINE SECOND SMALLEST & LARGEST NUMBER)

# def second_smallest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[1]   

# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))       ## hasilnya: 0

# def second_largest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   dup_items = set()
#   uniq_items = []
#   for x in numbers:
#     if x not in dup_items:
#       uniq_items.append(x)
#       dup_items.add(x)
#   uniq_items.sort()    
#   return  uniq_items[-2]   

# print(second_largest([1, 1, 0, 0, 2, -2, -2]))        ## hasilnya: 1



##### SOAL 20 (COLLECTION COUNTING)
# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)

# ## hasilnya:
# Original List :  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# Frequency of the elements in the List :  Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})



##### SOAL 21 (CONCANTENATE LIST WITH N RANGE NUMBERS)
# my_list = ['p', 'q']
# n = 4
# new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
# print(new_list)                 ##### ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4']



###### SOAL 22 (GENERATING ALL SUBLISTS)
# from itertools import combinations
# def sub_lists(my_list):
# 	subs = []
# 	for i in range(0, len(my_list)+1):
# 	  temp = [list(x) for x in combinations(my_list, i)]
# 	  if len(temp)>0:
# 	    subs.extend(temp)
# 	return subs


# l1 = [10, 20, 30, 40]
# print(sub_lists(l1))    	## hasilya: [[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]



##### SOAL 23 (ERATOSTHENES & PRIME NUMBERS)
# def prime_eratosthenes(n):
#     unprime_list = []
#     for i in range(2, n+1):
#         if i not in unprime_list:
#             print (i, end=" ")                       ## hasilnya: 2 3 5 7 11 13
#                 unprime_list.append(j)

# prime_eratosthenes(13)



##### SOAL 24 (GENERATE UNIQUE IDENTIFICATION)
# x = 100
# print(format(id(x), 'x'))       ## hasilnya: 7ff95d25adf0

# s = 'w3resource'
# print(format(id(s), 'x'))       ## hasilnya: 189205e8a30



##### SOAL 25 (GANTI TIAP Nth VALUE)
# from itertools import zip_longest, chain, tee
# def replace2copy(lst):
#     lst1, lst2 = tee(iter(lst), 2)
#     return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
# n = [0,1,2,3,4,5]
# print(replace2copy(n))          ## hasilnya: [1, 0, 3, 2, 5, 4]



##### SOAL 26 (SORT BERDASARKAN HURUF PERTAMA)
# from itertools import groupby
# from operator import itemgetter

# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)
##HASILNYA:
# a                                                                                                             
# ask                                                                                                           
# b                                                                                                             
# be                                                                                                            
# c                                                                                                             
# call                                                                                                          
# come                                                                                                          
# d                                                                                                             
# do    



###### SOAL 27 (CREATE MULTIPLE EMPTY LISTS)
# obj = {}
# for i in range(1, 21):
#     obj[str(i)] = []
# print(obj)
# #HASILNYA
# {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20': []}



###### SOAL 28 (SPLIT LIST)
# color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
#          ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# var1, var2, var3 = color
# print(var1)     ## HASILNYA: ('Black', '#000000', 'rgb(0, 0, 0)')
# print(var2)     ## HASILNYA: ('Red', '#FF0000', 'rgb(255, 0, 0)')
# print(var3)     ## HASILNYA: ('Yellow', '#FFFF00', 'rgb(255, 255, 0)')

# mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# def list_slice(list, step):
#     return [list[i::step] for i in range(step)]
# print(list_slice(mylist,7)) HASILNYA: [['a', 'h'], ['b', 'i'], ['c', 'j'], ['d', 'k'], ['e', 'l'], ['f', 'm'], ['g', 'n']]
# print(list_slice(mylist,3)) HASILNYA: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]



##### SOAL 29 (CREATE MULTIPLE LIST WITH RANGE)
# L1 = [[j for j in range(1,6)] for i in range(5)]
# L2 = [[5*i + j for j in range(1,6)] for i in range(5)]
# print(L1)
#HASILNYA:
# [[1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5],
#  [1, 2, 3, 4, 5], 
#  [1, 2, 3, 4, 5], 
#  [1, 2, 3, 4, 5]]

# print(L2)
#HASILNYA:
[[1, 2, 3, 4, 5], 
[6, 7, 8, 9, 10], 
[11, 12, 13, 14, 15], 
[16, 17, 18, 19, 20], 
[21, 22, 23, 24, 25]]



###### SOAL 30 (INSERT ELEMENT BEFORE EACH ELEMENTT)
# color = ['Red', 'Green', 'Black']
# color = [i for j in color for i in ('c', j)]
# print(color)    ## HASILNYA: ['c', 'Red', 'c', 'Green', 'c', 'Black']



#### SOAL 31 (SIMPLE STATISTICS)
### Finding the minimum value in a list
# nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
# num_min = min(nums)
# print(num_min)                                   ## HASILNYA: 1
### Finding the maximum value
# nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
# num_max = max(nums)
# print(num_max)                                   ## HASILNYA: 82
### Finding the sum of all numbers
# nums = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]
# total_num = sum(nums)
# print(total_num)                                 ## HASILNYA: 388



###### SOAL 32 (SIMPLE LIST INSERTING & REMOVING)
# colors = ['Red', 'Blue', 'Green', 'Black', 'White']

### Changing an element
# colors[0] = 'Yellow'
# colors[-2] = 'Red'
# print(colors)                       ## HASILNYA: ['Yellow', 'Blue', 'Green', 'Red', 'White']

### Inserting elements at a particular position
# colors.insert(0, 'Violet')
# colors.insert(2, 'Purple')
# print(colors)                       ## HASILNYA: ['Violet', 'Yellow', 'Purple', 'Blue', 'Green', 'Red', 'White']


### Deleting an element by its position
# del colors[-1]
# print(colors)                       ## HASILNYA: ['Violet', 'Yellow', 'Purple', 'Blue', 'Green', 'Red']
### Removing an item by its value
# colors.remove('Green')
# print(colors)                       ## HASILNYA: ['Violet', 'Yellow', 'Purple', 'Blue', 'Red']

### Pop the last item from a list
# most_recent_col = colors.pop()
# print(most_recent_col)              ## HASILNYA: Red
# print(colors)                       ## HASILNYA: ['Violet', 'Yellow', 'Purple', 'Blue']
### Pop the first item in a list
# first_col = colors.pop(0)
# print(first_col)                    ## HASILNYA: Violet
# print(colors)                       ## HASILNYA: ['Yellow', 'Purple', 'Blue']

### Sort the list by alphabetical order
# colors = sorted(colors)
# print(colors)                       ## HASILNYA: ['Blue', 'Purple', 'Yellow']
# Reverse sorted list
# print(colors[::-1])                 ## HASILNYA: ['Yellow', 'Purple', 'Blue']


### SOAL UNTUK BIKIN ARRAY PER HURUF LIST
# string1 = 'qwertyuiop'
# list1 = list(filter(lambda num: len(num)<100,string1))
# print(list1)        ## HASILNYA ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']



## UNTUK MISAH STRING DAN INTEGER JADI LIST PERKATA
# d = "dhikanarendra"
# b = 100100
# d = list(d)
# b = list(str(b))
# print(d)            ## HASILNYA ['d', 'h', 'i', 'k', 'a', 'n', 'a', 'r', 'e', 'n', 'd', 'r', 'a']
# print(b)            ## HASILNYA ['1', '0', '0', '1', '0', '0']