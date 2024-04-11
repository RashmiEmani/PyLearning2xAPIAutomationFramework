def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP Status Code (Failed Message)"


def verify_json_key_for_not_null(key):  # here key is used for booking_id
    assert key != 0, "Failed - Key is non empty " + key
    assert key > 0, "Failed - Key is greater than zero"

def verify_json_key_for_not_null_token(key):  # here key is used for booking_id
    assert key != 0, "Failed - Key is non empty " + key

def verify_response_key_should_not_be_none(key):
    assert key is not None


def verify_response_delete(response):
    assert "Created" in response


def verify_response_key(key,expected_data):
    assert key == expected_data

# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# Json Schema
