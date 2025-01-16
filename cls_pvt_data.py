class PrivateData:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

data = PrivateData("user1", "pass123")
print(f"username: {data.get_username()}, password: {data.get_password()}")
data.set_password("newpass123")
print(f"password: {data.get_password()}")