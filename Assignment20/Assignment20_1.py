import threading

def Even():
    for i in range(2,22,2):
        print(i)

def Odd():
    for i in range(1,21,2):
        print(i)

def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()