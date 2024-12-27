import requests
import time

from shared.local_logger import log
from shared.omada.config import OmadaConfig

REFRESH_TOKEN_EXPIRY_TIME = 14 * 24 * 60 * 60  # 14 days

class OmadaAuthError(Exception):
    pass

class OmadaAuth:

    def __init__(self):
        self.config = OmadaConfig()
        self.csrf_token = None
        self.session_id = None
        self.access_token = None
        self.token_expiry_time = None
        self.refresh_token = None
        self.refresh_token_expiry_time = None

    def login(self):
        self.csrf_token, self.session_id = self.get_csrf_and_session_id()
        authorization_code = self.get_authorization_code()
        self.access_token, self.token_expiry_time, self.refresh_token, self.refresh_token_expiry_time = self.get_access_token(authorization_code=authorization_code)

    def logged_in(self) -> bool:
        return self.access_token is not None and self.token_expiry_time > time.time()

    def current_state(self) -> dict:
        return {
            "access_token": self.access_token,
            "token_expiry_time": self.token_expiry_time,
            "token_expires_in": self.token_expiry_time - time.time(),
            "refresh_token": self.refresh_token,
            "refresh_token_expiry_time": self.refresh_token_expiry_time,
            "refresh_token_expires_in": self.refresh_token_expiry_time - time.time()
        }

    def current_access_token(self) -> str:
        log("Getting current access token")
        try:
            if not self.logged_in():
                log("Not logged in, starting login process")
                self.login()
            else:
                # If the access token is present, but expired, refresh it
                if self.access_token and self.token_expiry_time < time.time():
                    log("Access token exists but is expired, refreshing")
                # If the refresh token is present, but expired, start the login process again
                if self.refresh_token and self.refresh_token_expiry_time < time.time():
                    log("Refresh token exists but is expired, starting login process again")
                    self.login()
                else:
                    log("Refresh token exists but is not expired, refreshing access token")
                    self.access_token, self.token_expiry_time = self.refresh_access_token()
        except OmadaAuthError as e:
            log(f"Auth error occurred: {str(e)}. Starting login process again.")
            self.login()

        log(f"Current access token: {self.access_token}, expiry time: {self.token_expiry_time}, refresh token expiry time: {self.refresh_token_expiry_time}")

        return self.access_token

    def get_csrf_and_session_id(self) -> tuple[str, str]:
        # Step 1: Login to get CSRF token and session ID
        # curl "https://omada.hosk.in/openapi/authorize/login?client_id=YOUR_CLIENT_ID&omadac_id=YOUR_OMADA_ID" \
        #   -H 'content-type: application/json' \
        #   -d '{"username":"YOUR_USERNAME","password":"YOUR_PASSWORD"}' \
        #   -X POST

        # Response will contain:
        # {
        #   "csrfToken": "TOKEN_HERE",
        #   "sessionId": "SESSION_ID_HERE"
        # }

        url = f"{self.config.host}/openapi/authorize/login?client_id={self.config.client_id}&omadac_id={self.config.omadac_id}"
        response = requests.post(url, headers={"content-type": "application/json"}, json={"username": self.config.username, "password": self.config.password})

        log(f"Login response status: {response.status_code}")

        if response.status_code != 200:
            raise OmadaAuthError(f"Get CSRF token and session ID failed with status code {response.status_code}")

        data = response.json()
        log(f"Get CSRF token and session ID response: {data}")

        if "result" not in data:
            raise OmadaAuthError(f"Get CSRF token and session ID failed with missing result: {data}")

        if "csrfToken" not in data["result"] or "sessionId" not in data["result"]:
            raise OmadaAuthError(f"Get CSRF token and session ID failed with missing CSRF token or session ID: {data}")

        csrf_token = data["result"]["csrfToken"]
        session_id = data["result"]["sessionId"]

        return csrf_token, session_id

    def get_authorization_code(self) -> str:
        # Step 2: Get authorization code
        # curl "https://omada.hosk.in/openapi/authorize/code?client_id=YOUR_CLIENT_ID&omadac_id=YOUR_OMADA_ID&response_type=code" \
        #   -H 'content-type: application/json' \
        #   -H 'Csrf-Token: YOUR_CSRF_TOKEN' \
        #   -H 'Cookie: TPOMADA_SESSIONID=YOUR_SESSION_ID' \
        #   -X POST

        url = f"{self.config.host}/openapi/authorize/code?client_id={self.config.client_id}&omadac_id={self.config.omadac_id}&response_type=code"
        response = requests.post(url, headers={"content-type": "application/json", "Csrf-Token": self.csrf_token, "Cookie": f"TPOMADA_SESSIONID={self.session_id}"})

        if response.status_code != 200:
            raise OmadaAuthError(f"Get authorization code failed with status code {response.status_code}")

        log(f"Authorization code response status: {response.status_code}")
        data = response.json()
        log(f"Authorization code response: {data}")

        if "result" not in data:
            raise OmadaAuthError(f"Get authorization code failed with missing result: {data}")

        return data["result"]

    def get_access_token(self, authorization_code: str) -> tuple[str, int, str, int]:
        # Step 3: Exchange authorization code for access token
        # curl "https://omada.hosk.in/openapi/authorize/token?grant_type=authorization_code&code=YOUR_AUTH_CODE" \
        #   -H 'content-type: application/json' \
        #   -d '{"client_id": "YOUR_CLIENT_ID", "client_secret": "YOUR_CLIENT_SECRET"}' \
        #   -X POST

        # Response:

        # {"errorCode":0,"msg":"Open API Get Access Token successfully.","result":{"accessToken":"AT-bllLYOOYASck11SBSDmmHs85lCrkN6Gi","tokenType":"bearer","expiresIn":7200,"refreshToken":"RT-HqvaDuSxEqayM75U2ukTRnBl6f6fiRAc"}}

        url = f"{self.config.host}/openapi/authorize/token?grant_type=authorization_code&code={authorization_code}"
        response = requests.post(url, headers={"content-type": "application/json"}, json={"client_id": self.config.client_id, "client_secret": self.config.client_secret})

        if response.status_code != 200:
            raise OmadaAuthError(f"Get access token failed with status code {response.status_code}")

        log(f"Access token response status: {response.status_code}")
        data = response.json()
        log(f"Access token response: {data}")

        if "result" not in data:
            raise OmadaAuthError(f"Get access token failed with missing result: {data}")

        access_token = data["result"]["accessToken"]
        # Convert expiry seconds to future timestamp
        token_expiry_time = int(time.time()) + data["result"]["expiresIn"]
        refresh_token = data["result"]["refreshToken"]
        refresh_token_expiry_time = int(time.time()) + REFRESH_TOKEN_EXPIRY_TIME

        return access_token, token_expiry_time, refresh_token, refresh_token_expiry_time

    def refresh_access_token(self) -> tuple[str, int]:
        #     Refresh Access Token
        #     Currently, the access token is valid for 2 hours, and the refresh token is valid for 14 days. If the access token expires, you can use the refresh token interface to obtain a new access token. The refresh access token interface uses the POST method, the interface path is as follows: /openapi/authorize/token. If the refresh token also expires, you will need to go through the previous authentication process again.

        #     In the Query, fill in the grant type(The field name is grant_type), refresh token(The field name is refresh_token). The grant type indicate the authentication method, and the refresh token needs to be filled in with "refresh_token"
        #     In the Body, fill in the client ID(the field name is client_id) and client secret(the field name is client_secret).
        #     An example of the curl command of the refresh token interface is as follows: Request:

        #     curl "https://localhost:8043/openapi/authorize/token?client_id=185586e0df424f5ea938de13cba91e01&client_secret=767372a5258a4fc1a03c57f3d071fc35&refresh_token=RT-AhzwqCenDCZ84qpBHnZhYs3j2RGw9q8E&grant_type=refresh_token" -H 'content-type:application/json' -X POST -i -k --insecure
        #     Response:

        #     {"errorCode":0,"msg":"Open API Get Access Token successfully.","result":{"accessToken":"AT-w9veJNQlaK8dH08qEQZCTas6y70IRAii","tokenType":"bearer","expiresIn":7001,"refreshToken":"RT-AhzwqCenDCZ84qpBHnZhYs3j2RGw9q8E"}}

        url = f"{self.config.host}/openapi/authorize/token?grant_type=refresh_token&refresh_token={self.refresh_token}"
        response = requests.post(url, headers={"content-type": "application/json"}, json={"client_id": self.config.client_id, "client_secret": self.config.client_secret})

        if response.status_code != 200:
            raise OmadaAuthError(f"Refresh access token failed with status code {response.status_code}")

        log(f"Refresh access token response status: {response.status_code}")
        data = response.json()
        log(f"Refresh access token response: {data}")

        if "result" not in data:
            raise OmadaAuthError(f"Refresh access token failed with missing result: {data}")

        access_token = data["result"]["accessToken"]
        # Convert expiry seconds to future timestamp
        token_expiry_time = int(time.time()) + data["result"]["expiresIn"]

        return access_token, token_expiry_time
