# test for a missing worker_id in the payload with the right sceret

from fastapi import HTTPException
import pytest
from fastapi.security import HTTPAuthorizationCredentials
from dependencies import verify_tokens
from config import jwt_secret
from auth import jwt
from datetime import timezone, timedelta, datetime

def test_token_without_worker_id():
    payload = {"name": "raghav",
                                   "exp": datetime.now(tz=timezone.utc) + timedelta(hours=2),
                                   "role": "worker"}
    token_string = jwt.encode(payload, jwt_secret, algorithm="HS256")
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token_string)

    with pytest.raises(HTTPException) as exc_info:
        verify_tokens(credentials)

    assert exc_info.value.status_code == 401