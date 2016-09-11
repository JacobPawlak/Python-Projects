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
