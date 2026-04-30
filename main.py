# Display opening message
print(
    "\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n"
)

# Make book list
books = []

# Enter While loop
while True:
    # Print the menu
    print(
        "Menu:\n"
        "    Add book (Add)\n"
        "    Remove book (Remove)\n"
        "    Show inventory (Show)\n"
        "    Show inventory count (Count)\n"
        "    Quit (Q)\n"
    )
    # Ask for user action:
    action = input("What would you like to do? ").lower()

    if action == "add":
        book_name = input("What book would you like to add? ")
        books.append(book_name)
        print(f'"{book_name}" was added successfully.')
        continue
    elif action == "remove":
        book_name = input("What book would you like to remove? ")

        if not book_name in books:
            print("That book is not in your list of books.")
        else:
            books.remove(book_name)

        continue
    elif action == "show":
        for number, book in enumerate(books):
            print(f"{number}: {book}")
            continue

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
