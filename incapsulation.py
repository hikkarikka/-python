class User:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self.__pasword = "123"

    def get_password(self):
        return self.__pasword
    
    
    def set_password(self, new_pass):
        if len(new_pass) >= 8:
            self.__pasword = new_pass
        else:
            print("пароль должен быть длинее 8 символов")


user = User("Alex", 2000)
print(user.name)
print(user._balance)
print(user.get_password())
user.get_password("345")
print(user.get_password())