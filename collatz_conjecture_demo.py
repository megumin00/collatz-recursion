#gets user input to value n
n = int(input("Enter your base value: "))

breakToggle = False
breakCounter = 0
n_list = []

#loops until the last three values are 4, 2 and 1
while True:
    n_list.append(n)

    #if the remainder of n/2 is equals to 0 (even output), n is divided by 2. If it is not even, it multiplies by 3 and then adds 1 to itself
    if (n % 2) == 0:
        if n == 4:
            breakToggle = True

        n = n/2


    else: 
        n = 3*n+1

    #sets n to a integer to prevent floating point values
    n = int(n)

    if breakToggle == True:
        breakCounter += 1

    if breakCounter == 4:
        break

#checks the last three values of n_list if they are 4, 2 or 1 and if they all are, check is set to true
check = True

for i in range(3):
    if n_list[-(i+1)] in [4, 2, 1]:
        pass
    else:
        check = False

print(f"{n_list}, ending in 4, 2 and 1 is {check}")
