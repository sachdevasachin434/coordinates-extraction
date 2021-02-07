import json
import pytest
import io
from ..main import app
from re import search


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test with correct GCP Key with Maps Embed API enabled.
# def test_with_correct_input(client):
#     data = {
#         "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
#         "output_format": "json"
#     }
#     response = client.post("/getAddressDetails", data=data)
#     data = response.json
#     status_code = response.status_code
#     assert "coordinates" in data.keys() and "address" in data.keys()
#     assert status_code == 200

# def test_with_output_format_as_xml_with_valid_key(client):
#     data = {
#         "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
#         "output_format": "xml"
#     }
#     response = client.post("/getAddressDetails", json=data)
#     import pdb; pdb.set_trace()
#     data = response.data
#     status_code = response.status_code
#     assert search("xml version", data)
#     assert search("address", data)
#     assert search("coordinates", data)
#     assert status_code == 200

def test_with_correct_input_wrong_key(client):
    data = {
        "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": "json"
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert status_code == 400

def test_wrong_address_instance(client):
    data = {
        "address": ["3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008"],
        "output_format": "json"
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert search("Please pass address in a string format.", data["error_message"])
    assert status_code == 400

def test_wrong_output_format_instance(client):
    data = {
        "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": 11
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert search("Please pass output_format as string.", data["error_message"])
    assert status_code == 400

def test_wrong_output_format(client):
    data = {
        "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": "abc"
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert search("Please pass correct output_format. Allowed are json or xml.", data["error_message"])
    assert status_code == 400

def test_without_address(client):
    data = {
        # "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": "abc"
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert search("Please pass address in input json.", data["error_message"])
    assert status_code == 400

def test_without_output_format(client):
    data = {
        "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        # "output_format": "abc"
    }
    response = client.post("/getAddressDetails", json=data)
    data = response.json
    status_code = response.status_code
    assert "error_message" in data.keys()
    assert search("Please pass output_format in input json.", data["error_message"])
    assert status_code == 400

def test_with_output_format_as_xml_with_invalid_key(client):
    data = {
        "address": "3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": "xml"
    }
    response = client.post("/getAddressDetails", json=data)
    data = str(response.data)
    status_code = response.status_code
    assert search("xml version""", data)
    assert search("error_message", data)
    assert search("The provided API key is invalid.", data)
    assert status_code == 400
