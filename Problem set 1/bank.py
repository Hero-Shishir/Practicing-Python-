def main() :
    greeting = input("enter the greeting ")
    if case(greeting).startswith("hello") :
        print("$0")
    elif case(greeting).startswith("h"):
        print("$20")
    else :
        print("$100")

def case(n) :
    return n.lower().lstrip()

main()