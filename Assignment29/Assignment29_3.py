import sys

def main():
    ExistingFile = sys.argv[1]
    NewFile = "Demo.txt"
    
    fobj1 = open(ExistingFile,"r")
    Data = fobj1.read()
    fobj1.close()
    
    fobj2 = open(NewFile , "w")
    fobj2.write(Data)
    fobj2.close()
    
    print(f"Contents of {ExistingFile} copied to {NewFile}")

if __name__ == "__main__":
    main()