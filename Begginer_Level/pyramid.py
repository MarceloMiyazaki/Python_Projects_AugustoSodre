space = " "
mark = "*"
total_rows : int
space_count : int
row_count = 1
row_str = ""

print("-------------------------")
print("PYRAMID GENERATOR")
total_rows = int(input("How many rows will your pyramid have? "))
space_count = total_rows

def generate_pyramid(t_rows, s_count, r_count):
    for i in range(t_rows):
        row_str = ""
        for n in range(s_count):
            row_str = row_str + space
        s_count = s_count - 1
        for m in range(r_count):
            row_str = row_str + mark
        r_count = r_count + 2
        print(row_str)

generate_pyramid(total_rows, space_count, row_count)

print("-------------------------")