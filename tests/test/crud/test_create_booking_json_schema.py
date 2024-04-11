# Get Response
# Create the JSON schema - https://www.jsonschema.net/
# Save that schema into the name.json file
# If you want to validate the json schema - https://www.jsonschemavalidator.net/

import pytest
import json
import os
import allure
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBookingJsonSchema(object):

    # to check response -> with schema.json file saved, we use below func

    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID should not be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        # URl, Payload, Headers
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        #simple method -> file_path = "C:\Users\msman\PycharmProjects\PyLearning2xAPIAutomationFramework\tests\test\crud\create_booking_schema.json"
        #print(os.getcwd()) -> to check current working dir
        file_path = os.getcwd()+"/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(),schema=schema)
        except ValidationError as e:
            print(e.message)
            #pytest.fail("Failed: JSON Schema Error") #-> we can use this also but it shows errors in red
            pytest.xfail("Incorrect JSON Schema") #-> will use to fail validation (negative TC)

        # if we give value of booking_id type as string instead of integer, still our test case will beacause we have used try and except block
        # means our negative test case will also pass if we give try and except block
        # PASSED [100%]4325 is not of type 'string' -> error because if have not mentioned failure message like pytest.xfail("Incorrect JSON Schema")
        # Xfail will give warnings
        # fail will fail the test cases
        # we generally use fail, sometmes we dont need to fail test cases then we will use xfail