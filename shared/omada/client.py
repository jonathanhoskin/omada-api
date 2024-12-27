import requests

from shared.local_logger import log

from shared.omada.config import OmadaConfig
from shared.omada.auth import OmadaAuth

class OmadaClient:

    def __init__(self, auth: OmadaAuth):
        self.config = OmadaConfig()
        self.auth = auth

    def list(self):
        url = f"{self.config.host}/openapi/v1/{self.config.omadac_id}/sites/{self.config.site_id}/clients"
        response = requests.get(url, headers={"Authorization": f"Bearer {self.auth.current_access_token()}"}, timeout=10)
        log(f"Response status: {response.status_code}")
        data = response.json()
        log(f"Response data: {data}")
        return data
