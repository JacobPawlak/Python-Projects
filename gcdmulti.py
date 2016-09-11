#Jacob Pawlak
#Euclid's Algorithm with three numbers
def main():
    #Asks for three numbers
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))    
    num3 = float(input("Enter number 3: "))

    #Sentinel Value for Euclid's Algorithm 
    while (num2 != 0):

        if(num1 > num2):
            num1 = (num1 - num2)
        else:
            num2 = (num2 - num1)

    #num1 is now greater than b where b = 0

    #Same sentinel value used above
    while (num3 != 0):

        if(num1 > num3):
            num1 = (num1 - num3)
        else:
            num3 = (num3 - num1)

    #num2 and num3 are now 0 and num1 is the GCD

    print("The GCD of the three is ", int(num1))

    input()

main()
