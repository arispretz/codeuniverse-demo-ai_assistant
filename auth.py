import os
import json
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import Header, HTTPException

# Only initialize Firebase if not in test mode
if os.getenv("TEST_MODE") != "true":
    firebase_credentials = json.loads(os.environ.get("FIREBASE_CREDENTIAL_JSON", "{}"))
    cred = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(cred)

def verify_token(authorization: str = Header(...)):
    """
    Verify Firebase authentication token.
    In test mode, accepts any token and returns a fake user.
    """
    if os.getenv("TEST_MODE") == "true":
        return {"uid": "test_user", "email": "test@example.com"}

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ")[1]
    try:
        decoded = auth.verify_id_token(token)
        return decoded
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
