import os
from dotenv import load_dotenv

class OmadaConfig:

    def __init__(self):
        load_dotenv()
        self.host = os.getenv("OMADA_API_HOST")
        self.client_id = os.getenv("OMADA_API_CLIENT_ID")
        self.omadac_id = os.getenv("OMADA_API_OMADAC_ID")
        self.client_secret = os.getenv("OMADA_API_CLIENT_SECRET")
        self.username = os.getenv("OMADA_API_USERNAME")
        self.password = os.getenv("OMADA_API_PASSWORD")
