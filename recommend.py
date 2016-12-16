#Name: Daniel K Rono. #Class of 2016.  #Fourth Programming Assignment.

def main():

    openbooks = open('books.txt','r')                           #Opens and reads the books.txt file
    
    bookstuple = tuple(openbooks)                               #Stores the contents of the books.txt file in a tuple.

    openratings = open('ratings.txt','r')                       #Opens and reads the ratings.txt file

    ratingslist = list(openratings)                             #Stores the contents of the ratings.txt file in a list.

    printbooks = input("Welcome! If you would you like to see our titles, enter 1. If not, press 2: ")  #Gives the user the option of seeing the books in the books.txt file.

    if printbooks == "1":
        print ("BOOKLIST: Author, Title")
        books()                                     #Calls the books() function which prints out the contents of the books.txt file.
        
    else:
        print ("Thanks for your feedback.")

    rate = input("If you would like to rate the books in our list, enter 1. If not, press 2: ") # Requests the user to rate the books he/she has seen from the list.

    if rate == "1":
        ratings()               #Calls the ratings() function which is designed to get the user to rate the books.

    else:
        print ("Thanks for your feedback.")

    openbooks.close()           #Closes the books.txt file       
    openratings.close()         #Closes the ratings.txt file.

def books():
    
    openbooks = open('books.txt','r')

    b = 1
    while b <= 35:
        book = openbooks.readline()     #This while-loop iterates over the lines in the books.txt file and prints the books.
        print (book)
        b += 1

    openbooks.close()

def ratings():

    openbooks = open('books.txt','r')

    bookstuple = tuple(openbooks)

    username = input("Please enter your username: ")

    print("Please rate the titles in the list. The scale ranges from -3(if you really hated it) to 3(if you really liked it). If you haven't read the book enter zero(0).") #Instructions on rating the books.

    userlist = []               #Creates a list into which the user is supposed to enter his/her ratings.
        
    for line in openbooks:          #This for-loop is designed to iterate over each book in the list and ask the user to rate it, but I haven't managed to get it to work. I considered using a dictionary
        parts = line.split(',')     #which would allow me to refer to a book as the value in the key-value pair, but then the need for a strict sequence obliged me to use the list called "userlist" and
        userrating = input("Please rate ",parts[1]," :")  #append each rating at its end with every iteration. Unfortunately, I've not been able to get this loop to work. My plan was to use "userlist" as 
        userlist = userlist.append(userrating)            #the value in the "ratingsdict" dictionary and "username" as the key for the rating supplied by the user.
    print(userlist)

    openratings = open('ratings.txt','r')

    ratingslist = list(openratings)
    
    bookdict = dict()       

    ratingsdict = dict()

    for line in openbooks:
        parts = line.split(',')
        bookdict [parts[0]] = parts[1]   #Builds the "bookdict" dictionary containing the books and their respective authors.

    user = 0
    while user < len(ratingslist):
        name = ratingslist[user]
        rating = user + 1
        opinion = ratingslist[rating]    #Builds the "ratingsdict" dictionary containing the names of each user and their respective ratings of each book.
        ratingsdict[name] = opinion
        user += 2

    openbooks.close()
    openratings.close()
                   
main()
