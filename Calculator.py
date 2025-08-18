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
mmmsg = "--------------------------\nADD = Addition\nSUB = Subtraction\nMUL = Multiplication\nDIV = Division\nEXP = Exponent/Power Of\nSQRT = Square Root\nTRIG = Triginometry Mode\n--------------------------"
def add(a, b):
    global RESULT
    try:
        a = float(a)
    except ValueError:
        print("Please enter a valid number input for value A")
    try:
        b = float(b)
    except ValueError:
        print("Please enter a valid number input for value B")
        return
        
    RESULT = a + b
    print(f"{a}+{b}={RESULT}")
    
def sub(a, b):
    global RESULT
    try:
        a = float(a)
    except ValueError:
        print("Please enter a valid number input for value A")
    try:
        b = float(b)
    except ValueError:
        print("Please enter a valid number input for value B")
        return
    RESULT = a - b
    print(f"{a}-{b}={RESULT}")
    
def mul(a, b):
    global RESULT
    try:
        a = float(a)
    except ValueError:
        print("Please enter a valid number input for value A")
    try:
        b = float(b)
    except ValueError:
        print("Please enter a valid number input for value B")
        return
    RESULT = a * b
    print(f"{a}x{b}={RESULT}")
    
def div(a, b):
    global RESULT
    try:
        a = float(a)
    except ValueError:
        print("Please enter a valid number input for value A")
    try:
        b = float(b)
    except ValueError:
        print("Please enter a valid number input for value B")
        return
    RESULT = a / b
    print(f"{a}÷{b}={RESULT}")
    
def exp(b, p):
    global RESULT
    try:
        b = float(b)
    except ValueError:
        print("Please enter a valid number input for value B")
    try:
        p = float(p)
    except ValueError:
        print("Please enter a valid number input for value P")
        return
    RESULT = b ** p
    print(f"{b}^{p}={RESULT}")
    
def sqrt(n):
    global RESULT
    try:
        n = float(n)
    except ValueError:
        print("Please enter a valid number input for value N")
        return
    RESULT = n ** 0.5
    print(f"Square root of {n} is {RESULT}")
    
time.sleep(1)
print("Welcome to my virtual calculator")   

while True:
    time.sleep(1)
    print("--------------------------\nEnter certain short-hands to start an operation")
    time.sleep(1)
    print("Type EXIT to shut down this program")
    time.sleep(1)
    print(mmmsg)
    time.sleep(2)
    operation = input(opmsg).strip().upper()
            
    if operation == "ADD":
        addition = True
        time.sleep(0.5)
        print("--------------------------\nEntered Addition Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while addition:
            adda = input("\nEnter the number to add to").strip().upper()
            if adda == "BACK":
                operation = " "
                addition = False
                break
            time.sleep(0.5)
            addb = input("Enter how much you want to add").strip().upper()
            if addb == "BACK":
                operation = " "
                addition = False
                break
            time.sleep(0.5)
            add(adda, addb)
    elif operation == "SUB":
        subtraction = True
        time.sleep(0.5)
        print("--------------------------\nEntered Subtraction Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while subtraction:
            suba = input("\nEnter the number to subtract from").strip().upper()
            if suba == "BACK":
                operation = " "
                subtraction = False
                break
            time.sleep(0.5)
            subb = input("Enter how much you want to subtract").strip().upper()
            if subb == "BACK":
                operation = " "
                subtraction = False
                break
            time.sleep(0.5)
            sub(suba, subb)
    elif operation == "MUL":
        multiplication = True
        time.sleep(0.5)
        print("--------------------------\nEntered Multiplication Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        time.sleep(0.5)
        while multiplication:
            mula = input("\nEnter the number to multiply").strip().upper()
            if mula == "BACK":
                operation = " "
                multiplication = False
                break
            time.sleep(0.5)
            mulb = input("Enter how much you want to multiply by").strip().upper()
            if mulb == "BACK":
                operation = " "
                multiplication = False
                break
            time.sleep(0.5)
            mul(mula, mulb)
    elif operation == "DIV":
        division = True
        time.sleep(0.5)
        print("--------------------------\nEntered Division Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while division:
            diva = input("\nEnter the number to divide").strip().upper()
            if diva == "BACK":
                operation = " "
                division = False
                break
            time.sleep(0.5)
            divb = input("Enter how much you want to divide by").strip().upper()
            if divb == "BACK":
                operation = " "
                division = False
                break
            time.sleep(0.5)
            div(diva, divb)
    elif operation == "EXP":
        exponent = True
        time.sleep(0.5)
        print("--------------------------\nEntered Exponent Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while exponent:
            expb = input("Enter the base number").strip().upper()
            if expb == "BACK":
                operation = " "
                exponent = False
                break
            time.sleep(0.5)
            expp = input("Enter the exponent number").strip().upper()
            if expp == "BACK":
                operation = " "
                exponent = False
                break
            time.sleep(0.5)
            exp(expb, expp)
    elif operation == "SQRT":
        squareroot = True
        time.sleep(0.5)
        print("--------------------------\nEntered Square Root Mode")
        time.sleep(0.5)
        print("Type BACK to exit this mode")
        while squareroot:
            sqrtn = input("\nEnter the base number").strip().upper()
            if sqrtn == "BACK":
                operation = " "
                squareroot = False
                break
            time.sleep(0.5)
            sqrt(sqrtn)
    elif operation == "EXIT":
        print("\nExiting Host Environment")
        time.sleep(2)
        exit()
