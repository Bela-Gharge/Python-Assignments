def main():
    FileName = input("Enter File Name : ")
    SearchWord = input("Enter the word to be searched : ")
    
    fobj = open(FileName , "r")
    Data = fobj.read()
    fobj.close()

    Count = Data.count(SearchWord)
    
    print(f"Frequency of {SearchWord} is {Count}")
    

if __name__ == "__main__":
    main()