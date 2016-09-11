'''
Jacob Pawlak
November 18th, 2015
This is a more complete version of the creditcard validator
Fixes include: Now writing to a file without getting as memory error

'''

def validate(cardNum, fileobj):

    odds = 0
    evens = 0

    for i in range(16):

        if(i % 2 != 0):

            evens += int(cardNum[i])

        if(i % 2 == 0):

            doubleNumber = int(cardNum[i]) * 2

            if(doubleNumber >= 10):
                sdoubleNumber = str(doubleNumber)
                doubleNumber = (int(sdoubleNumber[0]) + int(sdoubleNumber[1]))

            odds += doubleNumber

    if((evens + odds) % 10 == 0):

        fileobj.write(cardNum + "\n")

    

def main():

    
    fobj = open("numbers.txt", "w") 

    #these are the values we are checking through, starting with 44304100 and 8 0's
    #4430410000000000 - 4430410099999999

    #ask the user for the range they want. validation range (1 - 10,000,000)
    rng = int(input("How many cards do you want to try? "))
    while((rng <= 0)or(rng > 100000000)):
        print("range out of bounds: Enter a range between 1 and 1000000")
        rng = int(input("How many cards do you want to try? "))

    
    for i in range(rng):
        string = ""
        n = str(i)
        string += ("0" * (8 - len(n))) + n
        cardNum = ("44304100" + string)

        validate(cardNum, fobj)

        
    print("Done!")
    fobj.close()
    print()
    input("Press ENTER to exit")
    

main()
