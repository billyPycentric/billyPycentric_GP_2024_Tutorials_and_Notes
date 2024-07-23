### Recursion

##### How to Structure a Recursive Func
## Usually have two statements 
## 1 Statemennt that Breaks the Func
## Statemeent that re-Calls the func
## always start withh what is true



def add_one(num):
    if (num  > 9):
        return num+1
    total = num+1
    add_one(total)
    print(total)
    

add_one(0)

# def subtract_one(num):
#     if(num <= 1):
#         return num -1
#     total = num-1
#     print(total)
#     return subtract_one(total)

# subtract_one(11)

# def walk(steps):
#     if steps ==0:
#         return
    
#     steps-=1
#     walk(steps)
#     print(steps)

# walk(22)