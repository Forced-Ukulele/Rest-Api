from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    User = UserModel.find_by_username(username)
    if User and safe_str_cmp(User.password,password):
        return User

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
