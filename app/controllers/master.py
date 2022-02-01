
import uuid
class Master:

    def set_user_id(self):
        global user_id
        user_id = uuid.uuid1()

    def get_user_id(self):
        return user_id