#muhammed muhammedbeshir abdulaziz question no-6
repeat=("r")
while True:
    if repeat==("r"):
        initial=90
        user=float(input("enter the kilometers"))
        print("the total service fee is"+str(initial+user*9))
    repeat=input("Do you want to quit or perform another operation(please enter 'r'for repeat and 'q' for quit):").lower()
    if repeat==("q"):
            break
