# from Library_view import StartView,existinguser
# from Library_model import existuser
import Library_view
import Library_model
def GetChoice():

    choice=input(Library_view.StartView())
    
    if choice.lower() =='e':
        username,usertype = Library_view.existinguserchecklibrarianoruser() 
        print(username)
        print(usertype)
        if usertype == 'User':
            e_option = 0
            while e_option != 5:
                e_option = Library_view.alreadyuser()
                if e_option == 1:
                    Library_view.ListallBooks()  
                if e_option == 2:
                    Library_view.ToLendbook(username)  
                if e_option ==3:
                    Library_view.ListofRentedbooks(username)  
                if e_option == 4:
                    Library_view.ToReturnBook(username)   
                if e_option == 5:
                    Library_view.exit()
                    #if e_option == 3:
                    #Library_view.CurrentlyAvailable() 
        if usertype == 'Librarian':
            #username,usertype = Library_view.existinguserchecklibrarianoruser() 
        #print(f"\nHello {username} Please select your options you want to perform: \n")
            option = 0
            while option != 9:
                option=Library_view.Librarian() 
                if option  == 1:
                    Library_view.newuser()  
                if option == 2:
                    Library_view.addnewbook()  
                if option == 3:
                    Library_view.ListallBooks()
                if option == 4:
                    Library_view.ModifyBooks()      
                if option == 5:
                    Library_view.addbooknum()
                if option == 6:
                    print("\nBelow are the list of existing users: ")
                    Library_model.Library.displayuserlistToDelete()
                    Library_view.Deleteuser()
                if option == 7:
                    print("\nBelow are the list of available books: ")
                    Library_view.ListallBooks()
                    Library_view.Deletebook()
                if option == 8:
                    Library_view.AddLibrarian()
                if option == 9:
                    Library_view.exit()

    elif choice.lower() =='n':
        username,usertype = Library_view.newuser()  
        e_option = 0
        while e_option != 5:
            e_option = Library_view.alreadyuser()
            if e_option == 1:
                Library_view.ListallBooks()  
            if e_option == 2:
                Library_view.ToLendbook(username)  
            if e_option ==3:
                Library_view.ListofRentedbooks(username)  
            if e_option == 4:
                Library_view.ToReturnBook(username)   
            if e_option == 5:
                Library_view.exit()
                    #if e_option == 3:
                    #Library_view.CurrentlyAvailable()
        #print("Please login as existing user with the registered username and password")

    elif choice.lower() =='l':
        username,usertype = Library_view.existinguserchecklibrarianoruser()
        #print(f"\nHello {username} Please select your options you want to perform: \n")
        if usertype == 'User':
            e_option = 0
            while e_option != 5:
                e_option = Library_view.alreadyuser()
                if e_option == 1:
                    Library_view.ListallBooks()  
                if e_option == 2:
                    Library_view.ToLendbook(username)  
                if e_option ==3:
                    Library_view.ListofRentedbooks(username)  
                if e_option == 4:
                    Library_view.ToReturnBook(username)   
                if e_option == 5:
                    Library_view.exit()
                    #if e_option == 3:
                    #Library_view.CurrentlyAvailable() 
        if usertype == 'Librarian':
            #username,usertype = Library_view.existinguserchecklibrarianoruser() 
        #print(f"\nHello {username} Please select your options you want to perform: \n")
            option = 0
            while option != 9:
                option=Library_view.Librarian() 
                if option  == 1:
                    Library_view.newuser()  
                if option == 2:
                    Library_view.addnewbook()  
                if option == 3:
                    Library_view.ListallBooks()
                if option == 4:
                    Library_view.ModifyBooks()      
                if option == 5:
                    Library_view.addbooknum()
                if option == 6:
                    print("\nBelow are the list of existing users: ")
                    Library_model.Library.displayuserlistToDelete()
                    Library_view.Deleteuser()
                if option == 7:
                    print("\nBelow are the list of available books: ")
                    Library_view.ListallBooks()
                    Library_view.Deletebook()
                if option == 8:
                    Library_view.AddLibrarian()
                if option == 9:
                    Library_view.exit()


if __name__== '__main__': # main method 
    GetChoice() # function call 