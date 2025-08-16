import time
RESULT = 0
addition = False
subtraction = False
multiplication = False
division = False
exponent = False
squareroot = False
triginometry = False
pytm = False
pyth = False
pyta = False
pytb = False
opmsg = "Enter an operation"
mmmsg = "ADD = Addition\nSUB = Subtraction\nMUL = Multiplication\nDIV = Division\nEXP = Exponent/Power Of\nSQRT = Square Root"
def add(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a + b
    print(f"{a}+{b}={RESULT}")
    
def sub(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a - b
    print(f"{a}-{b}={RESULT}")
    
def mul(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a * b
    print(f"{a}x{b}={RESULT}")
    
def div(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a / b
    print(f"{a}÷{b}={RESULT}")
    
def exp(b, p):
    global RESULT
    b = float(b)
    p = float(p)
    RESULT = b ** p
    print(f"{b}^{p}={RESULT}")
    
def sqrt(n):
    global RESULT
    n = float(n)
    RESULT = n ** 0.5
    print(f"Square root of {n} is {RESULT}")
    
time.sleep(1)
print("Welcome to my virtual calculator")   

while True:
    time.sleep(1)
    print("Enter certain short-hands to start an operation")
    time.sleep(1)
    print("Type EXIT to shut down this program")
    time.sleep(0.5)
    print(mmmsg)
    time.sleep(2)
    operation = input(opmsg).strip().upper()
            
    if operation == "ADD":
        addition = True
        time.sleep(0.5)
        print(" ")
        print("Entered Addition Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while addition:
            adda = input("Enter the number to add to").strip().upper()
            if adda == "BACK":
                operation = " "
                addition = False
                print(" ")
                break
            time.sleep(0.5)
            addb = input("Enter how much you want to add").strip().upper()
            if addb == "BACK":
                operation = " "
                addition = False
                print(" ")
                break
            time.sleep(0.5)
            add(adda, addb)
    elif operation == "SUB":
        subtraction = True
        time.sleep(0.5)
        print(" ")
        print("Entered Subtraction Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while subtraction:
            suba = input("Enter the number to subtract from").strip().upper()
            if suba == "BACK":
                operation = " "
                subtraction = False
                print(" ")
                break
            time.sleep(0.5)
            subb = input("Enter how much you want to subtract").strip().upper()
            if subb == "BACK":
                operation = " "
                subtraction = False
                print(" ")
                break
            time.sleep(0.5)
            sub(suba, subb)
    elif operation == "MUL":
        multiplication = True
        time.sleep(0.5)
        print(" ")
        print("Entered Multiplication Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while multiplication:
            mula = input("Enter the number to multiply").strip().upper()
            if mula == "BACK":
                operation = " "
                multiplication = False
                print(" ")
                break
            time.sleep(0.5)
            mulb = input("Enter how much you want to multiply by").strip().upper()
            if mulb == "BACK":
                operation = " "
                multiplication = False
                print(" ")
                break
            time.sleep(0.5)
            mul(mula, mulb)
    elif operation == "DIV":
        division = True
        time.sleep(0.5)
        print(" ")
        print("Entered Division Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while division:
            diva = input("Enter the number to divide").strip().upper()
            if diva == "BACK":
                operation = " "
                division = False
                print(" ")
                break
            time.sleep(0.5)
            divb = input("Enter how much you want to divide by").strip().upper()
            if divb == "BACK":
                operation = " "
                division = False
                print(" ")
                break
            time.sleep(0.5)
            div(diva, divb)
    elif operation == "EXP":
        exponent = True
        time.slep(0.5)
        print(" ")
        print("Entered Exponent Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while exponent:
            expb = input("Enter the base number").strip().upper()
            if expb == "BACK":
                operation = " "
                exponent = False
                print(" ")
                break
            time.sleep(0.5)
            expp = input("Enter the exponent number").strip().upper()
            if expp == "BACK":
                operation = " "
                exponent = False
                print(" ")
                break
            time.sleep(0.5)
            exp(expb, expp)
    elif operation == "SQRT":
        squareroot = True
        time.sleep(0.5)
        print(" ")
        print("Entered Square Root Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while squareroot:
            sqrtn = input("Enter the base number").strip().upper()
            if sqrtn == "BACK":
                operation = " "
                squareroot = False
                print(" ")
                break
            time.sleep(0.5)
            sqrt(sqrtn)
    elif operation == "EXIT":
        print(" ")
        print("Exiting Host Environment")
        time.sleep(2)
        exit()
