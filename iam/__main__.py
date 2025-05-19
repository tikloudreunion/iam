import os
import logging

from uvicorn import Config, Server
from fastapi import FastAPI

if __name__ == "__main__":
    server_host = os.getenv("SERVER_HOST", "127.0.0.1")
    try:
        server_port = int(os.getenv("SERVER_PORT", 3000))
    except ValueError:
        logging.error("Invalid port number. Using default port 3000.")
        server_port = 3000

    logging.info(f"Starting server on {server_host}:{server_port}")

    logging.debug(f"Server host: {server_host}, Server port: {server_port}")
    fastapi_application = FastAPI()

    logging.debug("Configuring Uvicorn server.")
    uvicorn_config = Config(app=fastapi_application, host=server_host, port=server_port)

    logging.debug("Starting Uvicorn server.")
    server = Server(config=uvicorn_config)

    try:
        logging.info("Running Uvicorn server.")
        server.run()
    except Exception as exception:
        logging.error(f"Error occurred while running the server: {exception}")
    finally:
        logging.info("Server stopped.")
        server.should_exit = True
        server.should_reload = False
        server.should_restart = False
        server.should_exit = True
        logging.info("Server cleanup completed.")
