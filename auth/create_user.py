import requests
import json


class Register():

    """
    This class is used to create a user and get an auth token. It will create the object using the hardcoded
    login & Password.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.body_credentials = json.dumps({'username': self.username, 'password': self.password})

        self.req = requests.Session()
        self.base_url = 'http://127.0.0.1:5000/'
        self.token_url = self.base_url + 'auth'

        self.register_url = 'register'
        self.headers = {'Content-Type': 'application/json'}

    def create_user(self):
        user = self.req.post(self.base_url+'register', headers=self.headers, data=self.body_credentials)
        print(user)
        response_code = user.status_code
        response_boby = user.json()
        expected_response_body = {'message': 'User already exist!'}
        if response_boby == expected_response_body:
            assert response_code != 400, "User Already Exist Try Again"
        else:
            assert response_code == 201, "Invalid Response Code User not Created"

        return [response_code, response_boby]

    def get_token(self):

        """
        This method is used to make a get a token
        """
        token = self.req.post(self.token_url, headers=self.headers, data=self.body_credentials)
        response_code = token.status_code
        response_boby = token.json()
        print(response_boby, response_code)
        assert response_code == 200, "Invalid Response Code, Token not Created {}".format(response_code)

        return [response_code,response_boby]




