import threading

Count = 0
lock = threading.Lock()


def Add():
    global Count
    for i in range(5):
        lock.acquire()
        Count = Count + 1
        lock.release()

def main():
    t1 = threading.Thread(target=Add)
    t2 = threading.Thread(target=Add)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final count : ",Count)

if __name__ == "__main__":
    main()