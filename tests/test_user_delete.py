from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):

    def test_delete_user_with_id_2(self):
        
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")
        response2 = MyRequests.delete(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_json_has_key(response2, "error")
        Assertions.assert_json_value_by_name(response2, "error", "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", "Unexpected error message")

    def test_delete_new_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_has_key(response3, "success")
        Assertions.assert_json_value_by_name(response3, "success", "!", "Unexpected error message")

        #GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == "User not found", f"Unexpected response content {response4.content}"

    def test_delete_under_another_user(self):
        # REGISTER 
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        user_id_to_delete = self.get_json_value(response1, "id")

        

        #REGISTER 2
        register_data2 = self.prepare_registration_data()
        register_data2['email'] = '1'+register_data2['email']
        response2 = MyRequests.post("/user/", data=register_data2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = register_data2['email']
        password = register_data2['password']

        login_data = {
            'email': email,
            'password':password 
        }

        response3 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        response4 = MyRequests.delete(f"/user/{user_id_to_delete}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 400)
        Assertions.assert_json_has_key(response4, "error")
        Assertions.assert_json_value_by_name(response4, "error", "This user can only delete their own account.", "Unexpected error message")