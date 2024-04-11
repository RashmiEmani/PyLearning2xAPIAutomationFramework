# payload manager helps you to keep the payload
# dictionary payload

from faker import Faker
import json

faker = Faker()


def payload_create_booking():
    payload = {
        "firstname": "Rashmi",
        "lastname": "Emani",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-18",
            "checkout": "2024-03-21"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():  # dynamic data by using faker library
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2024-03-18",
            "checkout": "2024-03-21"
        },
        "additionalneeds": faker.random_elements(elements=("Breakfast", "Parking", "Wifi", "Extra Bed"))
    }


# def payload_create_booking_data_excel():
#     payload = {
#         "firstname" : read.From.excel["firstname"],
#         "lastname" : "Emani",
#         "totalprice" : 1000,
#         "depositpaid" : True,
#         "bookingdates" : {
#             "checkin" : "2024-03-18",
#             "checkout" : "2024-03-21"
#         },
#         "additionalneeds" : "Breakfast"
#     }
#         return payload
def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
