
class Animal:
    def __init__(self, name):
        self.name = name  # Save the animal's name

    def speak(self):
        print("Animal speaks")  # Generic speak method

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} says Woof!")  # Dog's own speak method

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print(f"{self.name} says Meow!")

dog1 = Dog("Buddy")  # Create a Dog named Buddy
dog1.speak()        # Output: Buddy says Woof!

cat1 = Cat("Whiskers")  # Create a Cat named Whiskers
cat1.speak()  # Output: Whiskers says Meow!





## Q.1 Student Record System

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"{self.name}, {self.roll_no}, {self.marks}")

s1 = Student("Akash", 101, 87)
s2 = Student("Amit", 102, 91)
s3 = Student("Akshay", 103, 95)
s4 = Student("Nilesh", 104, 92)

students = [s1,s2,s3,s4]

def get_topper(students):
    topper = students[0]
    for student in students:
        if student.marks > topper.marks:
            topper = student
    return topper
top_student = get_topper(students)
print("Topper:")
top_student.display()



## Q2: Employee Salary System with Encapsulation and Property Decorators

class Employee:
    def __init__(self, name, salary):
        self.__name= name
        self.__salary = salary
    def display(self):
        print(f"{self.__name}, {self.__salary}")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 10000:
            raise ValueError("Salary must be at least 10,000")
        self.__salary = value

emp = Employee("Ravi", 15000)
emp.display()  # Should print: Ravi, 15000

print(emp.salary)  # Should print: 15000

emp.salary = 20000  # Should update salary
print(emp.salary)   # Should print: 20000

emp.salary = 9000   # Should raise ValueError



## Q3: Bank Account Management System

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")
# Step 1: Create a bank account object
acc1 = BankAccount("Akash", 5000)

# Step 2: Deposit money into it
acc1.deposit(10000)

# Step 3: Display account info
acc1.display()  # Output: Account Holder: Ravi, Balance: 15000

# Step 4: Withdraw money
acc1.withdraw(5000)

# Step 5: Display again
acc1.display()  # Output: Account Holder: Ravi, Balance: 10000

    

## Q4: Implement a Library System

# Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

# Library class that inherits from Book (not strictly necessary but for OOP demo)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} added to the library.")

    def display_books(self):
        print("\n📚 Available Books in Library:")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"✅ You borrowed '{book.title}'.")
                return
        print("❌ Book not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"✅ You returned '{book.title}'.")
                return
        print("⚠️ Book not found or already returned.")

# --- Using the classes ---

# Create library
my_library = Library()

# Add books
book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("1984", "George Orwell")
book3 = Book("Python Programming", "Guido van Rossum")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Display books
my_library.display_books()

# Borrow a book
my_library.borrow_book("1984")

# Display again
my_library.display_books()

# Try borrowing same book again
my_library.borrow_book("1984")

# Return the book
my_library.return_book("1984")

# Final state
my_library.display_books()


## Q. Shape Area Calculator using Polymorphism
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def shape_name(self):
        return "Rectangle"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def shape_name(self):
        return "Triangle"

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def shape_name(self):
        return "Circle"

# Polymorphic function
def print_area(shape):
    print(f"{shape.shape_name()} Area: {shape.area()}")

# Create shape objects
rect = Rectangle(10, 5)
tri = Triangle(8, 6)
circle = Circle(7)

# Print areas
print_area(rect)     # Rectangle Area: 50
print_area(tri)      # Triangle Area: 24.0
print_area(circle)   # Circle Area: 153.938...



## Bank Account Withdrawal with Exception Handling

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
         raise ValueError("Insufficient funds")
        else:
            self.balance -= amount

    def display(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

acc = BankAccount("Akash", 5000)
try:
    acc.withdraw(6000)
except ValueError as e:
    print(e)  # This will print "Insufficient funds" if balance is less
acc.display()


