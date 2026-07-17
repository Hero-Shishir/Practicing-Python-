def main () :
    x = input("file name :")
    if file_name(x).endswith((".jpg" , ".jpeg")):
        print("image/jpeg")
    elif file_name(x).endswith(".pdf"):
        print("application/pdf")
    elif file_name(x).endswith(".gif"):
        print("image/gif")
    elif file_name(x).endswith(".png"):
        print("image/png")
    elif file_name(x).endswith(".txt"):
        print("text/txt")
    else:
        print("application/octet-stream")
    
def file_name(n) :
    return n.strip().lower()

main()