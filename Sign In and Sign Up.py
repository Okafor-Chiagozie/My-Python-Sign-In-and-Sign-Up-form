class New_To_Website:
    def First(self):
        print("Press '1' for Sign_In   or ")
        print("Press '2' for Sign_Up")
        print()
        self.choice = int(input("Make a choice: "))
        
    def Sign_In(self):
        self.email = input("Your email or phone-number: ")
        self.password = input("Your password: ")
        
    def Sign_Up(self):
        self.firstname = input("Your Firstname: ")
        self.lastname = input("Your Lastname: ")
        print()
        print("Hello " + self.firstname + " " + self.lastname)
        print()
        self.email = input("Type in your email or phone-number: ")
        self.place = input("Which country are you from?: ")
        self.password = input("Create a password: ")
        self.confirm = input("Confirm password: ")
        
new = New_To_Website()


Website = "Yes"

if Website == "Yes":
    new.First()
    if new.choice == 1:
        new.Sign_In()
        print()
        print("Hello Fam ❤")
    elif new.choice == 2:
        age = int(input("Enter your age: "))
        if age >= 18:
            new.Sign_Up()
            if new.confirm == new.password:
                print()
                print("Welcome " + new.firstname + " " + new.lastname + " to Our Wonderful Website ❤")
            elif new.confirm != new.password:
                print()
                print("Your password dosen't match!!")
        else:
            print()
            print("Next time kiddo!!")
    else:
        print()
        print("")
