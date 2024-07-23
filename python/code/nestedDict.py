### Dictionaries

## Normal dictionaries
work_pc = {
    "PyCetric001" : "Abongile" ,
    "PyCetric002" : "Kanyi" ,
    "PyCetric003" : "Ifalanga" ,
    "PyCetric004" : "Vhutali"
  
 }

## displaying the work_pc dict
print(work_pc)

## displaying keys
print(work_pc.keys())

## displaying values
print(work_pc.values())

## dislpay sigle value
print(work_pc["PyCetric001"])

## ### Using a loop to traverse the dictionary
for i in work_pc.keys():
    print(i + ": " + work_pc[i])


#######################################################################
print("                               ")    
print("                               ")    
print("                               ")    
print("                              ")    
print("           NESTED                    ")

gym_members = {

}

member1 = {
    "Name":"Abongile" ,
    "Surname":"Billy" ,
    "Location":"VAAL" ,
}
member2 = {
    "Name":"Khanyi" ,
    "Surname":"LongSurname" ,
    "Location":"Pretoria" ,
}
member3 = {
    "Name":"Ifalanga" ,
    "Surname":"ForgotSurname" ,
    "Location":"JHB" ,
}
gym_members = {
    "Member 1" :member1 ,
    "Member 2" :member2 ,
    "Member 3" :member3 ,
}

# print(gym_members)

for member in gym_members:
    print(member + ": " + str(gym_members[member]))
















