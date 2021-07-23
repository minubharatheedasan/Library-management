import time
from typing import Pattern
import Library_model
import Library_controller
import re

def StartView(): 
    print("\n\n---Welcome to Central Library---")
    print("[N] for New user")
    print("[E] for Existing user")
    print("[L] If you are a Librarian")
    return "Enter your Choice :" 

def EndView():
    print("\nThank you for using the Central Library.\nHave a great day! :)")
    return

def InvalidEntry():
	print("\n>>>>ERROR<<<< : Invalid Entry!\n")
    
# def existinguser(): 
#     print("\n\n---Welcome to Central Library---")
#     print("Hello please enter your user name and password\n")
#     username = input("Username:")
#     password = input("Password:")
#     Library_model.Library.existuser(username,password)
#     return username
def existinguserchecklibrarianoruser(): 
    print("\n\n---Welcome to Central Library---")
    print("Hello please enter your user name and password\n")
    username = input("Username:")
    password = input("Password:")
    type = Library_model.Library.existuser(username,password)
    return username,type

def newuser(): 
    print("\n\n---Welcome to Central Library---")
    print("Hello new user you must register yourself with your name and phone number\n")
    username = input("name:")
    phone = input("phone:")
    password = input("password")
    # Pattern = re.compile("[7-9][0-9]{9}")
    # if (Pattern.match(phone)):
    #     validphone = phone
    # else:
    #     phone = "Invalid phone"
    #     print("Invalid phone number... Please try with a valid phone number starting with")
    # if phone == "Invalid phone":
    #     exit()
    # else:
    type = Library_model.Library.newuser(username,phone,password)
    return username,type

def AddLibrarian():
    print("\n\n---Welcome to Central Library---")
    print("Hello, You are about to add a librarian please enter the name and phone number\n")
    username = input("name:")
    phone = input("phone:")
    password = input("password")
    type = Library_model.Library.addLibrarian(username,phone,password)
    print(type)
    print(username)
    return username,type

def checkifuserexists(username,phone): 
    print("\n\n---Welcome to Central Library---")
    print("Hello the user or the phone number is registered already.\n Please try with different user name and phone number \n")
    username = input("name:")
    phone = input("phone:")
    password = input("password")
    Library_model.Library.newuser(username,phone,password)
    return "Hello {username}"

def Librarian(): 
    print("\n\n---Welcome to Central Library---")
    print("\n press\n 1. To Add user \n 2. To Add Books \n 3. To List all books\n 4. To update book details \n 5. To add the quantity of books \n 6. To delete user \n 7. To delete books \n 8. To add a Librarian \n 9. To Exit \n")
    lib_option = int(input("\nDear Librarian Enter your option:"))
    return lib_option
    

def addnewbook():
    print("\nPlease enter the book details\n")
    titleofbook = input("\n Enter the Title of the Book: ")
    author = input("\n Enter the name of author: ")
    publication = input("\n Enter the publication details: ")
    bookcategory = input("\n Enter the category of the book: ")
    numberofbooks = input("\n Enter the count of the book: ")
    Library_model.Library.addnewbook(titleofbook,author,publication,bookcategory,numberofbooks)
    

def ListallBooks():
    print("List of all books in library:")
    Library_model.Library.allBooks()
    

def ModifyBooks():
    Library_model.Library.allBooks()
    
    bookid = input("\nEnter the book id to modify the book details")
    
    updatelistDict = {}
    chtitle = input("\nDo you wish to change the title of the book?\n(press y if you wish to change the title) : ")
    if chtitle == 'y':
        changetitle = input("\nPlease enter the title you wanted to update")
        updatelistDict['titleofbook'] = changetitle
    else:
        chtitle = 0

    chauthor = input("\nDo you wish to change the author of the book?\n(press y if you wish to change the author) : ")
    if chauthor == 'y':
        changeauthor = input("\nPlease enter the author you wanted to update :")
        updatelistDict['author'] = changeauthor
    else:
        chauthor = 0

    chpublication = input("\nDo you wish to change the Publication of the book?\n(press y if you wish to change the Publication details) :")
    if chpublication == 'y':
        changepublication = input("\nPlease enter the Publication you wanted to update :")
        updatelistDict['publication'] = changepublication
    else:
        chpublication = 0

    chtype= input("\nDo you wish to change the Category  of the book?\n(press y if you wish to change the Publication details) :")
    if chtype == 'y':
        changecategory = input("\nPlease enter the category you wanted to update :")
        updatelistDict['booktype'] = changecategory
    else:
        chtype = 0

    chbooknos= input("\n Do you wish to modify the number of the books available?\n(press y if you wish to change the number of books) : ")
    if chbooknos == 'y':
        changebooknos = input("\n Please enter the category you wanted to update :")
        updatelistDict['numberofbooks'] = changebooknos
    else:
        chbooknos = 0
    # print(updatelistDict.keys())
    # print(updatelistDict.values())
    if chtitle == 0 and chauthor ==0 and chpublication ==0 and chtype ==0 and chbooknos == 0:
        print("\n You have opted not to change any details of books")

    else:
        Library_model.Library.ModifyBookDetails(bookid,updatelistDict)

def addbooknum():
    bookid = input("\nPlease enter the bookid to which you wanted to add books to: \t")
    cnt = input(f"\nPlease enter the count for books to be added for bookid {bookid}: \t")
    Library_model.Library.addbooknos(bookid,cnt)


def Deleteuser():
    userid = input("\n Please Enter the user's username to be deleted: ")
    Library_model.Library.UserToDelete(userid)
    Library_model.Library.displayuserlistToDelete()

def Deletebook():
    bookid = input("\n Please Enter the bookid to be deleted: ")
    Library_model.Library.BookToDelete(bookid)
    
def alreadyuser(): 
    print("\n\n---Welcome to Central Library---")
    print("\n press\n 1. To see the details of all books \n 2. To Lend a book \n 3. To fetch the list of books in your name \n 4. To return a book \n 5. To Exit \n")
    ex_option = int(input("\nDear User Enter your option from our menu:"))
    return ex_option   
    

def ToLendbook(username):
    ListallBooks()
    bookid = (int(input(f"\n\n Dear user {username} Please enter the book id you wish to render")))
    Library_model.Library.Lendbook(username,bookid)

def ListofRentedbooks(username):
    print(username)
    print("\nDear user the following are the books that you have rendered: ")
    Library_model.Library.Renderedlist(username)

def ToReturnBook(username):
    ListofRentedbooks(username)
    bookid = (int(input("Please enter the bookid you would like to return: "))) 
    Library_model.Library.ReturnBooks(username,bookid) 

def exit():
    print("Thank you for using Central Library.... HAPPY READING...")
    