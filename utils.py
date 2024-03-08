from os import getenv
from pyrogram.types.user_and_chats import User as PyrogramUser


class User(PyrogramUser):
    id: int = 0
    first_name: str = ''
    last_name: str = ''
    is_allowed: bool = False

    def __init__(self, chat):
        self.id = chat.id
        self.first_name = chat.first_name
        self.last_name = chat.last_name
        # Them check if user is allowed
        self.is_allowed = self.check_id_in_allowed_user_list()

    def check_id_in_allowed_user_list(self):
        # Read variable ALLOWED_USER_IDS from .env file
        allowed_user_ids = getenv('ALLOWED_USER_IDS', '').split(' ')
        # if user_id is not a string, convert it to string
        if not isinstance(self.id, str):
            self.id = str(self.id)
        # Check if user_id is in allowed_user_ids
        self.is_allowed = self.id in allowed_user_ids
        return self.is_allowed
