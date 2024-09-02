proStart = int(input('''Let's make table, Are you ready?
    1. Yes
    2. No
    : '''))

history = set({})

if proStart == 1:
    while True:
        usrInp = int(input('''Welcome Select Option 
        1. Making a table
        2. Check Table history
        3. Access Specific table from history
        4. Exit
        : '''))

        if usrInp == 1:
            tabNum = int(input("Enter a num You Want A Table: "))
            tabLen = int(input("Enter a table length: "))
            tabLen +=1
            history.add(tabNum)
            for i in range(1, tabLen):
                table = tabNum * i
                print(tabNum, " x ", i, " = ", table)
                save = open(f"History/{tabNum}.txt","a")
                save.write(f"\n{tabNum} x {i} = {table}\n")
        elif usrInp == 2:
            print("Table History: ")
            print(history)
        elif usrInp == 3:
            getNum = int(input("Enter a table num you want to access: "))
            print("Table History of ", getNum, " is: ")
            save = open(f"History/{getNum}.txt","r")
            print(save.read())
        elif usrInp == 4:
            print("Thanks for Using, I hope You Enjoyed it, Bye")
            break
        else:
            print("Please Select Correct Option. Thanks!")
    
elif proStart == 2:
    print("I hope you came as soon as posible")
else:
    print("Please Select Correct Option. Thanks!")