#oops in python
#real world mini project
#library management system
class Library:
    def __init__(self):
        self.book=["english","hindi","mathematics","science","social science","economy","history"]

    def add_book(self,book):
        self.book.append(book)
        print(f"{book} has been added to the library successfully.")

    def show_book(self):
        print(f"available book list in the library:")
        if len(self.book)==0:
            print(f"no book is available in the library.")
        else:
            for book in self.book:
                print(book)

    def issue_book(self,book):
        if book in self.book:
            self.book.remove(book)
            print(f"{book} is issued successfully.")
        else:
            print(f"{book} is not available in the library.")

    def return_book(self,book):
        self.book.append(book)
        print(f"{book} is returned back to the library list")

l1=Library()
l1.add_book("java")
l1.issue_book("economy")
l1.issue_book("python")
l1.return_book("economy")
l1.return_book("geography")
l1.show_book()
                                       