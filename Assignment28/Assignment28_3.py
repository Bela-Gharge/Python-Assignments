def main():
    filename = input("Enter filename : ")
    fobj = open(filename ,"r")

    Data = fobj.readlines()
    for line in Data:
        print(line)

    fobj.close()

    print("File Contents are : ")
    print(Data)

if __name__ == "__main__":
    main()