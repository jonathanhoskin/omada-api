from fastapi import FastAPI
import uvicorn

from shared.local_logger import log
from shared.omada.auth import OmadaAuth
from shared.omada.client import OmadaClient
from shared.omada.site import OmadaSite

app = FastAPI()
auth = OmadaAuth()
client = OmadaClient(auth)
site = OmadaSite(auth)

@app.get("/auth/login")
async def login():
    auth.login()
    if auth.logged_in():
        return {"status": "success"}
    else:
        return {"status": "failed"}

@app.get("/auth/state")
async def auth_state():
    return auth.current_state()

@app.get("/auth/access_token")
async def get_access_token():
    access_token = auth.current_access_token()
    return {"access_token": access_token}

@app.get("/clients/list")
async def list_clients():
    return {"clients": client.list()}

@app.get("/sites/list")
async def list_sites():
    return {"sites": site.list()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
