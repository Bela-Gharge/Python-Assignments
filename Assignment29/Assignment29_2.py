def main():
    filename = input("Enter file name : ")
    
    fobj = open(filename , "r")
    
    Data = fobj.read()

    print(Data)

if __name__ == "__main__":
    main()