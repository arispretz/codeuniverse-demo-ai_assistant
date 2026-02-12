import os
import pytest
import requests
from dotenv import load_dotenv

# Compute absolute path to project root and load .env.test
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # tests/
PROJECT_ROOT = os.path.dirname(BASE_DIR)               # ai_assistant/
load_dotenv(os.path.join(PROJECT_ROOT, ".env.test"))

# Load base URL strictly from environment variable
BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise RuntimeError("BASE_URL is not set in environment variables")

# Common authorization header for all requests
AUTH_HEADERS = {"Authorization": "Bearer test_token"}

@pytest.mark.parametrize("payload", [
    {"prompt": "Create a function that reverses a string", "language": "python", "user_id": "demo_user"},
])
def test_generate(payload):
    """
    Test the /generate endpoint to ensure it returns valid code.
    """
    res = requests.post(f"{BASE_URL}/generate", json=payload, headers=AUTH_HEADERS)
    print(res.json())
    assert res.status_code == 200
    data = res.json()
    assert "code" in data
    assert isinstance(data["code"], str)


@pytest.mark.parametrize("payload", [
    {
        "prompt": "Explain how this factorial function works",
        "language": "python",
        "code": "def factorial(n): return 1 if n<=1 else n*factorial(n-1)",
        "user_id": "demo_user",
        "user_level": "intermediate"
    },
])
def test_reply(payload):
    """
    Test the /reply endpoint to ensure it returns a mentor-style explanation.
    """
    res = requests.post(f"{BASE_URL}/reply", json=payload, headers=AUTH_HEADERS)
    print(res.json())
    assert res.status_code == 200
    data = res.json()
    assert "reply" in data
    assert isinstance(data["reply"], str)


@pytest.mark.parametrize("payload", [
    {
        "prompt": "Generate code that calculates the average of a list",
        "language": "python",
        "code": "def average(lst): return sum(lst)/len(lst)",
        "user_id": "demo_user",
        "user_level": "intermediate"
    },
])
def test_reply_code_only(payload):
    """
    Test the /reply-code-only endpoint to ensure it returns valid code only.
    """
    res = requests.post(f"{BASE_URL}/reply-code-only", json=payload, headers=AUTH_HEADERS)
    print(res.json())
    assert res.status_code == 200
    data = res.json()
    assert "code" in data
    assert isinstance(data["code"], str)
