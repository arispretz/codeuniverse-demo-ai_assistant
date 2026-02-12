from pydantic import BaseModel
from typing import Literal, Optional

class CodePrompt(BaseModel):
    """
    Model representing a code generation prompt.

    Attributes:
        prompt (str): The text prompt describing the task.
        language (str): Programming language for the generated code. Defaults to "python".
        user_id (Optional[str]): Optional identifier for the user.
    """
    prompt: str
    language: str = "python"
    user_id: Optional[str] = None


class CodeInput(BaseModel):
    """
    Model representing code input for processing.

    Attributes:
        code (str): The code snippet provided by the user.
        language (str): Programming language of the code. Defaults to "python".
        user_id (Optional[str]): Optional identifier for the user.
    """
    code: str
    language: str = "python"
    user_id: Optional[str] = None


class CodeOnly(BaseModel):
    """
    Model representing a request containing only code.

    Attributes:
        code (str): The code snippet provided by the user.
        user_id (Optional[str]): Optional identifier for the user.
    """
    code: str
    user_id: Optional[str] = None


class CodeRequest(BaseModel):
    """
    Model representing a complete code-related request.

    Attributes:
        prompt (str): The text prompt describing the task.
        language (str): Programming language of the code.
        code (str): The code snippet provided by the user.
        user_id (str): Identifier for the user.
        user_level (Literal): User expertise level. Options: "beginner", "intermediate", "advanced".
                              Defaults to "intermediate".
    """
    prompt: str
    language: str
    code: str
    user_id: str
    user_level: Literal["beginner", "intermediate", "advanced"] = "intermediate"
