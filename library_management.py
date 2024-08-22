class library:
    def __init__(self):
        self.books=[]
        self.members=[]
        self.no_of_books=0

    def books_name(self):
        if self.books:
            print("Books present in this library are:")
            for book in self.books:
                print(book)
        else:
            print("no book")

    def members_name(self):
        if self.members:
            print("Members in this library are:")
            for member in self.members:
                print(member)
        else:
            print("no members")

    def add_books(self,book_list):
        for book in book_list:
            self.books.append(book)
            print(f"{book} is added to the library")
        


    def add_member(self,member):
        self.members.append(member)
        print(f"{member} is added in members list of this library")

    def borrow(self,member_name,book_to_borrow):
        member = next((m for m in self.members if m.name == member_name),None)
        if member:
            if book_to_borrow in self.books:
                self.books.remove(book_to_borrow)
                member.borrowed_books.append(book_to_borrow)
                print(f"{member_name} borrowed '{book_to_borrow}'")
            else:
                print(f"{book_to_borrow} isn't available in the library.")
        else:
            print(f"member '{member_name} not found in the library")
    def book_return(self,member,book_to_return):
        member = next((m for m in self.members if m.name == member),None)
        if member:
            if book_to_return not in self.books:
                member.borrowed_books.remove(book_to_return)
                self.books.append(book_to_return)
                print(f"Member {member} returned the book {book_to_return}.")
            else:
                print(f"{book_to_return} was not borrowed.")
        else:
            print(f"Member '{member} not found in library.")

class Member(library):
    def __init__(self,name):
        self.name = name
        self.borrowed_books=[]

    def __str__(self):
        return self.name


if __name__== "__main__":

    lib1 = library()
    books_to_add = ["Harry Potter","A song of ice and fire","Mother","Bhagwat Geeta"]
    lib1.add_books(books_to_add)
    lib1.books_name()
    mem1 = Member("Aaditya")
    mem2 = Member("John")
    lib1.add_member(mem1)
    lib1.add_member(mem2)
    lib1.members_name()
    lib1.borrow("Aaditya","Harry Potter")
    lib1.borrow("Aaditya","A song of ice and fire")
    print("books after borrowing")
    lib1.books_name()

    print("\nmembers and their borrowed books")
    for member in lib1.members:
        borrowed_book_list = ", ".join(member.borrowed_books) if member.borrowed_books else "No Books"
        print(f"{member} has borrowed: {borrowed_book_list} ")

    lib1.book_return("Aaditya","Harry Potter")

    for member in lib1.members:
        borrowed_book_list = ", ".join(member.borrowed_books) if member.borrowed_books else "No Books"
        print(f"{member} has borrowed: {borrowed_book_list} ")