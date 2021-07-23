from logging import NullHandler
import mysql.connector
from mysql.connector import Error
import Library_view
import Library_controller
from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate


class Library:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def existuser(username, password):
        conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
        # if conn.is_connected():
        #     print('Connected to MySQL database')
        mycursor = conn.cursor()
        mycursor.execute("SELECT count(*) FROM `users` where username = %s and password = %s",(username,password))
        ((row,),) = mycursor.fetchall() 
       # print(mycursor.fetchall())
        userexists = row
        type = ''
        if userexists  > 0:
           
            mycursor.execute("SELECT usertype FROM users where username = %s and password = %s",(username,password))
            ((record,),) = mycursor.fetchall()
            type = record
            print(type)
           

            # if rec == 'Librarian':
            #     usertype = 'Librarian'
            # if rec == 'User':
            #     usertype = 'User'
        else:
            print("Invalid credentials... please try again..")
        mycursor.close()
        conn.close()
        return type


    def newuser(username, phone, password):
        conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
        # if conn.is_connected():
        #     print('Connected to MySQL database')
        mycursor = conn.cursor()
        # print("user name = ",username)
        # print("phone=" ,phone)
        # print("password=", password)
        check_if_exists_username = 0
        print(username)
        mycursor.execute("SELECT count(*) FROM users where username = %s",(username,))
        ((row,),) = mycursor.fetchall() 
        #print(row)
        check_if_exists_username = row
        #print(check_if_exists_username)
        # print(type(check_if_exists_username))
        # print(check_if_exists_username) 
        if check_if_exists_username != 0:
            print("\nUser name exists. Please try with different user name\n")
            Library_view.newuser()
        # check_if_exists_phone = 0
        mycursor.execute("SELECT count(*) FROM users where phone = %s ",(phone,))
        ((row,),) = mycursor.fetchall() 
        check_if_exists_phone = row
        #print(check_if_exists_phone)
        if check_if_exists_phone != 0:
            print("\nphone number exists. Please try with different phone number\n")
            Library_view.newuser()
        try:
            if  ((check_if_exists_username==0) and (check_if_exists_phone==0)) :
                fee = 0
                # print("Insert into......\n")
                # print(check_if_exists_username)
                # print(check_if_exists_phone)
                usertype = 'User'
                mycursor.execute("insert into users (username,phone,password,usertype) values (%s,%s,%s,%s)",(username,phone,password,usertype))
                conn.commit()
                mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into users table {}".format(error))
        conn.close()
        #Library_view.Librarian()
        return usertype

    def addLibrarian(username, phone, password):
        conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
        # if conn.is_connected():
        #     print('Connected to MySQL database')
        mycursor = conn.cursor()
        # print("user name = ",username)
        # print("phone=" ,phone)
        # print("password=", password)
        check_if_exists_username = 0
        print(username)
        mycursor.execute("SELECT count(*) FROM users where username = %s",(username,))
        ((row,),) = mycursor.fetchall() 
        #print(row)
        check_if_exists_username = row
        #print(check_if_exists_username)
        # print(type(check_if_exists_username))
        # print(check_if_exists_username) 
        if check_if_exists_username != 0:
            print("\nUser name exists. Please try with different user name\n")
            Library_view.newuser()
        # check_if_exists_phone = 0
        mycursor.execute("SELECT count(*) FROM users where phone = %s ",(phone,))
        ((row,),) = mycursor.fetchall() 
        check_if_exists_phone = row
        #print(check_if_exists_phone)
        if check_if_exists_phone != 0:
            print("\nphone number exists. Please try with different phone number\n")
            Library_view.newuser()
        try:
            if  ((check_if_exists_username==0) and (check_if_exists_phone==0)) :
                fee = 0
                # print("Insert into......\n")
                # print(check_if_exists_username)
                # print(check_if_exists_phone)
                usertype = 'Librarian'
                mycursor.execute("insert into users (username,phone,password,usertype) values (%s,%s,%s,%s)",(username,phone,password,usertype))
                conn.commit()
                mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into users table {}".format(error))
        conn.close()
        #Library_view.Librarian()
        return usertype

    def addnewbook(titleofbook,author,publication,bookcategory,numberofbooks):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            mycursor.execute("insert into books(`titleofbook`,`author`,`publication`,`booktype`,`numberofbooks`)values(%s,%s,%s,%s,%s)",(titleofbook, author,publication,bookcategory,numberofbooks))
            conn.commit()
            mycursor.execute("select `bookid`,`titleofbook`,`author`,`publication`,`booktype`,`numberofbooks` from books")
            records = mycursor.fetchall()
            print("\nNew book added\n")
            print (tabulate(records, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            #mycursor.execute("insert into books(titleofbook,author,publication,booktype)values(%s,%s,%s,%s)",(titleofbook, author,publication,bookcategory))
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to insert record into books table {}".format(error))
        conn.close()
        return
    

    def allBooks():
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            mycursor.execute("select * from books")
            records = mycursor.fetchall()
            print (tabulate(records, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            # for row in records:

            #    # print("Book ID | \t Book Name | \t Author | \t Publication | \t Book Type | \n")
            #     #print(str(row[0]) +" | \t "+ str(row[1]) +" | \t "+ str(row[2]) +" | \t "+ str(row[3]) +" | \t "+ str(row[4])+"\n")
            #     print("Book ID : ", row[0])
            #     print("Book Name: ", row[1])
            #     print("Author: ", row[2])
            #     print("Publication: ", row[3])
            #     print("Book Type:",row[4])
            #     print("Number of Available Books", row[5])
            #     print("\n")
            conn.commit()
            #mycursor.execute("insert into books(titleofbook,author,publication,booktype)values(%s,%s,%s,%s)",(titleofbook, author,publication,bookcategory))
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from books table {}".format(error))
        conn.close()
        return 


    def ModifyBookDetails(bookid,updatelistDict):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            query = "update books set {} where bookid = {}".format(', '.join('{}=%s'.format(k) for k in updatelistDict),bookid)
            values = []
            values = list(updatelistDict.values())
            mycursor.execute(query, values)
            conn.commit()
            mycursor.execute("select * from books")
            records = mycursor.fetchall()
            print (tabulate(records, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from books table {}".format(error))
        conn.close()
        return

    def displayuserlistToDelete():
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            mycursor.execute("select username, phone, usertype from users")
            records = mycursor.fetchall()
            print (tabulate(records, headers=["User Name","Phone","User Type"]))
            # for row in records:
            #     print("User Name: ", row[0])
            #     print("Phone: ",row[1])
            #     print("usertype: ",row[2])
                # print("User Name | \t\t Phone | \t\t User Type\n")
                # print(str(row[0]) +" | \t\t "+ str(row[1]) +" | \t\t "+ str(row[2]) +"\n")
            conn.commit()
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from user table {}".format(error))
        conn.close()
        return

    def addbooknos(bookid,cnt):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            #if conn.is_connected():
                #print('Connected to MySQL database')
               # conn._buffered = True
            mycursor = conn.cursor()
            print("bookid:",bookid)
            print("Count:",cnt)
            check_if_exists_bookid = 0
            mycursor.execute("SELECT count(*) FROM books where bookid = %s",(bookid,))
            ((row,),) = mycursor.fetchall() 
            print(row)
            check_if_exists_bookid = row
        
            if check_if_exists_bookid > 0:
                print("\nBefore adding books")
                mycursor.execute("select * from books")
                record = mycursor.fetchall()
                print (tabulate(record, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
                mycursor.execute("update books set numberofbooks = numberofbooks+%s where bookid = %s",(cnt,bookid))
                conn.commit()
                print("\n Books count increased...")
                print("\nAfter adding books")
                mycursor.execute("select * from books")
                records = mycursor.fetchall()
                print (tabulate(records, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            else:
                print("Given bookid doesn't exist...")
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from books table {}".format(error))
        conn.close()
        return

    def UserToDelete(userid):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            #mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
            #mycursor.fetchall()
            check_if_exists_username = 0
            print(userid)
            mycursor.execute("SELECT count(*) FROM users where username = %s",(userid,))
            ((row,),) = mycursor.fetchall() 
            #print(row)
            check_if_exists_username = row
            if check_if_exists_username != 0:
                mycursor.execute("Delete from users where username = %s",(userid,))
                print("\n User deleted...")
            else:
                print("Given user name doesn't exist...")            
            #((row,),) = mycursor.fetchall() 
            conn.commit()
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from user table {}".format(error))
        conn.close()
        return
    
    def BookToDelete(bookid):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            #mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
            #mycursor.fetchall()
            check_if_exists_book = 0
            #print(check_if_exists_book)
            mycursor.execute("SELECT count(*) FROM books where bookid = %s",(bookid,))
            ((row,),) = mycursor.fetchall() 
            #print(row)
            check_if_exists_username = row
            if check_if_exists_username != 0:
                mycursor.execute("Delete from books where bookid = %s",(bookid,))
                print("\n Book deleted...")
                conn.commit()
                mycursor.execute("select * from books")
                record = mycursor.fetchall()
                print (tabulate(record, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            else:
                print("Given bookid doesn't exist...")            
            #((row,),) = mycursor.fetchall() 
            conn.commit()
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from books table {}".format(error))
        conn.close()
        return

    def Lendbook(username,bookid):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            #mycursor.execute("SET SQL_SAFE_UPDATES = 0;")
            #mycursor.fetchall()
            check_bookid_exists = 0
            mycursor.execute("SELECT count(*) FROM books where bookid = %s",(bookid,))
            ((row,),) = mycursor.fetchall() 
            #print(row)
            # mycursor.execute("select * from books")
            # record = mycursor.fetchall()
            # print (tabulate(record, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
            check_bookid_exists = row
            if check_bookid_exists != 0:            
                check_if_book = 0
                # print(check_if_exists_book)
                mycursor.execute("SELECT numberofbooks FROM books where bookid = %s",(bookid,))
                ((row,),) = mycursor.fetchall() 
                #print(row)
                check_if_book = row
                if check_if_book == 0:
                    print(f"The count of the book with bookid {bookid} is zero. please check after some days.")
                #print(username)
                if check_if_book > 0:
                    mycursor.execute("select user_name,bookid from rented_details where user_name = %s and bookid =%s",(username,bookid))
                    exec = mycursor.fetchall()
                    print(exec)
                    print(len(exec))
                    if len(exec)>0:
                        print(f"\nThe bookid {bookid} is already rendered for the user {username}... \nPlease try different bookid for the user {username}")
                    else:
                        mycursor.execute("update books set numberofbooks = numberofbooks-1 where bookid = %s",(bookid,))
                        conn.commit()
                        print("\n Book Rendered...")
                        current_time = datetime.datetime.now()
                        # print(current_time)
                        renteddate = current_time.strftime("%Y-%m-%d")
                        # print(renteddate)
                        days20fromnow = datetime.datetime.now() + relativedelta(days=20)
                        # print(days20fromnow)
                        duedate = days20fromnow.strftime("%Y-%m-%d")
                        # print(duedate)
                        actualreturneddate = duedate
                        # print(actualreturneddate)
                        fee = 0
                        # print(fee)
                        rentedORreturned = 'Rented'
                        # print(rentedORreturned)
                        # phone = mycursor.execute("select phone from users where user_name=%s",(username,))
                        # print(mycursor.execute("select phone from users where user_name=%s",username,))
                        mycursor.execute("""insert into rented_details (user_name,bookid,renteddate,duedate,actualreturneddate,fee,rentedORreturned) 
                        values (%s,%s,%s,%s,%s,%s,%s)""",(username,bookid,renteddate,duedate,actualreturneddate,fee,rentedORreturned))
                        # print(mycursor.execute("""insert into rented_details (user_name,bookid,renteddate,duedate,actualreturneddate,fee,rentedORreturned) 
                        # values (%s,%s,%s,%s,%s,%s,%s)""",(username,bookid,renteddate,duedate,actualreturneddate,fee,rentedORreturned)))
                        conn.commit()
                        mycursor.execute("select * from books")
                        record = mycursor.fetchall()
                        print (tabulate(record, headers=["Book id","Title of Book","Author","Publication","Book Type","Number of books"]))
                            # #((row,),) = mycursor.fetchall() 
                    conn.commit()       
                else:
                    print(f"Given bookid {bookid} not present")

            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from rented details table {}".format(error))
        conn.close()
        return
    def Renderedlist(username):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            print(username)
            check_user = 0
            un = [username]
            rentedORreturned = 'Rented'
            mycursor.execute("SELECT count(*) FROM `rented_details` where `user_name` = %s and `rentedORreturned` = %s ",(username,rentedORreturned))
            ((row,),) = mycursor.fetchall() 
            print(row)
            check_user = row
            if check_user > 0:  
                mycursor.execute("select `user_name`,`bookid`,`renteddate`,`duedate`,`fee`,`rentedORreturned` from rented_details where `user_name` = %s and `rentedORreturned` = %s ",(username,rentedORreturned))
                record = mycursor.fetchall() 
                print (tabulate(record, headers=["User Name","bookid","Rented Date","Due date","Fee","Rented or Returned"]))
                # for row in record:
                #     print("User Name: ", row[0])
                #     print("bookid: ",row[1])
                #     print("Rented Date: ",row[2])
                #     print("Due date : ",row[3])
                #     print("Fee : ",row[4])
                #     print("Rented or Returned : ",row[5])
            conn.commit()       
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from rented details table {}".format(error))
        conn.close()
        return
    
    def ReturnBooks(username,bookid):
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='MySQL@2')
            # if conn.is_connected():
            #     print('Connected to MySQL database')
            mycursor = conn.cursor()
            print(username)
            check_user = 0
            un = [username]
            # mycursor.execute("""select books.bookid, books.titleofbook, books.author,rented_details.user_name,
            #                 rented_details.renteddate,rented_details.duedate,
            #                 rented_details.fee,rented_details.rentedORreturned 
            #                 from books inner join rented_details  
            #                 on books.bookid = rented_details.bookid and rented_details.user_name = %s """,(username,))
            # reco = mycursor.fetchall() 
            # print (tabulate(reco, headers=["Book id", "Book Title", " Author" ,"User Name","renteddate","duedate","fee","rentedORreturned"]))
                
            mycursor.execute("SELECT count(*) FROM `rented_details` where `user_name` = %s",(username,))
            ((row,),) = mycursor.fetchall() 
            # print(row)
            check_user = row
            if check_user > 0:  
                current_time = datetime.datetime.now().date()
                actualreturneddate = current_time.strftime("%Y-%m-%d")
                print(type(actualreturneddate))
                mycursor.execute("select duedate from rented_details where user_name = %s and bookid = %s",(username,bookid))
                ((dd,),) = mycursor.fetchall()
                # print(dd)
                # print("dd type",type(dd))
                # ddtodate = datetime.datetime.strptime(dd, '%Y-%m-%d')
                # print(ddtodate)
                rentedORreturned = 'Returned'
                mycursor.execute("update rented_details set `actualreturneddate` = %s,rentedORreturned = %s where `bookid` = %s",(actualreturneddate,rentedORreturned,bookid))
                conn.commit()
                mycursor.execute("update books set numberofbooks = numberofbooks+1 where bookid = %s",(bookid,))
                conn.commit()
                act_ret = datetime.datetime.strptime(actualreturneddate, '%Y-%m-%d').date()
                # print(type(act_ret))
                # print(act_ret)
                if (act_ret > dd):
                    f = 20
                    diff = (act_ret - dd).days
                    # print(diff)
                    diff = diff-1
                    fi=20
                    if diff>0 and diff<5:
                        mycursor.execute("update rented_details set `fee` = %s where `bookid` = %s and `user_name` = %s",(f,bookid,username))
                        conn.commit()
                    if diff>0 and diff>=5:
                        fine = 20
                        for i in range(int(diff/5)):
                            fi = fi+5
                            fine = fine+fi
                            diff =diff-5
                        #     print("FI", fi)
                        #     print("Fine" ,fine)
                        #     print("Diff",diff)
                        # print(fine)
                        mycursor.execute("update rented_details set `fee` = %s where `bookid` = %s and `user_name` = %s",(fine,bookid,username))
                        conn.commit()
                mycursor.execute("select `user_name`,`bookid`,`renteddate`,`duedate`,`fee`,`rentedORreturned` from rented_details where `user_name` = %s",(username,))
                record = mycursor.fetchall() 
                print (tabulate(record, headers=["User Name","bookid","renteddate","duedate","fee","rentedORreturned"]))
                # for row in record:
                #     print("User Name: ", row[0])
                #     print("bookid: ",row[1])
                #     print("Rented Date: ",row[2])
                #     print("Due date : ",row[3])
                #     print("Fee : ",row[4])
                #     print("Rented or Returned : ",row[5])
            conn.commit()       
            mycursor.close()
        except mysql.connector.Error as error:
            print("Failed to List the details from rented details table {}".format(error))
        conn.close()
        return