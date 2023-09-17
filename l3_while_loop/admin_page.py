def load_admin_page():
    print("please enter your login and password")

    login = input("Enter your login:")
    password = input("Enter your password:")
    print("login = " + login + " password = " + password)


    def login_password_check(log, pas):
        # This is a function
        return login == log and password == pas


    if (login_password_check("andrew", "qwe123")
            or login_password_check("kevin", "asd456")
            or login_password_check("julia", "zxc789")
            or login_password_check("alex", "poi098")
            or login_password_check("helen", "lkj765")):
        print('Welcome to admin page ' + login)
    else:
        print("Wrong login or password")
