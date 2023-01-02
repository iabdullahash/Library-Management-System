import datetime
import pandas as pd

df = pd.read_csv('Book1.csv')
today = datetime.date.today()
time_to_return = datetime.timedelta(days=14)  # 14 days to return
return_time = today + time_to_return
structure = pd.DataFrame(df)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
count = 0


def add_book():
    global structure
    global today
    book = input("Enter new book: ")
    row = input("Enter book placement(row,column): ")
    newbook = {'Book Name': book, 'Entry Date': today, 'Availability': 'Yes', 'Issue Date': 'None', 'Issued To': 'None',
               'Return Date': 'None', 'Extra Charges': 0, 'Placement': row}
    structure = structure.append(newbook, ignore_index=True)


def issue_book():
    global structure
    global df
    print('------------------------------')
    print(structure)
    print('------------------------------')
    print('')
    book = input("What book do you want to issue?: ")
    issue_person = input("Who do you want to issue the book to: ")
    if structure['Book Name'].str.contains(book).any():
        structure.set_index('Book Name', inplace=True)
        structure.loc[book, 'Issue Date'] = today
        structure.loc[book, 'Availability'] = 'No'
        structure.loc[book, 'Issued To'] = issue_person
        structure.loc[book, 'Return Date'] = return_time
        structure.reset_index(inplace=True)
        print('------------------------------')
        print('Book issued Successfully')
        print('------------------------------')

    else:
        print('------------------------------')
        print("Wrong Input, Enter book index again!")
        print('------------------------------')
        issue_book()


def user_issued():
    user = input("Enter user to view: ")
    global structure
    if structure['Issued To'].str.contains(user).any():  # Checks if the user is in the 'Issued To' box
        check = structure[structure['Issued To'] == user]
        print(check)
    else:
        print('No book issues to specifies person')
        print('')
        print('Enter again')
        user_issued()


def book_issued():
    book = input("Enter Book to view: ")
    global structure
    if structure['Book Name'].str.contains(book).any():
        check = structure[structure['Book Name'] == book]
        print(check)
    else:
        print('------------------------------')
        print('No book with the name', book, 'found in the database')
        print('------------------------------')
        print('Enter Again')
        book_issued()


def return_book():
    global structure
    returned_book = input("Enter book name to return: ")
    if structure['Book Name'].str.contains(returned_book).any():
        structure.set_index('Book Name', inplace=True)
        structure.loc[returned_book, 'Availability'] = 'Yes'
        structure.loc[returned_book, 'Issue Date'] = 'None'
        structure.loc[returned_book, 'Return Date'] = 'None'
        structure.loc[returned_book, 'Issued To'] = 'None'
        structure.reset_index(inplace=True)
        print("Book Returned")
    else:
        print('------------------------------')
        print('Invalid Book')
        print('------------------------------')
        print('Enter Again')
        return_book()


def available():
    global structure
    print(structure[structure['Availability'] == 'Yes'])


def delete_book():
    global structure
    delete = input("Which book do you want to delete?: ")
    if structure['Book Name'].str.contains(delete).any():
        structure.set_index('Book Name', inplace=True)
        structure = structure.drop(delete)
        structure.reset_index(inplace=True)
        print("-------------------------------------------------")
        print("Book Deleted")
    else:
        print("Invalid Entry")
        print("Enter Again")
        delete_book()


print('-------------------------------------------------')
print('-                    -')
print('-  Welcome to Library Management System  -')
print('-                    -')
print('-------------------------------------------------')
print('')

while True:

    print("""           Enter 'A' to add a new book
           Enter 'I' to issue a book
           Enter 'U' to view issued books to the user
           Enter 'R' to return a book
           Enter 'V' to view available books
           Enter 'B' to view status of a book
           Enter 'D' to view database
           Enter 'X' to delete a book
           Enter 'Q' to exit
           Enter 'S' to save file""")

    print('-------------------------------------------------')
    choice = input("What would you like to do: ").upper()
    print('-------------------------------------------------')
    if choice == 'A':
        add_book()
        print(structure)
        print('-------------------------------------------------')
    elif choice == 'I':
        issue_book()
        print('-------------------------------------------------')
    elif choice == 'U':
        user_issued()
        print('-------------------------------------------------')
    elif choice == 'R':
        return_book()
        print('-------------------------------------------------')
    elif choice == 'B':
        book_issued()
        print('-------------------------------------------------')
    elif choice == 'D':
        print(structure)
        print('-------------------------------------------------')
    elif choice == 'X':
        delete_book()
        print('-------------------------------------------------')
    elif choice == 'V':
        available()
        print('-------------------------------------------------')
    elif choice == 'S':
        structure.to_csv('Book1.csv',index=False)
        print("File Saved")
        print('-------------------------------------------------')
        count = count + 1
    elif choice == 'Q':
        if count == 0:
            print("You have not saved your work. Do you want to exit anyways?:")
            decision = input(">").upper()
            if decision == 'YES':
                break
            else:
                continue
        else:
            break
    else:
        print('-------------------------------------------------')
        print('Invalid choice, Choose again')
        print('-------------------------------------------------')

print("Good Bye")
