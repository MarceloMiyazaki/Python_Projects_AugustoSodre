from random import randrange

#T-shirts var section
patterned_shirts = ["Dark_Red", "Road", "Black_Squares", "Military", "Brownie", "Harsh_Blue", "Dark_Blue", "Brooksfield_Blue", "Zebra", "Yellow"]
plain_shirts = ["Pink", "White", "Dark_Green","Light_Green", "Dark_Gray", "Dark_Blue", "Black", "Red"]
t_shirts = [patterned_shirts , plain_shirts]

a = randrange(0,2)
b : int

match a:
    case 0:
        t_shirt_message = "Patterned Shirt: "
        b = randrange(0,9)
    case 1:
        t_shirt_message = "Plain Shirt: "
        b = randrange(0,7)

t_shirt_message : str
chosen_t_shirt = t_shirts[a][b]


#UI question section
print("======================================")
print("Ohayo Master, would you like to wear shorts? [y/n]")
answer = input(str)
print("======================================")

#Shorts/Pants var section
pants = ["Light_Jeans", "Dark_Jeans", "Black_Jeans", "Beige"]
shorts = ["Dark_Blue", "Beige"]
c : int
chosen_pants : str
pants_message : str


#Sneakers var section
pants_sneakers  = ["White_Nike", "Green_Vans", "Blue_Vans", "Black_Vans", "New_Balance", "Beige_Aramis"]
shorts_sneakers = ["Blue_Sergios", "Green_Vans", "Blue_Vans", "Black_Vans", "Beige_Aramis"]
d : int
chosen_sneakers : str
sneakers_message : str


#Pants Result method section
if (answer == "n"):
    c = randrange(0,3)
    chosen_pants = pants[c]
    pants_message = "Pants: "
    
else:
    c = randrange(0,2)
    chosen_pants = shorts[c]
    pants_message = "Shorts: "


#Sneakers Result method section
if (answer == "n"):
    d = randrange(0,5)
    chosen_sneakers = pants_sneakers[d]
    sneakers_message = "Sneakers: "
    
else:
    d = randrange(0,4)
    chosen_sneakers = shorts_sneakers[d]
    sneakers_message = "Sneakers: "


user_exit = False

#UI result section
def result_ui():
    print("")
    print("======================================")
    print("Wardrobe!")
    print("")
    print(t_shirt_message + chosen_t_shirt)
    print(pants_message + chosen_pants)
    print(sneakers_message + chosen_sneakers)
    print("======================================")

result_ui()
