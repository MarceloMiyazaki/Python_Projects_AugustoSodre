name = input("Give me your full name: ")
print("Your name in uppercase is " + name.upper())
print("Your name in lowercase is " + name.lower())
count = 0
for i in name:
    if i != " ":
        count += 1
print(f"Your full name has {count} characters")
first_name = ""
first_name_count = 0
passed_first_space = False
for c in name:
    if c != " ":
        if passed_first_space == False:
            first_name += c
    else:
        passed_first_space = True

for x in first_name:
    first_name_count += 1

print(f"Your first name is {first_name} and it has {first_name_count} characters")