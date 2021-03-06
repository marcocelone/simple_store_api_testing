import sys
import pytest
import json
from auth.create_user import Register
from request_models.requests_methods import REQ

print(sys.path)

register = Register('marco111', 'asdfgh')
req = REQ()

# creating our object to be used to make API call connections
#create_user = rq.create_user()
token = register.get_token()
my_token = token[1]
access_token = my_token["access_token"]
storename = 'teststore1'
itemname = 'pen1'


def test_put_new_item():

    create_store = req.post_new_store('store/', storename, access_token)
    store_response_code = create_store[0]
    store_response_body = create_store[1]
    store_id = create_store[2]
    payload = {
        'price': 30.99,
        'store_id': store_id}

    payload_update = {
        'price': 30.99,
        'store_id': store_id}

    print("payload is {} ".format(payload))

    if store_response_code ==400:
        print("Invalid Response {} Expected 400".format(store_response_body))
    else:
        assert store_response_code == 201, "Invalid Response {} Expected 201".format(store_response_body)

    create_item = req.put('item/'+itemname, payload, access_token)
    item_response_body = create_item[1]
    item_response_code = create_item[0]
    if item_response_code == 400:
        print("Invalid Response {} Expected 400".format(item_response_body))
    else:
        assert item_response_code == 200, "Invalid Response {} Expected 201".format(item_response_code)

    update_item = req.put('item/'+itemname, payload_update, access_token)
    update_response_body = update_item[1]
    item_response_code = update_item[0]
    if item_response_code == 400:
        print("Invalid Response {} Expected 400".format(update_response_body))
    else:
        assert item_response_code == 200, "Invalid Response {} Expected 201".format(item_response_code)

    delete_item = req.delete('item/'+itemname, access_token)
    delete_item_code = delete_item[0]
    delete_item_body = delete_item[1]
    assert delete_item_code == 200, "Invalid Response {} Expected 200".format(delete_item_body)

    delete_store = req.delete('store/'+storename, access_token)
    delete_store_response = delete_store[0]
    delete_store_body = delete_store[1]
    assert delete_store_response == 200, "Invalid Response {} Expected 200".format(delete_store_body)


if __name__ == "__main__":
    test_put_new_item
   # pytest.main()