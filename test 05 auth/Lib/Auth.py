import uuid


class Auth:
    def __init__(self):
        self.users = {
            "john_doe": {
                "password": "password123",
                "uuid": "12345678-1234-5678-1234-567890abcdef"
            }
        }
        self.authorized_users = {}

    def authenticate(self, login, password, user_uuid):  # Changed argument name to user_uuid
        # Check if there is a user with the same username and password
        if login in self.users and password == self.users[login]["password"] and user_uuid == self.users[login]["uuid"]:
            # Generate and store an authorization token
            token = str(uuid.uuid4())
            self.authorized_users[token] = login
            return token
        else:
            raise Exception("Invalid username, password or UUID")

    def check_purchase_page_access(self, token):
        # Check if the token is valid
        if token in self.authorized_users:
            # Check if there is access to the page for buying goods
            if self.authorized_users[token] == "john_doe":
                return True
            else:
                return False
        else:
            raise Exception("Access Denied")