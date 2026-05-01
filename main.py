# Make book list
# Display opening message
# Enter While loop
# Print the menu
# Ask for user action:
## If add:
### Ask user for name of  book
### Add book to list of books
### Print success/failure message
### Continue
## If remove:
### Ask user for book to remove
### Check if book is in book list
#### If it is, remove it from the book list
### If it is not, print a failure message
## If show:
### Print out an (enumerated) list of the books in the list
## If count:
### Print out the length of the book list
## If quit:
### Break

books = []

print(
    "\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'"
)


while True:
    print(
        "\nMenu:\n"
        " Add book (Add)\n"
        " Remove book (Remove)\n"
        " Show inventory (Show)\n"
        " Show inventory count (Count)\n"
        " Quit (Q)\n"
    )
    action = input("What would you like to do? ").lower()

    if action == "add":
        book_name = input("What book would you like to add? ")
        books.append(book_name)
        print(f"{book_name} was added successfully.")
    elif action == "remove":
        book_name = input("What book would you like to remove? ")

        if not book_name in books:
            print(f"Error: {book_name} is not in inventory.")
        else:
            books.remove(book_name)
            print(f"Successfully removed {book_name} from inventory.")
    elif action == "show":
        for index, book in enumerate(books):
            print(f"{index + 1}: {book}")
    elif action == "count":
        print(f"There are {len(books)} books in your inventory.")
    elif action == "q":
        print("Exiting.")
        break
    else:
        print("Error: invalid action.")
