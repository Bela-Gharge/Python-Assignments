def main():
    filename = input("Enter file name : ")

    fobj = open(filename , "r")

    Data = fobj.read()
    words = Data.split()
    no_words = len(words)

    fobj.close()

    print("Total number of words in ",filename,"is : ",no_words)

if __name__ == "__main__":
    main()