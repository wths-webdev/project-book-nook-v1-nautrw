# Make book list
books = []


# Display opening message
print(
    "\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'"
)


# Enter While loop
while True:
    # Print the menu
    print(
        "\nMenu:\n"
        " Add book (Add)\n"
        " Remove book (Remove)\n"
        " Show inventory (Show)\n"
        " Show inventory count (Count)\n"
        " Quit (Q)\n"
    )
    # Ask for user action:
    action = input("What would you like to do? ").lower()

    ## If add:
    if action == "add":
        ### Ask user for name of  book
        book_name = input("What book would you like to add? ")
        ### Add book to list of books
        books.append(book_name)
        ### Print success/failure message
        print(f"{book_name} was added successfully.")
    ## If remove:
    elif action == "remove":
        ### Ask user for book to remove
        book_name = input("What book would you like to remove? ")

        ### Check if book is in book list
        if not book_name in books:
            ### If it is not, print a failure message
            print(f"Error: {book_name} is not in inventory.")
        else:
            #### If it is, remove it from the book list
            books.remove(book_name)
            print(f"Successfully removed {book_name} from inventory.")
    ## If show:
    elif action == "show":
        ### Print out an (enumerated) list of the books in the list
        for index, book in enumerate(books):
            print(f"{index + 1}: {book}")
    ## If count:
    elif action == "count":
        ### Print out the length of the book list
        print(f"There are {len(books)} books in your inventory.")
    ## If quit:
    elif action == "q":
        print("Exiting.")
        ### Break
        break
    else:
        print("Error: invalid action.")
