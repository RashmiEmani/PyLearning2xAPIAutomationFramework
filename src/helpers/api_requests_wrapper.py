# To Make the POST, PUT, PATCH, DELETE, GET
# You can create by class or functions

import json
import requests


def get_request(url, auth):
    get_response = requests.get(url=url, auth=auth)
    return get_response.json()


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:  # this statement is optional, added to make it generic
        return post_response.json()
    return post_response
    # json.dumps means whatever the payload setting it as a dictionary, it is get converted into json
    # because while making create request it should be in json
    # json.dumps means always covert data or payload into pure json
    # in_json used for boolean json data


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


def delete_request(url, auth, headers, in_json):
    delete_response = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_response.json()
    return delete_response
