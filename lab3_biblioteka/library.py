import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def to_dict(self):
        return {"title": self.title, "author": self.author, "is_borrowed": self.is_borrowed}

    @staticmethod
    def from_dict(data):
        b = Book(data["title"], data["author"])
        b.is_borrowed = data["is_borrowed"]
        return b


class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load()

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                self.save()
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                self.save()
                return True
        return False

    def list_books(self):
        return self.books

    def search_books(self, keyword):
        result = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                result.append(book)
        return result

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2, ensure_ascii=False)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]
        except FileNotFoundError:
            self.books = []
