from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):

    def setup_method(self):
        # REGISTER
        self.register_data = self.prepare_registration_data()
        self.response1 = MyRequests.post("/user/", data=self.register_data)

        Assertions.assert_code_status(self.response1, 200)
        Assertions.assert_json_has_key(self.response1, "id")

        self.email = self.register_data['email']
        self.first_name = self.register_data['firstName']
        self.password = self.register_data['password']
        self.user_id = self.get_json_value(self.response1, "id")

    def test_edit_just_created_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        #GET
        response4 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    def test_edit_while_unauthorized(self):
        #EDIT
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"/user/{self.user_id}",
            data={"firstName": new_name}
        )
        Assertions.assert_json_has_key(response2, "error")
        Assertions.assert_json_value_by_name(
            response2,
            "error",
            "Auth token not supplied",
            "Unexpected error message"
        )
        Assertions.assert_code_status(response2, 400)

    def test_edit_while_authorized_with_another_user(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{int(self.user_id)-1}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_has_key(response3, "error")
        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "This user can only edit their own data.",
            "Unexpected error message"
        )

    def test_edit_email_without_at_symbol(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_email = self.email.replace('@','') 

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_has_key(response3, "error")
        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "Invalid email format",
            "Unexpected error message"
        )

    def test_edit_username_on_short(self):
        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_username = 'a' 

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data={"username": new_username}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_has_key(response3, "error")
        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "The value for field `username` is too short",
            "Unexpected error message"
        )