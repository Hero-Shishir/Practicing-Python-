name = input("enter the name ")

match name:
    case  "shishir" | "binod" :
        print("Red")
    case  "arjun" :
        print("green")
    case "sudip" :
        print("blue")
    case  "suman" :
        print("yellow")
    case _ :
        print("who")