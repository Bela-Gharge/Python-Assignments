def main():
    filename = input("Enter file name : ")

    fobj = open(filename , "r")

    lines = fobj.readlines()
    no_lines = len(lines)

    fobj.close()

    print("Total number of lines in ",filename,"is : ",no_lines)

if __name__ == "__main__":
    main()