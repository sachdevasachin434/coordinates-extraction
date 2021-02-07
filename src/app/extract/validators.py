"""
    HTTP argument validation
"""
from marshmallow import ValidationError


def validate_input(input_dict):
    """Validator function to validate the input parameters.

    Args:
        input_dict (dict): {"address": "H.No. 2552, Panipat, Haryana", "output_format": "json"}

    Raises:
        ValidationError: Please pass address in input json.
        ValidationError: Please pass output_format in input json.
        ValidationError: Please pass correct output_format. Allowed are json or xml.
        ValidationError: Please pass address in a string format.
    """
    if "address" not in input_dict.keys():
        raise ValidationError("Please pass address in input json.")
    if "output_format" not in input_dict.keys():
        raise ValidationError("Please pass output_format in input json.")
    if not isinstance(input_dict["output_format"], str):
        raise ValidationError(
            "Please pass output_format as string."
        )
    if input_dict["output_format"] not in ["json", "xml"]:
        raise ValidationError(
            "Please pass correct output_format. Allowed are json or xml."
        )
    if not isinstance(input_dict["address"], str):
        raise ValidationError("Please pass address in a string format.")
