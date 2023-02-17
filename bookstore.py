#Import sqlite3 and create a cursor for the table
import sqlite3
connection = sqlite3.connect("ebookstore.db")
cursor = connection.cursor()




#Create "books" table in ebookstore database and fill it up with "book_list" (this will not run everytime and it must use if the database not exists with the table).
"""cursor.execute("create table books(id integer, title text, author text, qty integer)")
book_list = [
    (3001, "A Tale of Two Cities", "Charles Dickesn", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12),
]
cursor.executemany("insert into books values (?,?,?,?)", book_list)
connection.commit()"""






#This Function lets the user to add a new book to the system
def add_book():
    sure = input("You will add a new book to the system. Are you sure in this? ('yes' or 'no'): ")
    if sure.lower() == "yes":
        try:
            book_id = int(input("Please, enter the ID of the book: "))
            book_title = input("Please, enter the title of the book: ")
            book_author = input("Please, enter the author of the book: ")
            book_qty = int(input("Please, enter the quantity of the book: "))

            cursor.execute("insert into books(id, title, author, qty) values(?,?,?,?)", (book_id, book_title, book_author, book_qty))
            connection.commit()
            print("Book succesfully added to the system!")
        except ValueError:
            print("The entered value is not a number!")

    elif sure.lower() == "no":
        return
    else: 
        print("The entered value is not valid!")







#This Function lets the user to add a new book to the system
def update_book():
    try:
        update_id = int(input("Please, enter the ID of the book which you want to update: "))

        print("""-----------------------
    Please, enter the number of the option which you want to update:
    1. ID
    2. Title
    3. Author
    4. Qty
    0. Exit
        -----------------------""")
        option = input("Enter the number: ")

        if option == "1":
            try:
                new_id = int(input("Please, enter the new ID of the book: "))
                cursor.execute("update books set id = ? where id = ?", (new_id, update_id))
                connection.commit()
                print("The id of the book was successfully changed!")
            except ValueError:
                print("The entered value is not a number!")
                return

        elif option == "2":
            new_title = input("Please, enter the new title of the book: ")
            cursor.execute("update books set title = ? where id = ?", (new_title, update_id))
            connection.commit()
            print("The title of the book was successfully changed!")

        elif option == "3":
            new_author = input("Please, enter the new author of the book: ")
            cursor.execute("update books set author = ? where id = ?", (new_author, update_id))
            connection.commit()
            print("The author of the book was successfully changed!")

        elif option == "4":
            try:
                new_qty = int(input("Please, enter the new quantity of the book: "))
                cursor.execute("update books set qty = ? where id = ?", (new_qty, update_id))
                connection.commit()
                print("The quantity of the book was successfully changed!")
            except ValueError:
                print("The entered value is not a number!")

        elif option == "0":
            return
        
        else:
            print("The entered value is not valid!")
    except ValueError:
            print("The entered value is not a number!")





#This Function lets the user to update a book in the system
def delete_book():
    try:
        del_book = int(input("Please, enter the ID of the book which you want to delete: "))
        cursor.execute("delete from books where id = ?", (del_book, ))
        connection.commit()
        print("Book successfully deleted from the system!")
    except ValueError:
            print("The entered value is not a number!")





#This Function lets the user to search for a book in the system
def search_book():
    try:
        search = int(input("Please, enter the ID of the book which you want to read about: "))
        cursor.execute("select * from books where id =?", (search,))
        book = cursor.fetchall()
        for row in book:
            print(f"ID:{row[0]}")
            print(f"Title:{row[1]}")
            print(f"Author:{row[2]}")
            print(f"Qty:{row[3]}")
            print("\n")
    except ValueError:
            print("The entered value is not a number!")




#This function is an extra and this prints out all the books in the system
def list_books():
    cursor.execute("select * from books")
    book = cursor.fetchall()
    print("""-------------
List of books
-------------""")
    for row in book:
        print(f"\tID:{row[0]}")
        print(f"\tTitle:{row[1]}")
        print(f"\tAuthor:{row[2]}")
        print(f"\tQty:{row[3]}")
        print("\n")



#==========Main Menu=============
#At this part the menu will be printed out where the user can make his/her choice which menu to open.
while True:
    menu = input('''--------------------------------------------------------------------
Select one of the following Options below(enter the number):
\t1.   - Enter book
\t2.   - Update book
\t3.   - Delete book
\t4.   - Search books
\t5.   - List of books 
\t0.   - Exit
--------------------------------------------------------------------
: ''')
    
    #At this part the menu options will call the correct function.
    if menu == "1":
        add_book()

    elif menu == "2":
        update_book()
        
    elif menu == "3":
        delete_book()

    elif menu == "4":
        search_book()

    elif menu == "5":
        list_books()

    elif menu == "0":
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")