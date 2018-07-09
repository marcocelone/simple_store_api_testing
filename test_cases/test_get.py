import sys
import pytest
from auth.create_user import Register
from request_models.requests_methods import REQ

print(sys.path)

register = Register('marco111', 'asdfgh')
req = REQ()

# creating our object to be used to make API call and db connections
#create_user = rq.create_user()
token = register.get_token()
my_token = token[1]
access_token = my_token["access_token"]


    #@attr(priority="high")
def test_verify_items():

    item_list = req.get('items',access_token)
    response_body = item_list[1]
    response_code = item_list[0]
    assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
    #print(response_body, response_code)

if __name__ == "__main__":
    pytest.main()
