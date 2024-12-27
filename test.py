# Write a script to test the omada api

from shared.omada.auth import OmadaAuth

auth = OmadaAuth()
auth.login()

print(auth.current_access_token())
