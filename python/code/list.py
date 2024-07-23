import sys

my_tuple = (1,2,3,4,5,3,3,2,4,5,6)
(one ,two , *three , four) = my_tuple

print(one)
print(two)
print(three)
print(four)
mylist = three

#print(mylist)
sys.exit()
users = ['1' , '2 ' , '3' , '4']

print(users)
print(len(users))
users.append("8")
print(users)

users[2:2] = ['9', '11']
print(users)

users[4:5] = ['14', '54 '  , '35']
print(users)


print(users.sort())