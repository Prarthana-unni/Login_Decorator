
#      Assignment 7 - Logging Decorator
#     Build a Python program using a custom login_required decorator to control access to different functions based onuser authentication.
#     Requirements:
# ●	Create a login_required decorator that checks whether the user is logged in before allowing access to a function.
# ●	Use the username “quest” and password “quest123” as the valid login credentials.
# ●	Create a login function that accepts the username and password from the user.
# ●	If the credentials are correct, display a login successful message and allow access to protected functions.
# ●	Create functions such as Home, About, and Profile.
# ●	Apply the login_required decorator only to functions that require authentication.
# ●	A function without the login_required decorator should work normally without login.
# ●	A function with the login_required decorator should not execute unless the user has successfully logged in.
# ●	If an unauthenticated user tries to access a protected function, display an appropriate access denied/login required message.
# ●	Demonstrate the difference between normal functions and decorator-protected functions.
# ●	Use a menu-driven program to allow the user to access the available functions. 



logged_in = False


def login():
    global logged_in

    uname = input("Enter the username: ")
    password = input("Enter the password: ")

    if uname == "quest" and password == "quest123":
        print("Login successful")
        logged_in = True
    else:
        print("Invalid username or password")


def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access denied. Please login first.")
    return wrapper


def home():
    print("Welcome Home")


def about():
    print("Welcome About")


@login_required
def profile():
    print("Welcome Profile")


while True:
    print("\n----- MENU -----")
    print("1. Login")
    print("2. Home")
    print("3. About")
    print("4. Profile")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login()

    elif choice == "2":
        home()

    elif choice == "3":
        about()

    elif choice == "4":
        profile()

    elif choice == "5":
        print("Program exited")
        break

    else:
        print("Invalid choice")