### AlL ABout formating Strings

person = "Billy"
coins = 3
player = {
    "person" : "Billy",
    "coins" : 7
}
message = "\n%s has %s coins left ."%(person,coins)
print(message)


message2 = "\n{} has {} coins left.".format(person,coins)
print(message2)

message3 = "\n{1} has {0} coins left.".format(person,coins)
print(message3)

message5 = "\n{person} has {coins} coins left.".format(**player)
print(message5)

message4 = "\n{person} has {coins} coins left.".format(
    coins=person,person=coins
    )
print(message4)

############################ F Strings #############################
about = {
    "name" : "Abongile",
    "Surname":"Billy" , 
    "Varsity": {
        "Name" : "North West University",
        "Course" : "BSc Computer Science And Economics"
        },
    "Profession": "Software Development Engineer",
    "Experince":" Less than A Year",
    "Coding Languages":{
        "Backend" :{
            "Languages" : "Python , Java",
            "Frame-Works" : "FastAPI , Spring"
        },
        "Web" : "HTML , javascript , typescript"

    },
    "Married" : False 
}
about_message = f""" Hi my name is {about['name']} {about['Surname']} and i am {str(25) + " years old (Dont know why i fogot to mention that)"} , 
I attended {about['Varsity']["Name"]} did the course {about['Varsity']["Course"]}  i am a {about['Profession']} currently have {about['Experince']} 
and i know these languages : {about['Coding Languages']['Backend']["Languages"]} for back end with framworks {about['Coding Languages']['Backend']["Frame-Works"]}

"""

print(about_message)
