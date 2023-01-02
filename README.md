# Library Management System
## Introduction
Library management system is useful for the librarian to keep track of all the books. He can
search the book in the library. This system helps the librarian to track the books that are being
issued to the students or staff.

### Tasks
- Add new book
- Update book
- Delete book
- Issue book
- Return book
- Global book search

### Artifacts
- Flow Chart
- Report
- Source Code
### Importing Modules
```
import datetime
import pandas as pd

```

Here we are importing 2 modules “datetime” and “pandas”. Datetime is used for handling time usage and getting the current time from the user. Then we import a .csv file and store the current time in ‘today’ variable. The ‘time_to_return’ variable adds 14 days as a result date whenever it is called. ‘pd.set_option’ is used to display the terminal correctly and prevent it from overlapping.

## Functions
### Add Book


The add_book() function adds a new book in the DataFrame. Global variables are used so that any variable outside the function can be used inside the function as well. Then we take two inputs from the user for the book name and the placement of the book. Then using a Dictionary in which keys are column headers of a DataFrame, we append the entered data into the DataFrame.

### Issue Book

The issue_book() function is used to issue a book to a person. It takes two inputs: one for the book name and the other for the person name it is issued to.

### Return Book

The return_book() function returns an issued book and sets all the columns to default values.

### Delete Book

The delete_book() function deletes a book from the DataFrame by deleting the row using drop function. Then we set the index to “Book Name” again so that we can take input from the user in a string.

### View Books Issued to a User

The user_issued() function checks if the user is in the ‘Issued to’ column of the DataFrame and shows all the books issued to that user.

### Status of a Book

The book_issued() function checks if the entered book is in the DataFrame. If it is, then it shows the status of the book e.g. it’s availability, the user this book is issued to, placement of the book and entry date.


## Home Screen
This the main code of the program where you are first welcomed by a welcome message and then using the while True infinite loop, we take inputs from user to choose. Each choice has its own function that it calls and if the choice entered is invalid, then the loop runs again.

### Welcome Screen
```print('-------------------------------------------------')
print('-                    -')
print('-  Welcome to Library Management System  -')
print('-                    -')
print('-------------------------------------------------')
print('')
```

As you can here, You are first welcomed by this message. Then we run a while True infinite loop.

### While True Loop
```while True:

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

```




### Our Motive
> ***The reason behind this code is that we wanted to create a system where you can manage and add data in it and upon looking at the library management system, we found it to be very interesting. We wanted to design a program where you can have all your data in a single frame, save the new entered data and is also capable of performing all the other library management system related functions.***

## Flow Chart

![Flow Chart LMS_1](https://user-images.githubusercontent.com/72499151/157419274-9ecbf25c-e9c7-45b3-b26e-7af4ce6f8c4f.jpg)
![FLow lms_1](https://user-images.githubusercontent.com/72499151/157419223-40bf362a-ccfa-4a22-a363-58e22ca6deb1.jpg)
![Flow Chart LMS_2](https://user-images.githubusercontent.com/72499151/157419286-5a2ddd98-dfea-465f-a448-b7158cf8d147.jpg)
