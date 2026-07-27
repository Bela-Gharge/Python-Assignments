def main():
    FileName = input("Enter File Name : ")
    SearchWord = input("Enter the word to be searched : ")

    fobj = open(FileName , "r")
    Data = fobj.read()
    fobj.close()

    if SearchWord in Data:
        print(f"{SearchWord} found in {FileName}")
    else :
        print(f"{SearchWord} not found in {FileName}")    

if __name__ == "__main__":
    main()