import os
import uvicorn

def main():
    """
    Entry point for running the FastAPI application with Uvicorn.

    Environment Variables:
        HOST (str): Host address to bind the server.
        PORT (int): Port number to run the server.
    """
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    if not host or not port:
        raise RuntimeError("HOST and PORT must be set in environment variables")

    uvicorn.run("main:app", host=host, port=int(port))

if __name__ == "__main__":
    main()
