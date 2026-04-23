while True:
    number = int(input("Enter value b/w 1 and 10 \n"))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print('invalid number, try again')