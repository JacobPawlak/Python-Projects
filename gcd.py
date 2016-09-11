#Jacob Pawlak
#Euclid's Algorithm for two numbers

def main():
    #Ask for two numbers
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    #Sentinel value for Euclid's Algorithm 
    while (num2 != 0):    

        if(num1 > num2):
            num1 = (num1 - num2)
        else:
            num2 = (num2 - num1)
    #Display the GCD with some flavor
    print("The greatest common denominator is ", int(num1))        
            

main()
