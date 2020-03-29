#Author:zyx
user,passwd = 'zyx','123456'
def auth(auth_type):
    print("auth func",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if user == username and passwd == password:
                print("\033[32;1mUser has passed auth\033[0m")
                res = func(*args, **kwargs)
                print("continue")
                return res
            else:
                exit("\033[31;1mInvalid username or password\033[0m")
        return wrapper
    return outer_wrapper

def index():
    print("Welcome to index")
@auth(auth_type='local')  # home = auth()
def home():
    print("Welcome to home")
    return "from home"
@auth(auth_type='ldep')
def bbs():
    print("Welcome to bbs")

index()
print(home())
bbs()
