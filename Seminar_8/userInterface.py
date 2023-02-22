from methods import readBook, writeBook, searchBook, editBook, deleteBook

def interface():
    # raw string
    print("""Choose mode:
                1 - Write new contact
                2 - Show contact list
                3 - Search contact
                4 - Edit
                5 - Delete
                """)

    userInput = int(input("Mode: "))
    while userInput < 1 or userInput > 5:
        print("Input correct mode number!")
        userInput = int(input("Mode: "))
    
    if userInput == 1:
        writeBook()
    elif userInput == 2:
        readBook()
    elif userInput == 3:
        searchBook()
    elif userInput == 4:
        editBook()
    elif userInput == 5:
        deleteBook()
