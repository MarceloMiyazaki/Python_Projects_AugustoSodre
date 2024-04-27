answer = "y"

while answer == "y":
    print("LET'S ADD HIM!")
    name = input("Insert your name: ")
    age = input("Now, insert your age: ")
    employee_file = open("employee.txt", "r")
    if employee_file.read() == "":
        employee_file = open("employee.txt", "a")
        employee_file.writelines(name + " " + age)    
    else:
        employee_file = open("employee.txt", "a")
        employee_file.writelines("\n" + name + " " + age)
    employee_file = open("employee.txt", "r")
    print(employee_file.readlines())
    employee_file.close()
    print(input("Would you like to add someone else?"))
