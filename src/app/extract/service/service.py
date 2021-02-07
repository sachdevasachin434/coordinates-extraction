"""
    Service Layer for Longitude and Lattitude Extraction.
"""
import json
import os.path as path
import requests


class FetchLongitudeAndLattitude:
    """
    Class for the service layer of post api.
    """

    @staticmethod
    def find_geocode(request):
        """Method to make required data arrangements for input and fetch longitude and lattitude.

        Args:
            request (request): request containg address and output format.

        Returns:
            Dict: Conatins error message as key if there is problem with key, else returns result.
        """
        config_path = path.abspath(path.join(__file__, "../../../../config.json"))
        address = request.get_json(force=True)["address"]
        address = address.replace(" ", "+")
        with open(config_path, "r") as jsonfile:
            data = json.load(jsonfile)
        key = data["GCP Key"]
        response = requests.get(
            f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}"
        )
        resp_json_payload = response.json()
        if "error_message" in resp_json_payload.keys():
            return {"error_message": resp_json_payload["error_message"]}

        long_latt_dict = resp_json_payload["results"][0]["geometry"]["location"]
        return {"coordinates": long_latt_dict, "address": address}
