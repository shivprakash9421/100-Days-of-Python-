x = int(input("Enter the value of x: "))

match x:
    case 30:
        print("x is 30")
    case 20:
        print("x is 20")
    case 10:
        print("x is 10")
    
    case _ if x != 80:
        print(x, "is not 80")
    case _ if x != 70:
        print(x, "is not 70")
    
    case _:
        print(x)

   
     
            