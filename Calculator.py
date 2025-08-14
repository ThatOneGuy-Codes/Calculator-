import time
RESULT = 0

def vui():
    print(" ")
    print("Welcome to my virtual calculator")
    time.sleep(1)
    print("Enter certain short-hands to start an operation")
    print(" ")
    time.sleep(0.5)
    print("ADD = Addition")
    time.sleep(0.5)
    print("SUB = Subtraction")
    time.sleep(0.5)
    print("MUL = Multiplication")
    time.sleep(0.5)
    print("DIV = Division")
    time.sleep(0.5)
    print("EXP = Exponent/Power Of")
    time.sleep(0.5)
    print("SQRT = Square Root")
    time.sleep(0.5)
    print("EXIT = Exit the program")
    time.sleep(2)
    operation = input("Choose an operation").strip().upper()
    if operation == "ADD":
        addui1()
    elif operation == "SUB":
        subui1()
    elif operation == "MUL":
        multui1()
    elif operation == "DIV":
        divui1()
    elif operation == "EXP":
        expui1()
    elif operation == "SQRT":
        sqrtui1()
    elif operation == "EXIT":
        print("Exiting...")
        time.sleep(2)
        print("Successfully exited host environment")
        exit()
        
def vui2():
    print(" ")
    print("Enter certain short-hands to start an operation")
    print(" ")
    time.sleep(0.5)
    print("ADD = Addition")
    time.sleep(0.5)
    print("SUB = Subtraction")
    time.sleep(0.5)
    print("MUL = Multiplication")
    time.sleep(0.5)
    print("DIV = Division")
    time.sleep(0.5)
    print("EXP = Exponent/Power Of")
    time.sleep(0.5)
    print("SQRT = Square Root")
    time.sleep(0.5)
    print("EXIT = Exit the program")
    time.sleep(2)
    operation = input("Choose an operation").strip().upper()
    if operation == "ADD":
        addui1()
    elif operation == "SUB":
        subui1()
    elif operation == "MUL":
        multui1()
    elif operation == "DIV":
        divui1()
    elif operation == "EXP":
        expui1()
    elif operation == "SQRT":
        sqrtui1()
    elif operation == "EXIT":
        print("Exiting...")
        time.sleep(2)
        print("Successfully exited host environment")
        exit()

def add(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a + b
    print(f"{a}+{b} = {RESULT}")
    addui2()
    
def addui1():
    time.sleep(1)
    print(" ")
    print("Entered addition mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    adda = input("Write the number to add to").strip().upper()
    if adda == "BACK":
        vui2()
    time.sleep(1)
    addb = input("Write how much you want to add").strip().upper()
    if addb == "BACK":
        vui2()
    time.sleep(0.5)
    add(adda, addb)
    
def addui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    adda = input("Write the number to add to").strip().upper()
    if adda == "BACK":
        vui2()
    time.sleep(1)
    addb = input("Write how much you want to add").strip()
    if addb == "BACK":
        vui2()
    time.sleep(0.5)
    add(adda, addb)

def sub(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a - b
    print(f"{a}-{b} = {RESULT}")
    subui2()
    
def subui1():
    time.sleep(1)
    print(" ")
    print("Entered subtraction mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    suba = input("Write the number to subtract from").strip().upper()
    if suba == "BACK":
        vui2()
    time.sleep(1)
    subb = input("Write how much you want to subtract").strip().upper()
    if subb == "BACK":
        vui2()
    time.sleep(0.5)
    sub(suba, subb)
    
def subui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    suba = input("Write the number to subtract from").strip().upper()
    if suba == "BACK":
        vui2()
    time.sleep(1)
    subb = input("Write how much you want to subtract").strip().upper()
    if subb == "BACK":
        vui2()
    time.sleep(0.5)
    sub(suba, subb)
    
def mult(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a * b
    print(f"{a}x{b} = {RESULT}")
    multui2()
    
def multui1():
    time.sleep(1)
    print(" ")
    print("Entered multiplication mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    multa = input("Write the number to multiply").strip().upper()
    if multa == "BACK":
        vui2()
    time.sleep(1)
    multb = input("Write how much you want to multiply by")
    if multb == "BACK":
        vui2()
    time.sleep(0.5)
    mult(multa, multb)
    
def multui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    multa = input("Write the number to multiply").strip().upper()
    if multa == "BACK":
        vui2()
    time.sleep(1)
    multb = input("Write how much you want to multiply by")
    if multb == "BACK":
        vui2()
    time.sleep(0.5)
    mult(multa, multb)
    
def div(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a / b
    print(f"{a}÷{b} = {RESULT}")
    divui2()
    
def divui1():
    time.sleep(1)
    print(" ")
    print("Entered division mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    diva = input("Write the number to divide").strip().upper()
    if diva == "BACK":
        vui2()
    time.sleep(0.5)
    divb = input("Write how much you want to divide by")
    if divb == "BACK":
        vui2()
    time.sleep(0.5)
    div(diva, divb)
    
def divui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    diva = input("Write the number to divide").strip().upper()
    if diva == "BACK":
        vui2()
    time.sleep(0.5)
    divb = input("Write how much you want to divide by")
    if divb == "BACK":
        vui2()
    time.sleep(0.5)
    div(diva, divb)

def exp(a, b):
    global RESULT
    a = float(a)
    b = float(b)
    RESULT = a ** b
    print(f"{a}^{b} = {RESULT}")
    expui2()
    
def expui1():
    time.sleep(1)
    print(" ")
    print("Entered exponent mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    expa = input("Write the base number").strip().upper()
    if expa == "BACK":
        vui2()
    time.sleep(0.5)
    expb = input("Write the exponent number")
    if expb == "BACK":
        vui2()
    time.sleep(0.5)
    exp(expa, expb)
    
def expui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    expa = input("Write the base number").strip().upper()
    if expa == "BACK":
        vui2()
    time.sleep(0.5)
    expb = input("Write the exponent number")
    if expb == "BACK":
        vui2()
    time.sleep(0.5)
    exp(expa, expb)
    
def sqrt(num):
    global RESULT
    num = float(num)
    RESULT = num ** 0.5
    print(f"Square root of {num} is {RESULT}")
    sqrtui2()

def sqrtui1():
    time.sleep(1)
    print(" ")
    print("Entered square root mode")
    time.sleep(0.5)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    sqrtnum = input("Write the base number").strip().upper()
    if sqrtnum == "BACK":
        vui2()
    time.sleep(0.5)
    sqrt(sqrtnum)
    
def sqrtui2():
    time.sleep(1)
    print("Type BACK to exit this mode")
    time.sleep(0.5)
    sqrtnum = input("Write the base number").strip().upper()
    if sqrtnum == "BACK":
        vui2()
    time.sleep(0.5)
    sqrt(sqrtnum)

vui()
