
##initial statement for welcoming the user to the store

a="Welcome to My Book Store"
x=a.center(80,'-')
print(x)


##stored data

ns =[["Pst",90,5],["Sindhi",120,5],["Urdu",110,10],["English",130,0],["Physics",90,0],["Chemistry",90,0],["Biology",120,0],["Computer",100,0],["Maths",135,10]]
ng =[["Islamiat",90,10],["English",130,5],["Science",100,10],["Maths",135,5]]

ms =[["Islamiat",90,10],["English",130,5],["Physics",90,5],["Chemistry",90,6],["Biology",120,7],["Computer",100,10],["Maths",135,10]]
mg =[["Islamiat",90,0],["English",130,0],["Physics",90,5],["Chemistry",90,0],["Biology",120,0],["Computer",100,0],["Maths",135,10]]

es =[["Islamiat",90,3],["English",130,5],["Physics",90,0],["Chemistry",90,5],["Biology",120,0],["Computer",100,5],["Maths",135,10]]
ec =[["Islamiat",90,6],["English",130,0],["Physics",90,10],["Chemistry",90,10],["Biology",120,0],["Computer",100,0],["Maths",135,10]]


ts =[["Pst",90,5],["Urdu",110,5],["English",130,0],["Physics",90,5],["Chemistry",90,10],["Biology",120,0],["Computer",100,0],["Maths",135,0]]
tc =[["Islamiat",90,5],["English",130,5],["Physics",90,5],["Chemistry",90,0],["Biology",120,0],["Computer",100,10],["Maths",135,20]]



##global lists which is appended by the local lists

Book = []
Price = []
Discount = []


##function for searching in the lists 
def search(book):
    f = 0
    global Book
    global Price
    global Discount
    for i in range(len(l)):
            if(l[i][0]==book):
                price = l[i][1]
                discount = l[i][2]
                Book.append(book)
                Price.append(price)
                Discount.append(discount)
                f=1
                print("You have successfully purcahsed this book.")    
              
    if (f==0):
        print("Sorry, This book isn't available right now!" )
    
    
  

##asking for the queary from the user

def queary():
    global ns
    global ng
    global ms
    global mg
    global es
    global ec
    global ts
    global tc
    global l
    
    #To avoid alphabets
    while True:
        try:
            grade = int(input("Enter the book's grade : "))
            
            if(grade==9):
                False
                break
            elif(grade==10):
                False
                break
            elif(grade==11):
                False
                break
            elif(grade==12):
                False
                break
            elif grade!=9 or 10 or 11 or 12:
                print("Grade must be in range 9-12 and input must be an integer number.")         
        except:
            print("Input must be a number and in range 9-12.")
            
   #To avoid input other than expected groups         
    True
    while True:
        Group = str(input("Enter the group : "))
        group = Group.capitalize()
        if(group== "Science"):
            False
            break
        elif(group== "General"):
            False
            break
        elif(group== "Commerce"):
            False
            break
        elif(group!= "Science" or "General" or "Commerce"):
            print("Enter Science, General or Commerce.")
            
                                      
    book = str(input("Enter the name of the book, you want to buy : ")).capitalize()
    if(group=="Science" and grade==9):
        l = ns
        search(book)
    elif (group=="General" and grade==9):
        l=ng
        search(book)
    elif (group=="Science" and grade==10):
        l=ms
        search(book)
    elif  (group=="General" and grade==10):
        l=mg
        search(book)
    elif  (group=="Science" and grade==11):
        l=es
        search(book)
    elif  (group=="Commerce" and grade==11):
        l=ec
        search(book)
    elif  (group=="Science" and grade==12):
        l=ts
        search(book)
    elif  (group=="Commerce" and grade==12):
        l=tc
        search(book)


##function for providing the final sale receipt to the user
def slip():
        global Book
        global Price
        global Discount
        sum = 0
        n = len(Book)
        if(n==0):
            print("Thanks for visiting our store.")
        else:
            print()
            print("Your sale receipt!")
            print()
            print("-----------------------------------------")
            print("BOOK",'\t', '\t', "PRICE",'\t','\t', "DISCOUNT")
            print("-----------------------------------------")
            for i in range(n):
                
                if (Book[i]== "Pst"): 
                    print (Book[i],'\t','\t',"Rs",Price[i],'\t','          ',"Rs",Discount[i])
                    sum+= Price[i]
                    sum-= Discount[i]
                    continue
                if (Book[i]== "Urdu"):
                    print (Book[i],'\t','\t',"Rs",Price[i],'\t','  ',"Rs",Discount[i])
                    sum+= Price[i]
                    sum-= Discount[i]
                    continue
                if (Book[i]=="Maths"):
                    print (Book[i],'\t','\t',"Rs",Price[i],'\t','  ',"Rs",Discount[i])
                    sum+= Price[i]
                    sum-= Discount[i]
                    continue
                if (Book[i]!= "Pst" or "Urdu" or "Maths"):
                    print (Book[i],'\t',"Rs",Price[i],'\t','  ',"Rs",Discount[i])    
                    sum+= Price[i]
                    sum-= Discount[i]
                        

            print('\n')
            print("You total price of",n,"book(s):" , "Rs",sum, "Only")

        
##initializing the program from this piece of code

print("Do you want to shop? :")

while True:
    ini = str(input("Yes OR N0? : ")).capitalize()
    if(ini=="Yes"):
        name = str(input("Enter your name: ")).capitalize()
        queary()
        False
        break
    if (ini=="No"): 
        print("Thanks for visiting our store.")
        False
        break
    if(ini!="Yes" or "No"):
        print("Only input Yes or No")
        
    
##code for accepting more than one book shopping and providing the final sale receipt to the user
if(ini=="Yes"):  
    x = 0
    while(x==0):
        again = str(input("Do you want to buy any other book? Yes OR No?: ")).capitalize()
        if(again=="Yes"):
            queary()
        if(again=="No"):
            slip()
            x = 1
            if (len(Book)!=0):
                print("Thanks for shopping", name,'.')





                
        
        
    
        
                
            
            
        
        



