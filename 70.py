#menu-driven calculator.
while True:       #infinite loop
    print("menu:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. modulus")
    print("6. floor division")
    print("7. exponent")
    print("8. exit")
    
    choice=int(input("enter your choice:"))
    if choice==8:
        print("exit!")
        break
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    
