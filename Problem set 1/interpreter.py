def main() :
    expression = input("Expression: ")
    x , y, z = expression.split(" ")
    x= integer_x(x)
    z= integer_z(z)
    if y.startswith("+"):
        a = (x+z)
        print (f"{a:.1f}")
    elif y.startswith("-"):
        b = (x-z)
        print (f"{b:.1f}") 
    elif y.startswith("*"):
        c = (x*z)
        print (f"{c:.1f}")
    elif y.startswith("/"):
        d = (x/z)
        print (f"{d:.1f}")

def integer_x(m) :
    return int (m)

def integer_z(n) :
    return int (n)
main ()