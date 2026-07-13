def main():
    emoji = input ("enter the input " )
    print (convert(emoji))


def convert(x):
    return x.replace(":)" ,"🙂").replace(":(" ,"🙁")

main()