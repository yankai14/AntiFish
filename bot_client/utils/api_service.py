from dataclasses import dataclass
import requests
import json

import urllib
from config import ENV


@dataclass
class ApiEndpoints:
    VALIDATE_URL: str = "/validateUrl"
    REPORT_URL: str = "/report"

    def __init__(self):
        for attr in dir(self):
            if not attr.startswith("__"):
                setattr(self, attr, ENV.API_BASE_URL + getattr(self, attr))


APIEndpoints = ApiEndpoints()


class ApiService:

    @staticmethod
    def validate_url(url: str) -> tuple[dict, int]:
        headers = {
            "Content-Type": "application/json"
        }
        # encode url
        url = urllib.parse.quote(url)

        response = requests.get(
            APIEndpoints.VALIDATE_URL + "?url=" + url,
            headers=headers
        )
        validation = response.json()
        if validation.get("fish"):
            isPhish = validation.get("fish")
        else:
            isPhish = False
        status_code = response.status_code

        return isPhish, status_code

    @staticmethod
    def report_url(url: str) -> int:
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            APIEndpoints.REPORT_URL,
            headers=headers,
            data=json.dumps({"url": url}),
        )
        status_code = response.status_code

        return status_code



