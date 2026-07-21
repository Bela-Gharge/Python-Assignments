class BookStore:
    NoOfBooks = 0

    def __init__(self , Name , Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author} . No of Books are : {BookStore.NoOfBooks}")


obj1 = BookStore("Linux System" , "Robert")
obj1.Display()

obj2 = BookStore("C Programming" , "Dennis Ritchie")
obj2.Display()

obj3 = BookStore("Chhava" , "Shivaji Sawant")
obj3.Display()

obj4 = BookStore("TSITP","Jenny")
obj4.Display()

