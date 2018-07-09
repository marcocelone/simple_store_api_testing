import requests
import json
from helpers import setup


class REQ():

    def __init__(self):

        self.req = requests.Session()

    def get(self, endpoint, my_token):
        """
        This method is used to make a GET Rest request the token and the endpoint are needed
        """
        jwt_token = 'JWT ' + my_token
        request_header = {'Authorization': jwt_token}
        result = self.req.get(setup.base_url+endpoint, headers=request_header)
        rs_code = result.status_code
        rs_body = result.json()
        #assert rs_code == 200, "Invalid Response Code {} cannot get Roles".format(rs_code)
        #print(rs_code, rs_body)

        return [rs_code, rs_body]

    def post_new_store(self, endpoint, storename, my_token):
        """
        This method is used to make a POSt Rest request to create a new store the token and the endpoint and store name are needed
        """
        jwt_token = 'JWT ' + my_token
        request_header = {'Authorization': jwt_token}
        result = self.req.post(setup.base_url+endpoint+storename, headers=request_header)
        rs_code = result.status_code
        rs_body = result.json()
        store_id = rs_body['store_id']

        print("I am the store body {}".format(rs_body))

        return [rs_code, rs_body, store_id]

    def post(self, endpoint, itemname, payload, my_token):
        """
        This method is used to make a GET Rest request the token and the endpoint are needed
        """
        jwt_token = 'JWT ' + my_token
        request_header = {'Authorization': jwt_token}
        result = self.req.post(setup.base_url+endpoint+itemname, headers=request_header, data=payload)
        rs_code = result.status_code
        rs_body = result.json()

        print("I am the item body {}".format(rs_body))
        return [rs_code, rs_body]

    def put(self, endpoint, payload,  my_token):
        """
        This method is used to make a GET Rest request the token and the endpoint are needed
        """
        jwt_token = 'JWT ' + my_token
        request_header = {'Authorization': jwt_token}
        result = self.req.put(setup.base_url + endpoint, headers=request_header, data=payload)
        rs_code = result.status_code
        rs_body = result.json()

        return [rs_code, rs_body]

    def delete(self, endpoint, my_token):
        """
        This method is used to DELETE Rest request the token and the endpoint are needed
        """
        jwt_token = 'JWT ' + my_token
        request_header = {'Authorization': jwt_token}
        result = self.req.delete(setup.base_url + endpoint, headers=request_header)
        rs_code = result.status_code
        rs_body = result.json()

        return [rs_code, rs_body]
