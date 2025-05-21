from fastapi import FastAPI

NAME = "IAM - Ti Kloud Réunion"
DESCRIPTION = "This is the IAM API for Ti Kloud Réunion"
VERSION = "0.1.0"

fastapi_application = FastAPI(
    title=NAME,
    description=DESCRIPTION,
    version=VERSION,
)
