
library = []

def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = int(input("Enter publication year: "))
        book = {"title": title, "author": author, "year": year}
        library.append(book)
        print("Book added successfully!\n")
    except ValueError:
        print("Invalid input for year. Please enter a number.\n")

def show_books():
    if not library:
        print("No books in the library.\n")
    else:
        print("\n=== All Books ===")
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")
        print()

def search_book():
    title = input("Enter the book title to search: ")
    found = [book for book in library if book["title"].lower() == title.lower()]
    if found:
        print("\nBook found:")
        for book in found:
            print(f"{book['title']} by {book['author']} ({book['year']})\n")
    else:
        print("Book not found.\n")

def delete_book():
    title = input("Enter the book title to delete: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book deleted successfully!\n")
            return
    print("Book not found.\n")

def main():
    while True:
        print("=== Library Management System ===")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Delete a book")
        print("5. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
