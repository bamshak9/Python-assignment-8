"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""
class Library:
    def __init__(self):
        self.available=[]
        self.borrowed={}
    def add_book(self,book):
        self.available.append(book)
    def borrow_book(self,user,book):
        self.available.remove(book)
        self.borrowed[user]=book
    def return_book(self,user):
        if user in self.borrowed.keys():
            self.available.append(self.borrowed[user])
            self.borrowed.pop(user)
        else:
            print(f"{user} did not borrow a book")
    def show_available_books(self):
        return self.available

lib = Library()
lib.add_book("Python 101")
lib.add_book("Data Science Handbook")
lib.borrow_book("Alice", "Python 101")
print(lib.show_available_books())
lib.return_book("Alice")
lib.return_book("Alice")
print(lib.show_available_books())