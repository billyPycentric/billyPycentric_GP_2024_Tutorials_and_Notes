## Functions

def hell_world():
    print("Hello , Billy")

hell_world()

# using defalu parameters
def add_numbers(num1=0,num2=0):
    return num1+num2

add_numbers(3,5)

### adding args -> aguments
def names(*args):
    print(args)

## key-word
def names2(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i+" : " + kwargs[i])

names("Abongile" , "billy")
names2(first = "Abongile" , last = "Billy")