class Person:
    public_book=[]
    student_book=[]
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password

class Admin(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
    def add_books(self,book):
        self.book=book
        self.coustom_book=vars(book)
        self.public_book.append(self.coustom_book)
    def show_available_book(self):
        print(self.public_book)

    
class User(Person):
    book_list=[]
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
    def show_available_book(self):
        print(self.public_book)
    def take_book(self,name1):
        print("the name is: ",name1)
        for i in range(0,len(self.public_book)):
            #print(self.public_book[i])
            value_1=self.public_book[i]
            for key in value_1:
                 #print(value_1[key])
                 if value_1[key]==name1:
                     #print(value_1[key])
                     self.book_list.append(value_1[key])
    def show_my_book_list(self):
        print(self.book_list)

                

class Book:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity
while(True):
    input1=int(input("Press 1 for Create Account As A Admin:\nPress 2 for Create Account As A User:\nPress 3 for Exit:\n"))

    if input1==1:
        print("Enter Your Email and Password:")
        input2=input("Enter Your Email: ")
        input3=input("Enter Your Password: ")
        input4=int(input("Enter 1 for login:\nEnter 2 for Exit:\n"))
        if input4==1:
            input5=input("Enter Your Email: ")
            input6=input("Enter Your Password: ")
            if input2==input5 and input3==input6:
                print("Dear Admin Congratulation: ")
                while(True):
                    input7=int(input("Enter 1 for Add Book:\nEnter 2 for Show Book:\nEnter 3 for logout:\n"))
                    if input7==1:
                        call_admin_class=Admin('hafiz@gmail.com','1e2f')
                        input_book=input("Enter book name: ")
                        input_price=int(input("Enter book price: "))
                        input_quantiry=int(input("Enter book quantity: "))
                        call_book_class=Book(input_book,input_price,input_quantiry)
                        call_admin_class.add_books(call_book_class)
                    elif input7==2:
                        call_admin_class.show_available_book()
                    else:
                        print("Enter Your Email and Password for logout: ")
                        emi=input("Enter Your Email: ")
                        pas=input("Enter Your Passwor: ")
                        if emi==input5 and pas==input6:
                            break

        else:
            break      
    
    elif input1==2:
        print("Enter Your Email and Password for Create Account:")
        email1=input("Enter Your Email: ")
        password1=input("Enter Your Password: ")
        check=int(input("Press 1 for Login:\nPress 2 for Exit:\n"))
        if check==1:
            email2=input("Enter Your Email: ")
            password2=input("Enter Your Password: ")
            if email1==email2 and password1==password2:
                print("Welcome To Our Library:")
                while(True):
                    run=int(input("Enter 1 for Show available book:\nEnter 2 for Collect book:\nEnter 3 for show book:\nEnter 4 for Exit:\n"))
                    if run ==1:
                        call_user_class=User('hafiz','123234')
                        call_user_class.show_available_book()

                    elif run==2:
                        name1=input("Enter Your Book Name: ")
                        call_user_class.take_book(name1)
                    elif run==3:
                        call_user_class.show_my_book_list()
                    else:
                        break


    
    else:
        break
