#muhammed muhammedbeshir abdulaziz question no-2
repeat=("r")
while True:
    if repeat==("r"):
        import math
        pi=math.pi
        choose=input("which volume of the prism,cone or sphere would you like to calculate ").lower()
        if choose==("sphere"):
            r=float(input("enter the radius in meters"))
            print((4/3)*pi*r**3,"m^3")
        elif choose==("cone"):
            h=float(input("please enter the hieght in meters"))
            r=float(input("enter the radius"))
            print(pi*r**2*(h/3),"m^3")
        elif choose==("prism"):
            base=float(input("please enter the base area in meters"))
            h=float(input("please enter the hieght in meters"))
            print(base*h,"m^3")
    repeat=input("Do you want to quit or perform another operation(please enter 'r'for repeat and 'q' for quit):").lower()
    if repeat==("q"):
        break
