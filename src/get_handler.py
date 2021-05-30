"""Send GET request to AWS to retrieve data."""
import sys
import os
import datetime
import hashlib
import hmac
import json
import requests

from . import arguments
# import arguments

# REQUEST VALUES
METHOD = "GET"
SERVICE = "execute-api"
REGION = "us-east-2"


def auth_config():
    """Authorization configuration."""
    api_key = os.environ.get("GATOR_API_KEY")
    endpoint = os.environ.get("GATOR_ENDPOINT")
    # Read AWS access key from env. variables or configuration file
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    if access_key is None:
        raise EnvironmentError("No aws access key is given.")
    if secret_key is None:
        raise EnvironmentError("No aws secret key is given.")
    if api_key is None:
        raise EnvironmentError("No gator api key is given.")
    if endpoint is None:
        raise EnvironmentError("No gator endpoint is given.")

    return {
        "api_key": api_key,
        "endpoint": endpoint,
        "access_key": access_key,
        "secret_key": secret_key,
    }


def sign(key, msg):
    """Key derivation functions from AWS."""
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def get_signature_key(key, date_stamp, region_name, service_name):
    """Key derivation functions from AWS."""
    k_date = sign(("AWS4" + key).encode("utf-8"), date_stamp)
    k_region = sign(k_date, region_name)
    k_service = sign(k_region, service_name)
    k_signing = sign(k_service, "aws4_request")
    return k_signing


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def get_request(
        assignment, passbuild, api_key, endpoint, access_key, secret_key):
    """Create and sign request."""
    # Create a date for headers and the credential string
    time = datetime.datetime.utcnow()
    amzdate = time.strftime("%Y%m%dT%H%M%SZ")
    # Date w/o time, used in credential scope
    datestamp = time.strftime("%Y%m%d")

    host, stage, method = endpoint.replace("https://", "").split("/")
    canonical_uri = "/" + stage + "/" + method

    # query
    request_parameters = f"assignment={assignment}&passBuild={str(passbuild)}"
    # Create the canonical query string
    canonical_querystring = request_parameters

    # Create the canonical headers and signed headers. Header names
    # must be trimmed and lowercase, and sorted in code point order from
    # low to high. Note that there is a trailing \n.
    canonical_headers = (
        "host:"
        + host
        + "\n"
        + "x-amz-date:"
        + amzdate
        + "\n"
        + "x-api-key:"
        + api_key
        + "\n"
    )

    # Create the list of signed headers. This lists the headers
    # in the canonical_headers list, delimited with ";" and in alpha order.
    signed_headers = "host;x-amz-date;x-api-key"

    # Create payload hash (hash of the request body content). For GET
    # requests, the payload is an empty string ("").
    payload_hash = hashlib.sha256(("").encode("utf-8")).hexdigest()

    # Combine elements to create canonical request
    canonical_request = (
        METHOD
        + "\n"
        + canonical_uri
        + "\n"
        + canonical_querystring
        + "\n"
        + canonical_headers
        + "\n"
        + signed_headers
        + "\n"
        + payload_hash
    )

    # print(canonical_request)

    # CREATE THE STRING TO SIGN
    # Match the algorithm to the hashing algorithm you use, either SHA-1 or
    # SHA-256 (recommended)
    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = (
        datestamp + "/" + REGION + "/" + SERVICE + "/" + "aws4_request"
    )
    string_to_sign = (
        algorithm
        + "\n"
        + amzdate
        + "\n"
        + credential_scope
        + "\n"
        + hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
    )

    # CALCULATE THE SIGNATURE
    # Create the signing key using the function defined above.
    signing_key = get_signature_key(secret_key, datestamp, REGION, SERVICE)

    # Sign the string_to_sign using the signing_key
    signature = hmac.new(
        signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256
    ).hexdigest()

    # ADD SIGNING INFORMATION TO THE REQUEST
    # The signing information can be either in a query string value or in
    # a header named Authorization
    authorization_header = (
        algorithm
        + " "
        + "Credential="
        + access_key
        + "/"
        + credential_scope
        + ", "
        + "SignedHeaders="
        + signed_headers
        + ", "
        + "Signature="
        + signature
    )

    # headers include "host", "x-amz-date", and "Authorization"
    # The 'host' header is added automatically by the Python 'requests' library
    headers = {
        "x-api-key": api_key,
        "x-amz-date": amzdate,
        "Authorization": authorization_header,
    }

    request_url = endpoint + "?" + request_parameters

    # SEND THE REQUEST
    try:
        response = requests.get(request_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
        raise Exception(f"Http Error: {errh}") from errh
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        raise Exception(f"Connecting Error: {errc}") from errc
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        raise Exception(f"Timeout Error: {errt}") from errt
    except requests.exceptions.RequestException as err:
        print("RequestException:", err)
        raise Exception(f"RequestException: {err}") from err
    if not response.json():
        raise Exception("The response is empty, the requested \
assignment might not be in the database")
    return response.json()


if __name__ == "__main__":
    get_arguments = arguments.parse(sys.argv[1:])
    arg_assignment = get_arguments.assignment
    arg_passbuild = get_arguments.passBuild
    configs = auth_config()
    print(json.dumps(get_request(arg_assignment, arg_passbuild, **configs)))
