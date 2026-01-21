
num = int(input("Enter a number: "))


shift = int(input("Enter number of positions to shift: "))


left_shift = num << shift
print(f"{num} << {shift} = {left_shift}")


right_shift = num >> shift
print(f"{num} >> {shift} = {right_shift}")
