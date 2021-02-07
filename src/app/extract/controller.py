"""
    Endpoint controller layer of the project
"""
import dicttoxml
from flask import request, Response
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from .service.service import FetchLongitudeAndLattitude
from .validators import validate_input

API = Namespace("Extract", description="Extract API")


@API.route("/getAddressDetails")
class GetLongitudeLattitude(Resource):
    """
    Class handling HTTP requests to endpoint /getAddressDetails
    """

    @classmethod
    def post(cls):
        """Flask Post Method

        Returns:
            xml or json: Returns result as xml or json as per output_format mentioned.
        """
        try:
            validate_input(request.get_json(force=True))
        except ValidationError as err:
            return {"error_message": str(err)}, 400

        result = FetchLongitudeAndLattitude.find_geocode(request)

        if "error_message" in result:
            if request.get_json(force=True)["output_format"].lower() == "xml":
                result = dicttoxml.dicttoxml(result)
                return Response(result, mimetype="text/xml", status=400)
            return result, 400
        if request.get_json(force=True)["output_format"].lower() == "xml":
            result = dicttoxml.dicttoxml(result)
            return Response(result, mimetype="text/xml", status=200)
        return result, 200
