"""Send GET request to AWS to retrieve data"""
import sys
import os
import datetime
import hashlib
import hmac
import requests

# REQUEST VALUES
METHOD = "GET"
SERVICE = "execute-api"
REGION = "us-east-2"
API_KEY = os.environ.get("GATOR_API_KEY")
ENDPOINT = os.environ.get("GATOR_ENDPOINT")
# Read AWS access key from env. variables or configuration file
ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
if ACCESS_KEY is None or SECRET_KEY is None:
    print("No access key is available.")
    sys.exit()


def sign(key, msg):
    """Key derivation functions from AWS"""
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def getSignatureKey(key, dateStamp, regionName, serviceName):
    """Key derivation functions from AWS"""
    k_date = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    k_region = sign(k_date, regionName)
    k_service = sign(k_region, serviceName)
    k_signing = sign(k_service, "aws4_request")
    return k_signing


def get_request(assignment):
    """Create and sign request"""
    # Create a date for headers and the credential string
    t = datetime.datetime.utcnow()
    amzdate = t.strftime("%Y%m%dT%H%M%SZ")
    datestamp = t.strftime("%Y%m%d")  # Date w/o time, used in credential scope

    host, stage, method = ENDPOINT.replace('https://', '').split('/')
    canonical_uri = "/" + stage + '/' + method

    # query
    request_parameters = f"assignment={assignment}"
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
        + API_KEY
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

    # CREATE THE STRING TO SIGN
    # Match the algorithm to the hashing algorithm you use, either SHA-1 or
    # SHA-256 (recommended)
    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = datestamp + "/" \
        + REGION + "/" + SERVICE + "/" + "aws4_request"
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
    signing_key = getSignatureKey(SECRET_KEY, datestamp, REGION, SERVICE)

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
        + ACCESS_KEY
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
        "x-api-key": API_KEY,
        "x-amz-date": amzdate,
        "Authorization": authorization_header,
    }

    # SEND THE REQUEST
    request_url = ENDPOINT + "?" + request_parameters

    print("\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++")
    print("Request URL = " + request_url)
    r = requests.get(request_url, headers=headers)
    print("\nRESPONSE++++++++++++++++++++++++++++++++++++")
    print("Response code: %d\n" % r.status_code)

    return r.text


if __name__ == '__main__':
    response = get_request(input("Assignment name: \n"))
    print(response)
