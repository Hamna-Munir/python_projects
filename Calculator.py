try:
    num_1 = int(input("Enter a first number: "))
    num_2 = int(input("Enter a second number: "))

    print("Choose calculation to perform: /n",
          "1. Add/n" ,
          "2. Subtract/n",
          "3. Multipiy/n",
          "4. Divide/n",
          )
    cal = input().strip().lower()
    
    if cal == "add":
        ans = num_1 + num_2
    elif cal =="subtract":
        ans = num_1 - num_2
    elif cal == "multipy":
        ans = num_1*num_2
    elif cal == "divide":
        if num_2==0:
            print("Error! Can't divide by zero.")
            ans = None
        else:
            ans = num_1 / num_2 
    else:
        print("Invalid Opertation!")
        ans = None

    if ans is not None:
        print(F"The Answer is {ans}")
except ValueError:
    print("Invalid input! Please enter valid number!")