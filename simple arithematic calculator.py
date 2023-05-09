#muhammed muhammedbeshir abdulaziz question no 0
repeat=("r")
while True:
    if repeat==("r"):
        first=int(input("please enter the first number"))
        ope=input("please enter the operator")
        second=int(input("please enter the second number"))
        if ope==("+"):
            print(first+second)
        elif ope==("-"):
            print(first-second)
        elif ope==("/"):
            print(first/second)
        elif ope==("*"):
            print(first*second)
        elif ope==("^"):
            print(first**second)
    repeat=input("Do you want to quit or perform another operation(please enter 'r'for repeat and 'q' for quit):").lower()
    if repeat==("q"):
            break
    

    
        
            

