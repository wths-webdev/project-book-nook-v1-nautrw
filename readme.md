# Book Nook Inventory System v1
<b>Welcome to Book Nook!</b>  
<img src="./images/book-nook-logo.png" width=170>  
You have been selected for an internship at the (fictional) Book Nook Library, one of the most prestigious libraries in the world. 

As an intern at the Book Nook, your first task is to create a Python program that simulates the inventory system of our library. You'll need to start with a basic list that represents the library’s shelves, and then add functionality that allows the staff to add and remove books from the inventory. You'll also need to display the count of the inventory in a readable format, so that the librarians can keep track of the books.

## Minimum Requirements
1. Start with creating your pseudocode / outline! I must see it before you move onto step 2.
2. Your program must have comments describing each code block.
3. Display a menu to your user, something like:
```
Welcome to...
      ______ ______
    _/      Y      \_
   // ~Book | ~~ ~  \
  // ~ ~ ~~ |  Nook~ \      
 //________.|.________\     
`----------`-'----------'

Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? 
```
4. Perform the necessary actions based on the user's input. You'll need conditional statements.
5. Use a loop to allow the librarian to stay in the program until they select quit.
5. Test your code by adding and removing books, manga, or comics you've read, and showing the inventory count.

So, are you ready? Grab your pens, notebooks, and library cards, and let's create an inventory system that will help us organize and share the world's knowledge!


## Extra Challenge
Extra Challenge
The better your inventory system, the better service we can provide our patrons. You'll need to:
* Add a menu option which displays the inventory in a readable format.
* Handle cases where the player tries to remove an item that is not in the inventory.
* Track which books have been checked out. Assume the library has 1 copy of each book.

### Sample Run 1
```
Welcome to...
      ______ ______
    _/      Y      \_
   // ~Book | ~~ ~  \
  // ~ ~ ~~ |  Nook~ \      
 //________.|.________\     
`----------`-'----------'

Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? add
What book would you like to add? Batman Court of Owls
Batman Court of Owls was added successfully.


Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? add
What book would you like to add? Wonder Woman
Wonder Woman was added successfully.


Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? count
There are 2 books in your inventory.
```
### Challenge Sample Run
```
Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory (show) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? remove
What book would you like to remove? fsdfs
Error: fsdfs not in inventory.

Menu: 
 Add book (add)
 Remove book (remove) 
 Show inventory (show) 
 Show inventory count (count) 
 Quit (q)

What would you like to do? show
There are 4 books in your inventory.
1. Wonder Woman
2. Batman Court of Owls
3. My Hero Academia
4. Fullmetal Alchemist
```
## The menu
```
print("\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n")
```
