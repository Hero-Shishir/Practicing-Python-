print ("what is the answer to the Great Question of Life, the Universe and Everything" )
def main () :
    x = input("")
    if case(x) == "forty-two" or case(x) == "forty two" or case(x) == "42"  :
        print ("Yes")
    else :
        print ("No")

def case(m) :
    return m.strip().lower()

main()