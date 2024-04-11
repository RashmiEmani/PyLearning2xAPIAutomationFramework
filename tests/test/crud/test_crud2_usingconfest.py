import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCrudBooking(object):

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description("Verify that Full Update with the booking ID and Token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(url=put_url,
                               headers=Util().common_headers_put_delete_patch_cookie(token=token),
                               payload=payload_create_booking(),
                               auth=None,
                               in_json=False
                               )
        print(response.json())
        # verifications here & more
        verify_response_key_should_not_be_none(response.json()["firstname"])
        verify_response_key_should_not_be_none(response.json()["lastname"])
        verify_response_key(response.json()["firstname"], "Rashmi")
        verify_response_key(response.json()["lastname"], "Emani")
        verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Test CRUD operation Delete(DELETE)")
    @allure.description("Verify that booking gets deleted with the booking ID and Token")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(url=delete_url,
                                  headers=Util().common_headers_put_delete_patch_cookie(token=token),
                                  auth=None,
                                  in_json=False
                                  )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expect_data=201)
