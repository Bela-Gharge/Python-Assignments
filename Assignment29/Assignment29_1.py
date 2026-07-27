import os

def main():
    FileName = input("Enter File Name : ")

    if os.path.exists(FileName):
        print(f"{FileName} exists in given directory")
    else :
        print(f"{FileName} not found in given directory ")    

if __name__ == "__main__":
    main()