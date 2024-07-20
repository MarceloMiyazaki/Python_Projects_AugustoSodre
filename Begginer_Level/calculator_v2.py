import os

def sum(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if (num2 == 0):
        print("Error - Can't divide by zero")
    else:
        return num1 / num2

def startHomeScreen():
    print("\nWhat operation are we up to?")
    result = input("\n1. Sum \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quit \n\nAnswer: ")

    match (result):
        case "1":
            os.system("cls")
            print("\nSum!\n")
            num1 = float (input("Give me first number: "))
            num2 = float(input("Give me the second numer: "))
            print("Result: " + str(sum(num1, num2)))
            startHomeScreen()
        case "2":
            os.system("cls")
            print("\nSubtraction!\n")
            num1 = float (input("Give me first number: "))
            num2 = float(input("Give me the second numer: "))
            print("Result: " + str(subtraction(num1, num2)))
            startHomeScreen()
        case "3":
            os.system("cls")
            print("\nMultiplication!\n")
            num1 = float (input("Give me first number: "))
            num2 = float(input("Give me the second numer: "))
            print("Result: " + str(multiplication(num1, num2)))
            startHomeScreen()
        case "4":
            os.system("cls")
            print("\nDivision!\n")
            num1 = float (input("Give me first number: "))
            num2 = float(input("Give me the second numer: "))
            print("Result: " + str(division(num1, num2)))
            startHomeScreen()
        case "5":
            quit(0)
        case _:
            os.system("cls")
            print("\nWrong number! Try it again!\n")
            startHomeScreen()

startHomeScreen()




    


