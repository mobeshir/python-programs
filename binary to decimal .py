#muhammed muhammedbeshir abdulaziz question no-9
repeat=("r")
while 1:
    if repeat==("r"):
        binary=(input("input a binary number"))
        dec=0
        for i in range(0,len(binary)):
            deci=binary[-(i+1)]
            if deci==("1"):
                dec=dec+(pow(2,i))
        print(dec)
    repeat=input("Do you want to quit or perform another operation(please enter 'r'for repeat and 'q' for quit):").lower()
    if repeat==("q"):
            break        

