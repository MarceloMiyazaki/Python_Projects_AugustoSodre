from random import randint

print(23 * "-")
print("Dice Calculator!")
dice_total_number :int = input("How many faces does your dice has? ")
dice_actual_number = randint(1, int(dice_total_number))
print("Your number will be " + str(dice_actual_number))
