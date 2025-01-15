class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    @property
    def password(self):
        return "******"  # Masked password

user = User("john_doe", "secure123")

print(f"username: {user.username}, password: {user.password}")
