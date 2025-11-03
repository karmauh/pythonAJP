from library import Library

def menu():
    print("\n1. Dodaj książkę")
    print("2. Wypożycz książkę")
    print("3. Zwróć książkę")
    print("4. Wyświetl wszystkie książki")
    print("5. Wyszukaj książkę")
    print("6. Zakończ")

def main():
    lib = Library()
    while True:
        menu()
        choice = input("Wybierz opcję: ")
        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            lib.add_book(title, author)
            print("Dodano książkę.")
        elif choice == "2":
            title = input("Tytuł do wypożyczenia: ")
            if lib.borrow_book(title):
                print("Książka wypożyczona.")
            else:
                print("Nie można wypożyczyć książki.")
        elif choice == "3":
            title = input("Tytuł do zwrotu: ")
            if lib.return_book(title):
                print("Książka zwrócona.")
            else:
                print("Nie znaleziono wypożyczonej książki.")
        elif choice == "4":
            for b in lib.list_books():
                status = "wypożyczona" if b.is_borrowed else "dostępna"
                print(f"{b.title} - {b.author} ({status})")
        elif choice == "5":
            keyword = input("Wpisz tytuł lub autora: ")
            results = lib.search_books(keyword)
            if results:
                for b in results:
                    status = "wypożyczona" if b.is_borrowed else "dostępna"
                    print(f"{b.title} - {b.author} ({status})")
            else:
                print("Brak wyników.")
        elif choice == "6":
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
