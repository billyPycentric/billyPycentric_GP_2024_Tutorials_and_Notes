# from functools import reduce 

# ### learning about lambda expressions

# add_numbers = lambda a,b : a+b
#  ## Higher Order functions

# numbers = [1,2,3,4,5,6,7,8,9]

# odd_nums = filter(lambda num : num%2 != 0 , numbers)

# square_numbers = map(lambda num:num*num ,numbers)

# ### returning even numbers

# my_list = [1,2,3,4,5,6,7,8,9,0,5,4,6,8,6,4,55,88,65,33,5,8,6,4,44,44,3,2,2]
# even_num = filter(lambda num:num%2 ==0,my_list)
# print(list(even_num))



# #### higher Order functions
# print("Higher Order Functions")
# total_sum = reduce(lambda acc,curr : acc + curr,[1,5,1,3,4])

# print("Here is the list  " + str([1,5,1,3,4])+ "\n"+str(total_sum))

# my_paragraphs = ["My name is Abongile Billy"," and i am 24 years Old","i am a software Engineer"," and i work at at start up"]
# char_count = reduce(lambda acc ,curr:len(curr) + acc  ,my_paragraphs,0)

# print(char_count)


def func_builder(a):
    return lambda b:a**b


square = func_builder(3)
print(square(2))