print("Welcome to Metal Weight Calculator")
print("Please follow the instructions : ")
l = float(input("Enter the length in mm :"))
b = float(input("Enter the width in mm :"))
t = float(input("Enter the thickness in mm :"))
u = int(input("Enter unit/s :"))
print("Enter 0 : for copper")
print("Enter 1 : for mildsteel")
print("Enter 2 : for aluminium")
x = int(input("Enter selection : "))


def metals(x):
    switcher = {
        0: 'copper',

        1: 'mildsteel',

        2: 'aluminium'
    }
    return switcher.get(x, "Invalid Input")


if (metals(x)) == "copper":
    c = 8960
    w = (l / 1000 * b / 1000 * t * c / 1000 * u)
    print("weight", w, "kg.")
if (metals(x)) == "mildsteel":
    c = 8050
    w = (l / 1000 * b / 1000 * t * c / 1000 * u)
    print("weight", w, "kg.")
if (metals(x)) == "aluminium":
    c = 2600
    w = (l / 1000 * b / 1000 * t * c / 1000 * u)
    print("weight", w, "kg.")
else:
    print("Invalid Input !!! ")
