import threading

def Prime(data):
    Prime_Number = []

    for n in data:
        count = 0

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1

                if n // i != i:
                    count += 1

        if count == 2:
            Prime_Number.append(n)

    print("Prime Numbers :", Prime_Number)


def NonPrime(data):
    Non_Prime = []

    for n in data:
        count = 0

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1

                if n // i != i:
                    count += 1

        if count > 2:
            Non_Prime.append(n)

    print("Non Prime Numbers :", Non_Prime)


def main():
    List = []

    limit = int(input("Enter number of elements : "))

    for i in range(limit):
        val = int(input(f"Enter Number {i+1} : "))
        List.append(val)

    print("Input List :", List)

    t1 = threading.Thread(target=Prime, args=(List,))
    t2 = threading.Thread(target=NonPrime, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()