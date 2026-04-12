# Q4 
count = 0
try:
    N = int(input())   
    
    for _ in range(N):
        a, b = input().split()
        
        try:
            result = int(a) // int(b)
            print(result)
        
        except ZeroDivisionError as e:
            print("Error Code:", e)
        
        except ValueError as e:
            print("Error Code:", e)

except Exception as e:
    print("Invalid input:", e)

    # Q5
    class FileNotFoundCustom(Exception):
        pass

class FileReadError(Exception):
    pass

try:
    filename = input("Enter file name: ")
    
    if filename != "data.txt":
        raise FileNotFoundCustom("File not found!")
    
    # Simulate reading error
    raise FileReadError("Error while reading file!")

except FileNotFoundCustom as e:
    print(e)

except FileReadError as e:
    print(e)
    # Q6

while True:
    print("Program executed")
    
    choice = input("Run again? (y/n): ")
    if choice.lower() != 'y':
        break