try:
    answer = 0/10
    num = int(input("Enter your number : "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")  