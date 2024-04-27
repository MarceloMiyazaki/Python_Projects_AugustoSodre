from random import randrange

#T-shirts section
patterned_shirts = ["Dark_Red", "Road", "Black_Squares", "Military", "Brownie", "Harsh_Blue", "Dark_Blue", "Brooksfield_Blue", "Zebra", "Yellow"]
plain_shirts = ["Pink", "White", "Dark_Green","Light_Green", "Dark_Gray", "Dark_Blue", "Black", "Red"]
t_shirts = [patterned_shirts , plain_shirts]
t_shirt_message : str

def shirt_selector():
    a = randrange(0,2)
    b : int

    match a:
        case 0:
            t_shirt_message = "Patterned Shirt: "
            b = randrange(0,9)
        case 1:
            t_shirt_message = "Plain Shirt: "
            b = randrange(0,7)
    
    return [t_shirt_message , t_shirts[a][b]]

shirt_result = shirt_selector()


#UI question section
print("======================================")
print("W A R D R O B E")
print("Ohayo Master, would you like to wear shorts? [y/n]")
answer = input(str)
print("======================================")


#Shorts/Pants section
pants = ["Light_Jeans", "Dark_Jeans", "Black_Jeans", "Beige"]
shorts = ["Dark_Blue", "Beige"]
pants_message : str

def pants_selector():
    c : int
    if (answer == "n"):
        c = randrange(0,3)
        pants_message = "Pants: "
        return [pants_message , pants[c]]
        
        
    else:
        c = randrange(0,2)
        pants_message = "Shorts: "
        return [pants_message , shorts[c]]

pants_result = pants_selector()   


#Sneakers section
pants_sneakers  = ["White_Nike", "Green_Vans", "Blue_Vans", "Black_Vans", "New_Balance", "Beige_Aramis"]
shorts_sneakers = ["Blue_Sergios", "Green_Vans", "Blue_Vans", "Black_Vans", "Beige_Aramis"]
sneakers_message : str

def sneakers_selector():
    d : int
    if (answer == "n"):
        d = randrange(0,5)
        sneakers_message = "Sneakers: "
        return [sneakers_message , pants_sneakers[d] ]
        
    else:
        d = randrange(0,4)
        sneakers_message = "Sneakers: "
        return [sneakers_message , shorts_sneakers[d]]

sneakers_result = sneakers_selector()

#UI result section

def result_ui():
    print("")
    print("======================================")
    print("R E S U L T")
    print("")
    print(shirt_result[0] + shirt_result[1])
    print(pants_result[0] + pants_result[1])
    print(sneakers_result[0] + sneakers_result[1])
    print("======================================")

result_ui()
last_answer = ""
while (last_answer != "n"):
    print("Would you like to change something? [shirt/pants/sneakers/n] ")
    last_answer = input(str)
    match last_answer:
        case ("shirt"):
            shirt_result = shirt_selector()
            result_ui()
        case ("pants"):
            pants_result = pants_selector()
            result_ui()
        case ("sneakers"):
            sneakers_result = sneakers_selector()
            result_ui()