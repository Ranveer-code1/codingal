class library:
    def __init__(self,books):
        self.books=books
    def display(self):
        print("Books in the L.I.B.R.A.R.Y")
        for i in self.books:
            print(i)
    def add(self,book):
        self.books.append(book)
        print("Successfully added book")
    def return_book(self,book):
        if book in self.books:
            print("This book is already in the libaray")
        else:
            self.books.append(book)
            print("Book successfully returned")
obj=library(["To Kill a Mockingbird","The Great Gatsby","The Lord of the Rings","Harry Potter and the Sorcerer’s Stone", "The Hobbit","The Chronicles of Narnia","Moby-Dick", "Little Women","Fahrenheit 451","Wuthering Heights", "The Kite Runner", "The Hunger Games", "A Tale of Two Cities"])

while True:
    print("Press 1 to display all the books")
    print("Press 2 to add books")
    print("Press 3 to return books")
    print("Press 4 to exit")
    a=int(input("Enter your choice"))
    if a==1:
        obj.display()
    elif a==2:
        b=input("Enter the book name in correct punctuation and spelling")
        obj.add(b)
    elif a==3:
        c=input("Enter the book name in correct punctuation and spelling")
        obj.return_book(c)
    elif a==4:
        break
    else:
        print("Enter a valid number")