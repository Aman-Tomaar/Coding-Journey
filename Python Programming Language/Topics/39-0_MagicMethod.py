#


class Book:
    def __init__(self, name, author, page_num):
        self.name = name
        self.author = author
        self.page_num = page_num

    def __str__(
        self,
    ):  # if this wasnt here the print(book1) would have resulted in giving a memory location
        return f"'{self.name}' by {self.author} & total no. of page in the book is: {self.page_num}"

    def __eq__(  # eq = equal
        self, other
    ):  # if this wasnt here even if the name and author of the book was same the result of print(book1 == book2) would be false
        return self.name == other.name and self.author == other.author

    def __lt__(  # lt = less than
        self, other
    ):  # if this wasnt here the print(book2 < book1) whould have given an error
        return self.page_num < other.page_num

    def __gt__(  # gt = grater than
        self, other
    ):  # if this wasnt here the print(book2 > book3) whould have given an error
        return self.page_num > other.page_num

    def __add__(  # add = addition
        self, other
    ):  # if this wasnt here the print(book1 + book3) whould have given an error
        return self.page_num + other.page_num

    def __contains__(  # contains used to see if its in .....
        self, keyword
    ):  # if this wasnt here the print("Lion" in book3) whould have given an error
        return keyword in self.name or keyword in self.author

    def __getitem__(
        self, key
    ):  # find the item and return it in print(book1["name"]), print(book2["author"]), print(book3["page_num"]) if not found then return None
        if key == "name":
            return self.name
        elif key == "author":
            return self.author
        elif key == "page_num":
            return self.page_num


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(book1)
print(book1 == book4)
print(book2 < book1)
print(book2 > book3)
print(book1 + book3)
print("Lion" in book3)
print(book1["name"])
print(book2["author"])
print(book3["page_num"])
print(book4["test"])
