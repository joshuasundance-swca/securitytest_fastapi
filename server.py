# import os

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from keys import correct_key

app = FastAPI()

# API_KEY = os.environ.get("SECURITYTEST_FASTAPI_API_KEY")
# if API_KEY is None:
#     raise RuntimeError("API key is not set")
API_KEY = correct_key
API_KEY_NAME = "access-token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get("/protected-endpoint")
async def protected_endpoint(api_key: str = Depends(get_api_key)):
    return {"message": "Access granted to protected endpoint"}
